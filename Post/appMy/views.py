from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request, cate="Null"):
    cards=Card.objects.all()

    cards_filter=Card.objects.filter(active=True)

    if cate=="Null":
        cards_filter=Card.objects.all()
    else:
        cards_filter=Card.objects.filter(category=cate)

    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        title=request.POST.get("title")
        text=request.POST.get("text")

        cont=Contact(name=name, email=email, title=title, text=text)
        cont.save()

    context={
        "cards":cards,
        "cards_filter":cards_filter,
    }
    return render(request,'index.html',context)


def detail(request,id):
    card=get_object_or_404(Card, id=id)

    comments=Comment.objects.filter(product=card)

    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        text=request.POST.get("text")

        com=Comment(name=name, email=email, text=text, product=card)
        com.save()

    context={
        "card":card,
        "comments":comments,
    }
    return render(request,'detail.html',context)




def loginUser(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            hata="KULLANICI ADI VEYA ŞİFRE YANLIŞ"
            context={
                "hata":hata,
            }
            return render(request,'user/login.html',context)
    
    context={}
    return render(request,'user/login.html',context)



def registerUser(request):

    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        if password1==password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user=User.objects.create_user(username=username, email=email, password=password2, first_name=name)
                    user.save()

                    userinfo=UserInfo(user=user, password=password1)
                    userinfo.save()

                    return redirect("loginUser")
                
                else:
                    context={"hata":"BU E-MAIL ZATEN KULLANILIYOR"}
                    return render(request,'user/register.html',context)
            else:
                context={"hata":"BU KULLANICI ADI ZATEN KULLANILIYOR"}
                return render(request,'user/register.html',context)
        else:
            context={"hata":"ŞİFRELER UYUŞMUYOR"}
            return render(request,'user/register.html',context)
    
    else:
        context={}
        return render(request,'user/register.html',context)
    
def logoutUser(request):
    logout(request)
    return redirect("loginUser")



def profileUser(request):
    user=User.objects.get(username=request.user)

    userinfo=UserInfo.objects.get(user=user)

    if request.method=="POST":
        name=request.POST.get("name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        image=request.FILES.get("image")
        job=request.POST.get("job")
        tel=request.POST.get("tel")
        address=request.POST.get("address")
        password=request.POST.get("password")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        user.email=email
        user.username=username
        user.first_name=name
        userinfo.tel=tel
        userinfo.job=job
        userinfo.address=address
        userinfo.image=image

        if password and password1 and password2:
            if user.check_password(password):
                if password1==password2:
                    userinfo.password=password2
                    user.set_password(password1)

        user.save()
        userinfo.save()
        login(request,user)
        return redirect("profileUser")
    
    context={
        "userinfo":userinfo,
    }
    return render(request,'user/profile.html',context)
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home") 
        else:
            return render(request, "user_login.html", {"error": "Invalid Credential"})



    return render(request,"user_login.html")




def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")

        

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "register.html", {"error": "Bu kullanıcı adı zaten kullanılıyor.",
                                                         "username": username,
                                                         "email": email,
                                                         "first_name": first_name,
                                                         "last_name": last_name,
                                                         "address": address,
                                                         "gender": gender,
                                                         "phone": phone})
            elif User.objects.filter(email=email).exists():
                return render(request, "register.html", {"error": "Bu e-posta adresi zaten kullanılıyor.",
                                                         "username": username,
                                                         "email": email,
                                                         "first_name": first_name,
                                                         "last_name": last_name,
                                                         "address": address,
                                                         "gender": gender,
                                                         "phone": phone})
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,

                    
                )

                user.save()
                return redirect("login")
        else:
            return render(request, "register.html", {"error": "Parolalar eşleşmiyor.",
                                                     "username": username,
                                                     "email": email,
                                                     "first_name": first_name,
                                                     "last_name": last_name,
                                                     "address": address,
                                                     "gender": gender,
                                                     "phone": phone})
    return render(request, "register.html")



def user_logout(request):
    logout(request)
    return redirect("home")
































from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,AddPostForm,ForgotPasswordSendingForm,SimplePasswordResetForm,PasswordChangeFormCustom
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Post
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail  
from django.conf import settings
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user = request.user,is_deleted=False)
        context = {
            "posts":posts
        }
        return render(request,"home.html",context)
    else:
        return render(request,"home.html")

def test(request):
    return render(request,"test.html")
def register(request):
    if request.user.is_authenticated:
        messages.warning(request,"you are already logged in")
        return redirect("home")
    url = request.META.get('HTTP_REFERER')
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            mail = form.cleaned_data['email']
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            user.email = mail
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,"User Created Successfully")
            return redirect('home')
    return render(request,"register.html",{"form":form})

def login_user(request):
    if request.user.is_authenticated:
        messages.warning(request,"you are already logged in")
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(request.user)
            messages.success(request,"logged in successfully")
            return redirect("home")
        else:
            messages.warning(request,"invalid username or password!!!")
            return redirect("login_user")
    return render(request,"login.html")
@login_required(login_url="login_user")
def logout_user(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect("home")
@login_required(login_url="login_user")
def user_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,"post created successfully")
            return redirect("home")
    else:
        form = AddPostForm()
    return render(request,"add_post.html",{"form":form})


@login_required(login_url="login_user")
def edit_post(request):
    if request.method == "POST":
        post_id = request.POST.get("hidden")
        print(post_id)
        pst = Post.objects.get(pk=post_id)  
        print(request)
        title = request.POST.get("title")
        content = request.POST.get("content")
        pst.title = title    
        pst.content = content
        pst.save()
        messages.success(request,"post edited successfully")
        return redirect("home")
    return redirect("home")

@login_required(login_url="login_user")
def delete_post(request):
    post_id = request.POST.get("hidden")
    print(post_id)
    post = Post.objects.get(pk=post_id)
    post.is_deleted = True
    post.save()
    messages.success(request,"post deleted successfully")
    return redirect("home")

@login_required(login_url="login_user")
def change_password(request):
    form = PasswordChangeFormCustom()
    if request.method == "POST":
        o_pass = request.POST.get("old_password")
        n_pass = request.POST.get("new_password")
        c_pass = request.POST.get("confirm_password")
        user = User.objects.get(username=request.user)

        if user.check_password(o_pass):
            if n_pass == c_pass:
                user.set_password(n_pass)
                update_session_auth_hash(request,user)
                user.save()
                messages.success(request,"password changed successfully")
                return redirect("home")
            else:
                messages.warning(request,"new password and confirm password does not match")
                return redirect("change_password")
        else:
            messages.warning(request,"old password is incorrect")
            return redirect("change_password")
    return render(request,"change_password.html" ,{"form":form})

def forgot_password(request):
    form = SimplePasswordResetForm()
    if request.method == "POST":
        print("hello")
        form = SimplePasswordResetForm(request.POST)
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            url = f"http://127.0.0.1:8000/forgot-password-sent/{uid}/{token}"
            subject = "Reset Password"
            message = f"click on the link to reset your password {url}"
            send_mail(subject,message,from_email=settings.EMAIL_HOST_USER,recipient_list=[user.email,])
            messages.success(request,"password reset link sent to your mail")
            return redirect("login_user")
        return redirect("login_user")
    return render(request,"forgot_password.html",{"form":form})


def forgot_password_send(request,uid,token):
    redirect_url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        uids = urlsafe_base64_decode(uid)
        user = User.objects.get(pk=uids)
        if default_token_generator.check_token(user,token):
            form = ForgotPasswordSendingForm(request.POST)
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request,"password changed successfully")
                return redirect("login_user")
            else:
                messages.warning(request,"new password and confirm password does not match")
                return redirect(redirect_url)
        else:
            messages.warning(request,"something happend wrong try again")
            return redirect("forgot_password")
    else:
        form = ForgotPasswordSendingForm()
        return render(request,"forgot_password_send.html",{"form":form})

        
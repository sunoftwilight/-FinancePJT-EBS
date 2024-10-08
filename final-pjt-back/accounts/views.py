from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse




def get_user_info(request, username):
    if request.method == 'GET':
        currentuser = get_user_model().objects.get(username=username)
        serializer = UserSerializer(currentuser)
        return JsonResponse({'data': serializer.data})
# Create your views here.
# def login(request):
#     if request.user.is_authenticated:
#         return redirect('articles:index')

#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect('articles:index')
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/login.html', context)


# @login_required
# def logout(request):
#     auth_logout(request)
#     return redirect('articles:index')


# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('articles:index')

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('articles:index')
#     else:
#         form = CustomUserCreationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/signup.html', context)


# @login_required
# def delete(request):
#     request.user.delete()
#     return redirect('articles:index')


# @login_required
# def update(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('articles:index')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/update.html', context)


# @login_required
# def change_password(request, user_pk):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             return redirect('articles:index')
#     else:
#         form = PasswordChangeForm(request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/change_password.html', context)


# def profile(request, username):
#     # User의 Detail 페이지
#     # User를 조회
#     person = get_user_model().objects.get(username=username)
#     context = {
#         'person': person,
#     }
#     return render(request, 'accounts/profile.html', context)


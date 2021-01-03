from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm, GenderPlusAcceptForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
        'title': 'Страница регистрации',
        'form': form
        }
    )
@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        genderAndAccept = GenderPlusAcceptForm(request.POST, instance = request.user.profile)

        if profileForm.is_valid() and updateUserForm.is_valid() and genderAndAccept.is_valid():
            updateUserForm.save()
            profileForm.save()
            genderAndAccept.save()
            messages.success(request, 'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)
        genderAndAccept = GenderPlusAcceptForm(instance = request.user.profile)
    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
        'genderAndAccept': genderAndAccept,
    }

    return render(request, 'users/profile.html', data)

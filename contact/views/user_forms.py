from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('contact:login')

    context = {
        'site_title': 'Cadastro',
        'form': form
    }

    return render(
        request,
        'contact/register.html',
        context,
    )


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    context = {
        'form': form,
        'site_title': 'Atualizar dados.'
    }

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            context,
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            context,
        )

    form.save()

    return redirect('contact:user_update')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')

    context = {
        'site_title': 'Login',
        'form': form
    }

    return render(
        request,
        'contact/login.html',
        context,
    )


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

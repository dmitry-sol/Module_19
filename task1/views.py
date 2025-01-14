from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


buyers = Buyer.objects.all()
print(buyers)


def index(request):
    return render(request, 'index.html')

def catalog(request):
    games = Game.objects.all()
    return render(request, 'task1/catalog.html',
                  {'games': games})

def cart(request):
    return render(request,
                  'task1/cart.html')


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        age = request.POST.get("age")

        if Buyer.objects.filter(name=username).exists():
            info['error'] = f'Пользователь {username} уже существует'
        elif password != confirm_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 8:
            info['error'] = 'Вы должны быть старше 8'
        else:
            Buyer.objects.create(name=username)
            return render(request, 'task1/registration_success.html', {'username': username})
    return render(request, 'task1/registration_page.html', info)


def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST, existing_users=Buyer.objects.all())
        if form.is_valid():
            username = form.cleaned_data['username']
            Buyer.objects.create(name=username)
            return render(request, 'task1/registration_success.html', {'username': username})
    else:
        form = UserRegister(existing_users=Buyer.objects.all())
    return render(request, 'task1/registration_page.html', {'form': form})


def news(request):
    return render(request, 'task1/news.html')
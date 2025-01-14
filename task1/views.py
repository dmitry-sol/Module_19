from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import UserRegister
from .models import *


buyers = Buyer.objects.all()
print(buyers)


def index(request):
    return render(request, 'index.html')


def news(request):
    posts = News.objects.all().order_by('-id')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'task1/news.html', {'news': page_posts})


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



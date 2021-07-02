from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth import authenticate, login

from .forms import CustomUserCreationForm
from .models import User
from .serializers import UserSerializer
import datetime


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form, 'name': 'Регистрация'}
    return render(request, 'registration/register.html', context)


def dashboard(request):
    numdays = 20
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
    # print(date_list)
    date_joined = User.objects.all().values('date_joined__date').annotate(dcount=Count('date_joined__date')).order_by(
        '-date_joined__date')

    j = 0
    all_users_list = [User.objects.all().count()]
    date_joined_list = []
    for i in range(numdays):
        if str(date_joined[j]['date_joined__date']) == str(date_list[i].date()):
            all_users = int(all_users_list[i]) - int(date_joined[j]['dcount'])
            all_users_list.append(all_users)
            date_joined_list.append(date_joined[j]['dcount'])
            j += 1
        else:
            all_users_list.append(int(all_users_list[i]))
            date_joined_list.append(0)
    date_joined_list.reverse()
    all_users_list = all_users_list[:-1]
    all_users_list.reverse()

    user_roles = User.objects.all().values('user_role').annotate(usercount=Count('user_role')).order_by()

    context = {
        'date_joined_list': date_joined_list,
        'all_users_list': all_users_list,
        'user_roles': user_roles,
    }
    return render(request, 'cabinet/dashboard.html', context)


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SingleUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

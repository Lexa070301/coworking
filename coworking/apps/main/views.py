from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth import authenticate, login
from .models import User
from .serializers import UserSerializer

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('test1')

        if form.is_valid():
            print('test2')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SingleUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

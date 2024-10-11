from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import logout
from .models import Car, Comment
from .form import CarForm, CommentsForm

class CarView(View):
    '''Вывод записей машин'''
    def get(self, request):
        post_cars = {
            'Cars': Car.objects.all(),
        }
        return render(request, 'html/index.html', post_cars)

class CarDetail(View):
    '''Отдельная страница с машиной'''
    def get(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        comments = Comment.objects.filter(car=car)
        form = CommentsForm()
        context = {
            'Car': car,
            'form': form,
            'comments': comments,
        }
        return render(request, 'html/cars_detail.html', context)

    def post(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.author = request.user
            comment.save()
            return redirect('post_car', pk=car.id)
        else:
            comments = Comment.objects.filter(car=car)
            return render(request, 'html/cars_detail.html', {'Car': car, 'form': form, 'comments': comments})

class AddCar(View):
    '''Добавление нового автомобиля'''

    def get(self, request):
        form = CarForm()
        return render(request, 'html/add_car.html', {'form': form})

    def post(self, request):
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('home')
        return render(request, 'html/add_car.html', {'form': form})


class DeleteCar(View):
    '''Удаление автомобиля'''

    def post(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        if car.owner == request.user:
            car.delete()
        return redirect('home')


class EditCar(View):
    '''Редактирование существующего автомобиля'''

    def get(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        if car.owner == request.user:
            form = CarForm(instance=car)
            return render(request, 'html/edit_car.html', {'form': form, 'car': car})
        return redirect('home')

    def post(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        if car.owner == request.user:
            form = CarForm(request.POST, instance=car)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'html/edit_car.html', {'form': form, 'car': car})


class LogoutView(View):
    '''Выход пользователя из системы'''

    def get(self, request):
        logout(request)
        return redirect('home')


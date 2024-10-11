from django.urls import path
from .views import CarView, CarDetail, AddCar, DeleteCar, LogoutView, EditCar

urlpatterns = [
    path('', CarView.as_view(), name='home'),
    #Главная страница приложения. Отображает список автомобилей.
    path('car/<int:pk>/', CarDetail.as_view(), name='post_car'),
    #Страница детальной информации об автомобиле. Отображает информацию об автомобиле с указанным идентификатором (pk).
    path('add/', AddCar.as_view(), name='add_car'),
    #Страница добавления нового автомобиля.
    path('delete/<int:pk>/', DeleteCar.as_view(), name='delete_car'),
    #Страница удаления автомобиля с указанным идентификатором (pk).
    path('logout/', LogoutView.as_view(), name='logout'),
    #Страница выхода из системы.
    path('edit_car/<int:pk>/', EditCar.as_view(), name='edit_car'),
    #Страница редактирования автомобиля с указанным идентификатором (pk).
]


from django.contrib import admin
from django.urls import path, include

# Определение шаблонов URL для проекта
urlpatterns = [
    # Интерфейс администратора
    path('admin/', admin.site.urls),

    # Включение URL-шаблонов приложения 'listofcars'
    path('', include('listofcars.urls')),

    # Включение URL-шаблонов приложения 'users' с именем 'users'
    path('users/', include('users.urls'), name='users')
]
from rest_framework import serializers
# Подключаем модель user
from .models import User
 
#Создаём класс UserRegistrSerializer
class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    repeat_password = serializers.CharField()
    
    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = ['email', 'username', 'password', 'repeat_password']
 
    # Метод для сохранения нового пользователя
    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = User(
            email=self.validated_data['email'], # Назначаем Email
            username=self.validated_data['username'], # Назначаем Логин
        )
        
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Проверяем на валидность повторный пароль
        repeat_password = self.validated_data['repeat_password']
        # Проверяем совпадают ли пароли
        if password != repeat_password:
            # Если нет, то выводим ошибку
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        # Возвращаем нового пользователя 
        return user
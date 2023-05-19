from rest_framework import serializers
# Подключаем модель user
from .models import User,SomeData
 
#Создаём класс UserRegistrSerializer
class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    repeat_password = serializers.CharField()
    id = serializers.IntegerField()
    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = ['email', 'username', 'password', 'repeat_password',"id"]
 
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
        user.id = self.validated_data['id']
        user.is_active = True#False

        # Сохраняем пользователя
        user.save()
        # Возвращаем нового пользователя 
        return user
class SomeDataSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    
    
    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = SomeData
        # Назначаем поля которые будем использовать
        fields = ["id_someUser","someData"]
# class UserLoginSerializer(serializers.ModelSerializer):
#     # Поле для повторения пароля
#     repeat_password = serializers.CharField()
    
#     # Настройка полей
#     class Meta:
#         # Поля модели которые будем использовать
#         model = User
#         # Назначаем поля которые будем использовать
#         fields = ['email','password']
 
#     # Метод для сохранения нового пользователя
#     def is_auth(self, *args, **kwargs):
#         password = self.validated_data['password']
#         email = self.validated_data['email']
#         try:
#             user = User.objects.get(email = email)
#         except BaseException as e:
#             # raise ValidationError({"400": f'{str(e)}'})
#             pass

#         if all([not(password != i.password) for i in user]):
#             # Если нет, то выводим ошибку
#             raise serializers.ValidationError({password: "Неправильный логин или пароль"})
#         # Сохраняем пароль
        
        
        
#         # Возвращаем нового пользователя 
#         return user
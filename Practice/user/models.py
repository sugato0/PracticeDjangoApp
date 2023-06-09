from django.db import models # Подключаем работу с моделями
# Подключаем классы для создания пользователей
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
 
# Создаем класс менеджера пользователей
class MyUserManager(BaseUserManager):
    # Создаём метод для создания пользователя
    def _create_user(self, email, username, password, **extra_fields):
        # Проверяем есть ли Email
        if not email: 
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Email")
        # Проверяем есть ли логин
        if not username:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Логин")
        # Делаем пользователя
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем всё остальное
        user.save(using=self._db)
        # Возвращаем пользователя
        return user
    
    # Делаем метод для создание обычного пользователя
    def create_user(self, email, username, password):
        # Возвращаем нового созданного пользователя
        return self._create_user(email, username, password)
 
    # Делаем метод для создание админа сайта
    def create_superuser(self, email, username, password):
        # Возвращаем нового созданного админа
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)
# Создаём класс User
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True) # Идентификатор
    username = models.CharField(max_length=50, default="NoName") # Логин
    email = models.EmailField(max_length=100, unique=True) # Email

    is_active = models.BooleanField(default=True) # Статус активации

    is_staff = models.BooleanField(default=False) # Статус админа
    
    mobile = models.BigIntegerField(blank=True,default=89888880900)
    mobile_verified = models.BooleanField(default=False)
    site_id = models.ManyToManyField("Site", verbose_name=("id"))

    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email' # Идентификатор для обращения 
    REQUIRED_FIELDS = ['username'] # Список имён полей для Superuser
 
    objects = MyUserManager() # Добавляем методы класса MyUserManager
    
    # Метод для отображения в админ панели
    def __str__(self):
        return self.email

class Blocks(models.Model):
    id = models.AutoField(primary_key=True)
    css = models.JSONField(null=True,blank=True)
    html = models.JSONField(null=True,blank=True)
    js = models.JSONField(null=True,blank=True)
    item_id = models.ForeignKey("Items", verbose_name=("id"), on_delete=models.DO_NOTHING)
class Items(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    item = models.CharField(max_length=100,default=None)
class Updates(models.Model):
    update_time = models.TimeField(auto_now_add=True)
    blocks_id = models.ForeignKey("Blocks", verbose_name=("id"), on_delete=models.DO_NOTHING)
class Site(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    update_id = models.ForeignKey("Updates", verbose_name=("id"), on_delete=models.DO_NOTHING)

class User_profile(models.Model):
    User_profile_id = models.OneToOneField("User", verbose_name=("id"), on_delete=models.CASCADE)
    
    
class Settings(models.Model):
    User_profile_id = models.OneToOneField("User", verbose_name=("id"), on_delete=models.CASCADE)
    
    thema_id = models.ForeignKey("Themas",on_delete=models.DO_NOTHING)
    notifications = models.CharField(max_length=100)
    language_id = models.ForeignKey("Language",on_delete=models.DO_NOTHING)

class Language(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    language = models.CharField(max_length=100,default=None)

class Themas(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    thema = models.CharField(max_length=100,default=None)





class SomeData(models.Model):
    id_someUser = models.IntegerField()
    someData = models.CharField(max_length=255)
    def __str__(self):
        return self.email
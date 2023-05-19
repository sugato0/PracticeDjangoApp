
# Create your views here.
from rest_framework import status
# Подключаем компонент для ответа
from rest_framework.response import Response
# Подключаем компонент для создания данных
from rest_framework.generics import CreateAPIView
# Подключаем компонент для прав доступа
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
# Подключаем модель User
from .models import User,SomeData
# Подключаем UserRegistrSerializer
from .serializers import UserRegistrSerializer,SomeDataSerializer
 
 
# Создаём класс RegistrUserView
class RegistrUserView(CreateAPIView):
    # Добавляем в queryset
    queryset = User.objects.all()
    # Добавляем serializer UserRegistrSerializer
    serializer_class = UserRegistrSerializer
    # Добавляем права доступа
    permission_classes = [AllowAny]
    
    # Создаём метод для создания нового пользователя
    def post(self, request, *args, **kwargs):
        # Добавляем UserRegistrSerializer
        serializer = UserRegistrSerializer(data=request.data)
        # Создаём список data
        self.request.session["user_id"] = request.data["id"]
        data = {}
        # Проверка данных на валидность
        if serializer.is_valid():
            # Сохраняем нового пользователя
            serializer.save()
            # Добавляем в список значение ответа True
            data['response'] = True
            # Возвращаем что всё в порядке
            return Response(data, status=status.HTTP_200_OK)
        else: # Иначе
            # Присваиваем data ошибку
            data = serializer.errors
            # Возвращаем ошибку
            return Response(data)
class SomeDataView(CreateAPIView):
    # # Добавляем в queryset
    queryset = SomeData.objects.all()
    # Добавляем serializer UserRegistrSerializer
    serializer_class = SomeDataSerializer()
    # Добавляем права доступа
    permission_classes = [AllowAny]
    
    # Создаём метод для создания нового пользователя
    def post(self, request, *args, **kwargs):
        # Добавляем UserRegistrSerializer
        serializer = SomeDataSerializer(data=request.data)
        # Создаём список data
        data = {}
        # Проверка данных на валидность
        if serializer.is_valid():
            # Сохраняем нового пользователя
            
            SomeData.objects.create(
                id_someUser = request.data["id_someUser"],
                someData = request.data["someData"],
            )
            
            # Добавляем в список значение ответа True
            data['response'] = True
            # Возвращаем что всё в порядке
            return Response(data, status=status.HTTP_200_OK)
        else: # Иначе
            # Присваиваем data ошибку
            data = serializer.errors
            # Возвращаем ошибку
            return Response(data)

    def get(self,request):
        try:
            # dataes =  SomeData.objects.get(id_someUser=request.data["id"])
            queryset1 = SomeData.objects.filter(id_someUser=request.data["id"])
            serialize_data = SomeDataSerializer(
                instance=queryset1,
                many = True
            )
        except:
            serialize_data = "Данных не обнаружено"
        return Response(serialize_data.data, status=status.HTTP_200_OK)
        


# class login():
#     serializer_class = UserLoginSerializer
#     # Добавляем права доступа
#     permission_classes = [AllowAny]
#     def post(self, request, *args, **kwargs):
#         data = {}
#         serializer = UserLoginSerializer(data=request.data)
#         user = serializer.is_auth()
        
#         token = Token.objects.get_or_create(user=Account)[0].key
#         print(token)
#         if not check_password(password, Account.password):
#             raise ValidationError({"message": "Incorrect Login credentials"})

#         if Account:
#             if Account.is_active:
#                 print(request.user)
#                 login(request, Account)
#                 data["message"] = "user logged in"
#                 data["email_address"] = Account.email

#                 Res = {"data": data, "token": token}

#                 return Response(Res)

#             else:
#                 raise ValidationError({"400": f'Account not active'})

#         else:
#             raise ValidationError({"400": f'Account doesnt exist'})
from .serializers import BlogSerializers,AuthorSerializer, LoginSerializer
from .models import Author,Blog
from rest_framework.views import APIView
from rest_framework import generics
from .models import User
from rest_framework.generics import ( RetrieveAPIView, RetrieveUpdateDestroyAPIView,ListCreateAPIView,CreateAPIView )
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import  RegisterSerializer
from django.contrib.auth import authenticate,logout
from  rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Register API
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    fields= ['username','password']

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def post(self, request):
        data = request.data

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                refresh = RefreshToken.for_user(user)

                return Response ({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })

            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data='username or password incorrect', status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
   def post(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

class AuthorListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['=name']

class AuthorDeatilView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BlogListView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


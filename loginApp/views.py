from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from loginApp.models import User
# from User.serializers import UserSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def user_list(request):
   
#     if request.method == 'GET':
#         user = User.objects.all()
#         serializer = UserSerializer(user, many=True)
#         return JsonResponse(serializer.data, safe=False  )  

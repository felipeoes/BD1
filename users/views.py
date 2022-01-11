from django.shortcuts import get_object_or_404
from users.models import Usuario
# from .serializers import CustomRegisterSerializer, UserSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


# class UserProfileImageUpload(APIView):
#     # permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         print(request.data)
#         serializer = CustomRegisterSerializer(request, data=request.data)
#         if serializer.is_valid():
#             serializer.save(request.data)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, *args, **kwargs):
    #     avatar = request.data['file']
    #     user = request.user
    #     user.avatar = avatar
    #     user.save()
    #     return Response({"status": "ok"})

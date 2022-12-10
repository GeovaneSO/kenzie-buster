from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer
from users.models import User

class UserView(APIView):
    
    def post(self, req: Request) -> Response:
        user_req = req.data

        serializer = UserSerializer(data=user_req)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        user = User.objects.all()

        serializer = UserSerializer(user, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewDetails(APIView):
    ...

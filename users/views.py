from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthenticatedOnly
from .models import User
from django.shortcuts import get_object_or_404
import ipdb


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOnly]

    def get(self, request: Request, user_id: int) -> Response:
        user_obj_params = get_object_or_404(User, id=user_id)
        # ipdb.set_trace()
        
        self.check_object_permissions(request, user_obj_params)

        serializer = UserSerializer(user_obj_params)
        return Response(serializer.data, status.HTTP_200_OK)

        # if not request.user.is_employee:
        #     if request.user.id == user_obj_params.id:
        #         serializer = UserSerializer(user_obj_params)

        #         return Response(serializer.data, status.HTTP_200_OK)
        #     else:
        #         return Response({"detail": "You do not have permission to perform this action."}, status.HTTP_403_FORBIDDEN)
        
        # serializer = UserSerializer(user_obj_params)

        # return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user_obj_params = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user_obj_params)

        serializer = UserSerializer(user_obj_params, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
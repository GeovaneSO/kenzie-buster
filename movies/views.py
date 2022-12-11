from django.shortcuts import render
from django.shortcuts import get_object_or_404
from users.permissions import CustomPermission
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieOrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):

    authentication_classes = [JWTAuthentication]

    permission_classes = [CustomPermission]

    def post(self, req: Request) -> Response:

        movie_req = req.data

        serializer = MovieSerializer(data=movie_req)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:

        movies = Movie.objects.all()

        result_page = self.paginate_queryset(queryset=movies, request=req, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieDetailView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [CustomPermission]

    def get(self, req: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, pk=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, req: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, pk=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def post(self, req: Request, movie_id: int) -> Response:

        movie_obj = get_object_or_404(Movie, pk=movie_id)
        
        serializer = MovieOrderSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie_obj, user=req.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

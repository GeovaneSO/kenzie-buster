from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404

class MovieView(APIView):
    def post(self, req: Request) -> Response:
        return Response()
    
    def get(self, req: Request) -> Response:
        return Response()


class MovieDetailView(APIView):
    def get(self, req: Request, movie_id: int) -> Response:
        return Response()

    def delete(self, req: Request, movie_id: int) -> Response:
        return Response()


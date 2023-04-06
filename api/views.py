from .models import Todo
from .serializers import TodoSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class TodoView(APIView):
    def get(self, request: Request) -> Response:
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        data = {
            'result': serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request: Request, tr:str) -> Response:
        todos = Todo.objects.get(task=tr)
        todos.delete()
        return Response({"ruselt: Ok delete"})
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.Serializer):
    task = serializers.CharField(max_length=50)
    desciption = serializers.CharField(max_length=100)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        todo = Todo.objects.create(
            task=validated_data['task'],
            description=validated_data['description'],
            completed=validated_data['completed'],
        )
        return todo
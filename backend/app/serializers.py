from rest_framework import serializers
from app.models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        
class BookSearchSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=255)

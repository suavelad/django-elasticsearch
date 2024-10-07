from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.documents import BookDocument
from app.serializers import BookSearchSerializer,BookSerializer

from rest_framework import viewsets
from app.models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def search_books(request):
    serializer = BookSearchSerializer(data=request.GET)
    if serializer.is_valid():
        query = serializer.validated_data['query']
        search_results = BookDocument.search_books(query)
        # Serialize and return the results
        data = [{'title': book.title, 'author': book.author} for book in search_results]
        return Response(data)
    return Response(serializer.errors, status=400)

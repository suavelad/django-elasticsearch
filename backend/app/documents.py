from elasticsearch_dsl import Q
from elasticsearch_dsl.query import MultiMatch
from django_elasticsearch_dsl.documents import Document

from elasticsearch_dsl import Document, Date, Text
from django_elasticsearch_dsl import fields, Index
from app.models import Book
from django_elasticsearch_dsl.documents import Document


book_index = Index('books')

@book_index.doc_type
class BookDocument(Document):
    title = Text()
    author = Text()
    published_date = Date()

    class Django:
        model = Book

    def search_books(query):
        search_query = MultiMatch(query=query, fields=['title', 'author'])
        return BookDocument.search().query(search_query).to_queryset()

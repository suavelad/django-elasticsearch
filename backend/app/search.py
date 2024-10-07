from django_elasticsearch_dsl import Document, Index
from .models import MyModel

my_index = Index('my_index')

@my_index.doc_type
class MyModelDocument(Document):
    class Django:
        model = MyModel
        fields = ['title', 'description', 'created_at']

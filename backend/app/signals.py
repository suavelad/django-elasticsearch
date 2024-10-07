from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import Book
from app.documents import BookDocument

@receiver(post_save, sender=Book)
def update_book_in_elasticsearch(sender, instance, **kwargs):
    book = BookDocument.get(id=instance.id)
    if book:
        book.update(title=instance.title, author=instance.author, published_date=instance.published_date)
    else:
        BookDocument.index(instance)
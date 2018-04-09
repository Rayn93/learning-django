from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.



class Autor(models.Model):

    first_name = models.CharField(verbose_name=_("first name"), max_length=20)
    last_name = models.CharField(verbose_name=_("last name"),max_length=50)

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)


    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = _('author')
        verbose_name_plural = _('authors')




class Publisher(models.Model):

    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name



class BookCategory(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name



class Book(models.Model):

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Autor)
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.title



class BookEdiion(models.Model):
    """
    Wydanie określonej książki
    """
    publisher = models.ForeignKey(Publisher)
    book = models.ForeignKey(Book, related_name='editions')
    date = models.DateField()
    isbn = models.CharField(max_length=17)


    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book, publisher=self.publisher)


COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard'),
#wartość w bazie, wartość wyświetlana
)


class BookItem(models.Model):
    """
    Postrzegulna książka
    """

    edition = models.ForeignKey(BookEdiion)
    catalog_number = models.CharField(max_length=30)
    cover_type = models.CharField(choices=COVER_TYPES, max_length=4)

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition, cover=self.get_cover_type_display())
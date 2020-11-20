import graphene
from graphene_django import DjangoObjectType
from .models import Books


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")

class Query(graphene.ObjectType):

    all_books = graphene.List(BooksType)

    def resolve_all_books(root, info):
        return Books.objects.filter(title="django")

schema = graphene.Schema(query=Query)
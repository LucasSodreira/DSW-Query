from django.shortcuts import render
from django.db import models
from django.db.models.functions import Length
from .models import Book, Author, Tag, Review, Profile

def query_examples(request):
    # Consulta com relacionamento reverso (todos os livros de um autor)
    # A)
    books_of_author = Book.objects.filter(author__name='Sofia Vieira')

    # Consulta many-to-many (livros com uma determinada tag)
    # B)
    books_with_tag = Book.objects.filter(tags__name='História')

    # Consulta na Bio do autor
    # C)
    bio_author = Author.objects.filter(bio__icontains='Lorem')
    
    # Consultar Livro com avalição alta
    # D)
    book_rating = Review.objects.filter(rating__gte=4)

    # Consultar Perfil com website espefico
    # E)
    user_website = Profile.objects.filter(website='http://www.da.net/')
    
    # Consultar Livro sem avaliação
    # F)
    book_rating_null = Review.objects.filter(rating__isnull=True)

    
    # Consultar Autores com maior numero de livro
    # G)
    authors = Author.objects.annotate(num_books=models.Count('books')).order_by('-num_books')
    
    # H)
    books = Book.objects.annotate(summary_len=Length('summary')).filter(summary_len__gt=150)

    # I)
    reviews = Review.objects.filter(book__author__name='J.K. Rowling')

    # J)
    livros_com_tags = Book.objects.filter(tags__id__in=[1, 2, 3])

    # Envie todas as consultas para o template
    context = {
        'books_of_author': books_of_author,
        'books_with_tag': books_with_tag,
        'bio_author': bio_author,
        'book_ratinge': book_rating,
        'user_website': user_website,
        'book_rating_null': book_rating_null,
        'authors': authors,
        'books': books,
        'reviews': reviews,
        'livros_com_tags': livros_com_tags,
    }

    return render(request, 'core/teste1.html', context)

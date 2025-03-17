import pandas as pd
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def handle(self, *args, **kwargs):

        df = pd.read_csv('books_scraper/data.csv') 

        for index, row in df.iterrows():
            Book.objects.create(
                 title=row['title'],
                category=row['category'],
                description=row['description'],
                price=row['price'],
               
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))

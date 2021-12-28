from django.db import models

class Book(models.Model):

    title     = models.CharField(max_length = 200)
    author    = models.CharField(max_length = 100)
    editorial = models.CharField(max_length = 150)
    gender    = models.CharField(max_length = 100)
    num_pages = models.IntegerField(verbose_name = "number of pages")
    pub_date  = models.DateField()

    class Meta:
        ordering = ["author", "publication_date"]
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return f"{self.title}"

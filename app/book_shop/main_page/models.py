from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    book = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="posts/images/")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        null=True,
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Комментарий")
    name = models.CharField(max_length=100, verbose_name="Имя")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text


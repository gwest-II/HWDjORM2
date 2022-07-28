from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    tag_name = models.CharField(max_length=40, unique=True, verbose_name='Название')
    article = models.ManyToManyField('Article', through='ArticleScope')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.tag_name


class ArticleScope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной раздел', default=False)

    def __str__(self):
        return f'{self.is_main}'
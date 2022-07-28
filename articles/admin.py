from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Article, Scope, ArticleScope
from django.forms import BaseInlineFormSet

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleScope)
class ArticleScopeAdmin(admin.ModelAdmin):
    pass


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Не определены рубрики')
        count_main = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main') is True:
                count_main += 1

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if count_main > 1:
                raise ValidationError('Больше одной главной темы!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]
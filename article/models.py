from django.db import models
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    title = models.CharField(_('article'), max_length=50)
    author = models.CharField(_('author'), max_length=50)
    email = models.EmailField(_('email'), unique=True, blank=False, null=False, max_length=25)
    date = models.DateField(_('date'), auto_now_add=True)
    
    class Meta:
        ordering = ('pk',)
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        
    def __str__(self) -> str:
        return self.title

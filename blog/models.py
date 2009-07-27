from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.

class Artigo(models.Model):
    class Meta:
    	ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(default=datetime.now,blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    '''
    def get_absolute_url(self):
        return '/artigo/%d/'%self.id

    '''
    def get_absolute_url(self):
        return reverse(
        'blog.views.artigo',
        kwargs={'slug': self.slug}
        )
    

# SIGNALS

from django.db.models import signals
from django.template.defaultfilters import slugify
def artigo_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(artigo_pre_save, sender=Artigo)


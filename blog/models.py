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
    #slug = models.SlugField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
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
#def artigo_pre_save(signal, instance, sender, **kwargs):
#    instance.slug = slugify(instance.titulo)

def artigo_pre_save(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente. Ele verifica se
    ja existe um artigo com o mesmo slug e acrescenta um numero ao
    final para evitar duplicidade"""
    if not instance.slug:
        slug = slugify(instance.titulo)
        novo_slug = slug
        contador = 0
        while Artigo.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
		contador += 1
		novo_slug = '%s-%d'%(slug, contador)

	instance.slug = novo_slug

signals.pre_save.connect(artigo_pre_save, sender=Artigo)

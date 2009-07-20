from django.contrib.syndication.feeds import Feed
from models import Artigo

class UltimosArtigos(Feed):
    title = 'Ultimos artigos do blog do Alatazan'
    link = '/'
    def items(self):
             return Artigo.objects.all()
    '''
    Retirado daqui e acresecentado em urls.py '((r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),'
    def item_link(self, artigo):
             return '/artigo/%d/'%artigo.id
    '''

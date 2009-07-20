# Create your views here.

from django.shortcuts import render_to_response
from models import Artigo
from django.template import RequestContext

'''
def artigo(request, artigo_id):
    return render_to_response('blog/artigo.html')
'''

'''
def artigo(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    return render_to_response('blog/artigo.html', locals())
'''
 
def artigo(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    return render_to_response('blog/artigo.html', locals(), context_instance=RequestContext(request))


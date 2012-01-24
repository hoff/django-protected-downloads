from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    print RequestContext(request)
    print request.user
    return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))

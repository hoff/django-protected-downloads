from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.template import RequestContext
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

from django.views.defaults import page_not_found

#required to limit access to authenticated users
from django.contrib.auth.decorators import login_required

#required for serving private file
from django.core.servers.basehttp import FileWrapper

import mimetypes
import os
from playground import settings


def home(request):
    return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))
    
@user_passes_test(lambda u: u.is_superuser)
def console(request):
    users = User.objects.all().order_by('-last_login')
    return render_to_response('console.html', {'users':users}, context_instance=RequestContext(request))
    

@login_required
def serve_file(request, filename):
    '''
    see http://stackoverflow.com/questions/1609273/how-to-make-a-private-download-area-with-django
    '''
    fullname = settings.SECURE_MEDIA + filename
    try:
        f = file(fullname, "rb")
    except Exception, e:
        return page_not_found(request, template_name='404.html')
    try:
        wrapper = FileWrapper(f)
        response = HttpResponse(wrapper, mimetype=mimetypes.guess_type(filename)[0])
        response['Content-Length'] = os.path.getsize(fullname)
        response['Content-Disposition'] = 'inline; filename={0}'.format(filename)
        return response
    except Exception, e:
        return page_not_found(request, template_name='500.html')

        
@login_required
def download_file(request, filename):
    '''
    see http://stackoverflow.com/questions/1609273/how-to-make-a-private-download-area-with-django
    '''
    fullname = settings.SECURE_MEDIA + filename
    try:
        f = file(fullname, "rb")
    except Exception, e:
        return page_not_found(request, template_name='404.html')
    try:
        wrapper = FileWrapper(f)
        response = HttpResponse(wrapper, mimetype=mimetypes.guess_type(filename)[0])
        response['Content-Length'] = os.path.getsize(fullname)
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response
    except Exception, e:
        return page_not_found(request, template_name='500.html')
        
@login_required        
def view_file(request, filename):
    return render_to_response('view.html', {'filename':filename})
    

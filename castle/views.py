from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User




def home(request):
    return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))
    
@user_passes_test(lambda u: u.is_superuser)
def console(request):
    users = User.objects.all().order_by('-last_login')
    return render_to_response('console.html', {'users':users}, context_instance=RequestContext(request))

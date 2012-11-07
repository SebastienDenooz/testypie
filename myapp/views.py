# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template("myapp/index.html")
    context = Context({
        'name': "Testypie",
    })
    return HttpResponse(template.render(context))

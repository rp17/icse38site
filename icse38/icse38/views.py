from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from icse38.models import ContactForm
#from django import newforms as forms
#from django.newforms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.db import connection, transaction

def index(request):
    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    return render_to_response("index.html", {}, RequestContext(request))

def base(request):
    return render_to_response("base.html", {}, RequestContext(request))

def dates(request):
    return render_to_response("dates.html", {}, RequestContext(request))

def videoContest(request):
    return render_to_response("videoContest.html", {}, RequestContext(request))
	
def formack(request):
	name = request.POST['name']
	email = request.POST['email']
	affiliation = request.POST['affiliation']
	video = request.POST['video']
	acceptance = str(request.POST.get('termsAccepted', False))
	sql = "INSERT INTO registrations (name, email, affiliation, video, acceptance) values ('" + name + "', '" + email + "', '" + affiliation + "', '" + video + "', '" + acceptance + "')"
	cursor = connection.cursor()
	cursor.execute(sql)
	transaction.set_dirty()        
	transaction.commit()
	return render_to_response('formack.html', {'name': sql}, RequestContext(request))
	
def formsub(request):
    return render_to_response("formsub.html", {}, RequestContext(request))
	
def oc(request):
    return render_to_response("oc.html", {}, RequestContext(request))

def downloads(request):
    return render_to_response("downloads.html", {}, RequestContext(request))

def venue(request):
    return render_to_response("venue.html", {}, RequestContext(request))

def keynotes(request):
    return render_to_response("keynotes.html", {}, RequestContext(request))

def addbook(request):
    form = AuthorForm()
    book_formset = BookFormset(instance=Author())

    if request.POST:
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            book_formset = BookFormset(request.POST, instance=author)
            if book_formset.is_valid():
                book_formset.save()
            return redirect('/index/')

    return render_to_response('addbook.html',{
        'form': form, 'formset': book_formset
    },context_instance=RequestContext(request))
		
# def brochures(request):
#     return render_to_response("brochures.html", {}, RequestContext(request))

# def promo(request):
#     return render_to_response("promo.html", {}, RequestContext(request))

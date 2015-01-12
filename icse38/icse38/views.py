from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


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

# def brochures(request):
#     return render_to_response("brochures.html", {}, RequestContext(request))

# def promo(request):
#     return render_to_response("promo.html", {}, RequestContext(request))

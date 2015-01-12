from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'icse38.views.index', name='index'),
    # url(r'^icse38/', 'icse38.views.index'),

    url(r'^base$', 'icse38.views.base', name='base'),

    url(r'^dates$', 'icse38.views.dates', name='base'),
	
	url(r'^videoContest$', 'icse38.views.videoContest', name='base'),
	
	url(r'^formsub$', 'icse38.views.formsub', name='base'),

    url(r'^team/organizing-committee$', 'icse38.views.oc', name='oc'),

    url(r'^downloads$', 'icse38.views.downloads', name='downloads'),

    url(r'^venue$', 'icse38.views.venue', name='venue'),

    url(r'^keynotes$', 'icse38.views.keynotes', name='keynotes'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # url(r'^downloads/promo-banners$', 'icse38.views.promo', name='promo'),

    # url(r'^downloads/benefactors-brochures$', 'icse38.views.brochures', name='brochures'),

)


# https://github.com/django-debug-toolbar/django-debug-toolbar/issues/529
# resolve error on "NoReverseMatch at / u'djdt' is not a registered namespace"
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

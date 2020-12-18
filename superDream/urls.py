"""superFrog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


# The sslVerify is to verify my ssl certificate.
# My ssl server NameCheap says they want this file to render (BFABF40A0DA7138F42243A3C8C380CA4.txt)
# when they type this into the address bar:
# http://thehyperdream.com/.well-known/pki-validation/BFABF40A0DA7138F42243A3C8C380CA4.txt
# I put that txt file in the /home/timetable/superDream/myDream/templates/myDream and it worked.

# Also see here:
"""
The certificate file was sent to: dave@thehyperdream.com you can also download it via the
following link: https://ap.www.namecheap.com/domains/ssl/certificatedownload/3014108/DetailsPagee
Please keep in mind that once the certificate is issued, it is necessary to install it on your hosting server.
The guide on the certificate installation for most common server types can be found here:
https://www.namecheap.com/support/knowledgebase/article.aspx/795/69/how-to-install-ssl-certificates
To check if the certificate is installed correctly, you can use this tool: https://decoder.link/sslchecker
"""
from myDream import sslVerify

# I needed this file to get the index view working.
from myDream import views

"""
from django.contrib.sitemaps.views import sitemap
from myDream.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}
"""

urlpatterns = [
    #url(r'^paypal/', include('paypal.standard.ipn.urls')),

    #url(r'^sitemap/.xml$', sitemap, {'sitemaps': sitemaps},
    #name='django.contrib.sitemaps.views.sitemap'),

    url(r'^myDream/', include('myDream.urls'), name = 'myDream'),
    #url(r'^myDream/', include('myDream.urls')),

    url(r'^sales/', include('sales.urls')),
    url(r'^admin/', admin.site.urls),

    # This is to verify my ssl certificate.                                       file.function
    url(r'^.well-known/pki-validation/AD0AC50BCB5650CAA8781523EEA222DC.txt', sslVerify.sslVerify, name='sslVerify'),

    # CAUTION:  This url MUST BE LAST in this list.
    url('^$', views.IndexView.as_view(), name='index'),
]

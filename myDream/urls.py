from django.conf.urls import url

# The '.' means the directory we are in ie myFrog
from . import views  # The file
from davesHappyFamily import signPost, logOn, smallHandlers, builder



from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}




# Help with sitemaps:
# https://docs.djangoproject.com/en/1.10/ref/contrib/sitemaps/#django.contrib.sitemaps.Sitemap


# This tells django which app the urls belong to
# when using the url tag var in an html file, see templates/myPolls/index.html.
app_name = 'myDream'


# Now we are going to use some generic views since many of our handlers
# were similar.  See the end of lesson 4 at:
# https://docs.djangoproject.com/en/1.10/intro/tutorial04/
# The 'IndexView, DetailView and ResultsView are classes now in views.py
# django expects the P to pass too be called <pk> for a generic as_view().


"""
help with regexp:
https://docs.python.org/2/library/re.html

(?:...)
A non-capturing version of regular parentheses. Matches whatever regular expression is
inside the parentheses, but the substring matched by the group cannot be retrieved
after performing a match or referenced later in the pattern.

(...)
Matches whatever regular expression is inside the parentheses, and indicates the start
and end of a group; the contents of a group can be retrieved after a match has been
performed, and can be matched later in the string with the \number special sequence,
described below. To match the literals '(' or ')', use \( or \), or enclose them inside a character class: [(] [)].
"""

"""
^	Match start of string	^Dear
eg r'^Dear' will match any string starting with the word Dear.
r'[^Dear]' will match anything but the word Dear.

$
Basically Davee the string before the $ must match.
eg  r'money$' will match any string ending in the word money.

Matches the end of the string or just before the newline at the
end of the string, and in MULTILINE mode also matches before a
newline. foo matches both 'foo' and 'foobar', while the regular
expression foo$ matches only 'foo'. More interestingly, searching
for foo.$ in 'foo1\nfoo2\n' matches 'foo2' normally, but 'foo1'
in MULTILINE mode; searching for a single $ in 'foo\n' will find
two (empty) matches: one just before the newline, and one at the
end of the string.

(?P<name>...)
Similar to regular parentheses, but the substring matched by the group is accessible
via the symbolic group name name. Group names must be valid Python identifiers, and
each group name must be defined only once within a regular expression. A symbolic
group is also a numbered group, just as if the group were not named.
And it goes on and on in the docs...

url(r'^blog/(?P<slug>[\w-]+)/$', 'myapp.views.blog_detail', name='blog_detail'),
"""

PAGE_RE = r'(?P<pk>[a-zA-Z0-9\_-]+)*/*'

urlpatterns = [

    # Just using this for testing stuff.
    # File views.py, class TestView in that file, imported above.
    url('test/',views.TestView.as_view(), name='test'),
    # or you can do this
    #url(r'^test/$',views.TestView.as_view(), name='test'),


    url('logOn/', logOn.logOn, name='logOn'),
    url('logOut/', smallHandlers.logOut, name='logOut'),

    # forgot name or password, this now handles both.
    url('forgot/', smallHandlers.forgot, name='forgot'),

    # The file 'signPost.py' must be in the same directory as this url mapper.
    # Works with forms.py, class UserInfoForm
    #        File signPost.py signPost() in that file.  file imported above.
    url('signPost/', signPost.signPost, name='signPost'),

    # Build your own web page in less that 5 seconds.
    url('fiveSeconds/', smallHandlers.FiveSeconds.as_view(), name='fiveSeconds'),

    url('message/', views.Message.as_view(), name='message'),

    url('yourProfile/', views.YourProfile.as_view(), name='yourProfile'),
    url('changePassword/', smallHandlers.changePassword, name='changePassword'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),

    url('books/', smallHandlers.books, name='books'),



# This has been temporarily pointed at my webflow art page.  Dec 29/18
    url('artForSale/', smallHandlers.artForSale, name = 'artForSale'),
# I use this one for updating in the background
    url('artForSale2/', smallHandlers.artForSale2, name = 'artForSale2'),

    url('paymentReceived/', smallHandlers.paymentReceived, name='paymentReceived'),

    url(r'^contact/$', smallHandlers.contact, name='contact'),


# This is a list of my dvd/s etc that I have for sale.  Available for download.
    url(r'^davesList/$', smallHandlers.davesList, name='davesList'),


    url(r'^guitarVideos/$', smallHandlers.guitarVideos, name='guitarVideos'),

    url(r'^baby/$', smallHandlers.baby, name='baby'),



    url(r'^sendExcel/$', smallHandlers.sendExcel, name = 'sendExcel'),

    url(r'^sendTrades/$', smallHandlers.sendTrades, name = 'sendTrades'),

    url(r'^sendTrades2/$', smallHandlers.sendTrades2, name = 'sendTrades2'),

    url(r'^stockMarketPortfolio/$', smallHandlers.stockMarketPortfolio, name='stockMarketPortfolio'),


    url(r'^sendStockMarketBook/$', smallHandlers.sendStockMarketBook, name='sendStockMarketBook'),


    url(r'^survives/$', smallHandlers.survives, name='survives'),

    url(r'^vehicle/$', smallHandlers.vehicle, name='vehicle'),

    url(r'^cats/$', smallHandlers.cats, name='cats'),

    url(r'^gout/$', smallHandlers.gout, name='gout'),

    url(r'^horse/$', smallHandlers.horse, name='horse'),

    url(r'^dunk/$', smallHandlers.dunk, name='dunk'),

    url(r'^money/$', smallHandlers.money, name='money'),

    url(r'^phone/$', smallHandlers.phone, name='phone'),


# builder
# This is where I build my clients web sites.  NOT HAPPENING SCRAP THIS ONE.
# I'm building my clients web sites at webFlow.com  They will use webFlows servers.
    #url(r'^builder/$', builder.davesBuilder, name='davesBuilder'),



# I am now using this mapper to redirect to my webflow page, as I won't
# be using this for mobirise (bootstrap) anymore.  Scraping mobirise.
# So FOR MY GOOGLE AD the client clicks on theHyperDream.com/myDream/websitebuilder
# and this redirects them to https://david-potschkas-five-star-project.webflow.io/

   url(r'^webSiteBuilder/$', builder.webSiteBuilder, name='webSiteBuilder'),





###################### End daveBuilder


    # This one must be last.  It is now in superDream/url.py
    #   file views.py, class IndexView
    #url(PAGE_RE, views.IndexView.as_view(), name='index')

]

"""
url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
"""




"""
Note that the name of the matched pattern in the regexes of the second
and third patterns has changed from <question_id> to <pk> above.
Anything inside <hello I'm inside> is passed to the handler.

The old way.
urlpatterns = [
    # ex: /myPolls/
    url(r'^$', views.index, name='index'),

    # ex: /myPolls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /myPolls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /myPolls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

"""
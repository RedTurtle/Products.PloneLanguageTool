## Script (Python) "switchLanguage"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lang,here_url=None,layer_url=None,available_languages=None,cookie=0
##title=

from Products.CMFCore.utils import getToolByName
REQUEST=context.REQUEST
if not here_url: here_url=context.absolute_url()
try:
    if not layer_url: layer_url=context.retrieveI18NContentLayerURL()
except AttributeError:
    layer_url = None

languageTool = getToolByName(context,'portal_languages')
portal_url = getToolByName(context, 'portal_url')()

if not available_languages: available_languages=languageTool.getSupportedLanguages()
if lang:
    #if lang in available_languages:
    #    context.REQUEST.RESPONSE.setCookie('I18N_CONTENT_LANGUAGE',lang,path='/')
    languageTool.setLanguageCookie(lang, REQUEST=REQUEST,noredir=1)




redirect=layer_url
try: referrer=REQUEST.environ['HTTP_REFERER']
except: referrer=hereurl

##print "lang", lang
##print "layer_url", layer_url
##print "referrer", referrer[:len(layer_url)]

if layer_url is None:
    return REQUEST.RESPONSE.redirect(referrer)

if referrer[:len(layer_url)] == layer_url:
    try: rest=referrer[len(layer_url):]
    except: rest=None
    print "r1", rest
    if rest and rest not in ('/','/index_html','/view'):
        rest=rest.split('/')
        print "rest", rest
        print "langs", available_languages
        if len(rest) > 1:
            rs = rest[1].split('?')
            if len(rs) > 1: q=rs[1]
            else: q=None
            r=rs[0]
            print "r, q", r,q
            if r in available_languages and lang in available_languages:
                if hasattr(context, lang):
                    if context.portal_membership.checkPermission('View', getattr(context, lang)):
                        r=lang
                    else:
                        r=None
                else:
                    r=None
            elif r == 'i18nlayer_languages_form':
                r=None
            else:
                #rest=[]
                r=None
            if not r:
                if q: rest.insert(2,'?'.join(('view',q)))
                else: rest.insert(2,'view')
                rest=rest[:3]
            if q and r and len(rest)>1: rest[1]='?'.join((r, q))
            elif r and len(rest)>1: rest[1]=r
            elif not r and len(rest)>1: del rest[1]
        redirect=layer_url+'/'.join(rest)
query={}
# parse current query
s = redirect.find('?')
if s >= 0:
    q = redirect[s+1:]
    redirect=redirect[:s]
    for e in q.split("&"):
        if e:
            k,v = e.split("=")
            query[k]=v
print "query", query
if lang:
    # no cookie support
    query['cl']=lang
qst="?"
for k, v in query.items():
    qst=qst+"%s=%s&" % (k, v)
redirect=redirect #+qst[:-1]
print "redirect", redirect
REQUEST.RESPONSE.redirect(redirect)


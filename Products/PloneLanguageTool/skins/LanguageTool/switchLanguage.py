## Script (Python) "switchLanguage"
##title=
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=set_language=None
REQUEST=context.REQUEST

if set_language: lang=set_language

here_url=context.absolute_url()
try: 
    layer_url=context.retrieveI18NContentLayerURL()
    available_languages=context.retrieveFilteredLanguages().keys()
except: 
    layer_url=here_url
    available_languages=()

redirect=layer_url

try: referrer=REQUEST.environ['HTTP_REFERER']
except: referrer=here_url

print "layer_url", layer_url
print "referrer", referrer

if referrer[:len(layer_url)] == layer_url:
    try: rest=referrer[len(layer_url):]
    except: rest=None
    print "r1", rest
    if rest and rest != '/' and rest != '/index_html':
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
		if context.portal_membership.checkPermission('View', getattr(context, lang)):
		    print "permission on", lang
                    r=lang
		else:
		    print "no permission on", lang
		    r=None
	    elif r == 'i18nlayer_languages_form':
	        r=None
	    #else: rest=[]
            if q and r and len(rest)>1: rest[1]='?'.join((r, q))
	    elif r and len(rest)>1: rest[1]=r
	    elif not r and len(rest) >1: del rest[1]
	    print "rest", rest, q, r
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

if set_language:
    query['set_language']=lang

qst="?"
for k, v in query.items():
    qst=qst+"%s=%s&" % (k, v)

redirect=redirect+qst[:-1]
print "redirect", redirect
#return printed
REQUEST.RESPONSE.redirect(redirect)


# Create your views here.
from django.http import HttpResponse
import re, io, urllib2

src_re = r'src="'
hyperlinks = r'<a.*?>([\s\S]*?)</a>'
patterns = [
        r'<table id="toc"[\s\S]*?</table>',
        r'<!-- header -->[\S\s]*<!-- /header -->',
        r'<!-- panel -->[\S\s]*<!-- /panel -->',
        r'<!-- footer -->[\S\s]*<!-- /footer -->',
        ]
image_source = r'([\S\s]*?src=")([\S\s]*?)("[\S\s]*)'

def load_html(url):
    headers = {'User-Agent' : 'Mozilla/5.0'}
    req = urllib2.Request(url, None, headers)
    return urllib2.urlopen(req).read()

def parse(url):
    html = load_html(url)
    html = html.replace('href="/', 'href="http://') # links to styles, images etc.
    for pattern in patterns:
        html = re.sub(pattern, '', html) # get rid of dirty stuff
    res = ''
    prev = 0
    img_num = 1
    for match in re.finditer(hyperlinks, html):
        if not re.search(r'[\S\s]*?<img[\s\S][\S\s]*?>', match.group(1)): # if link doesn't contain image inside
        #if match.group(1).find('<img') < 0:
            res += html[prev:match.start()] + match.group(1)
        else:
            # TODO: substitue name
            match_src = re.search(image_source, match.group(0))
            res += html[prev:match.start()] + re.sub(r'alt=".*"', 'alt="obrazek'\
                   + str(img_num) + '"', match_src.group(1)) + 'obrazek'\
                   + str(img_num) + '.png' + match_src.group(3)
            img_num += 1
        prev = match.end()
    return res

def sciagnij_opis(request, title):
    return HttpResponse(parse('http://en.wikipedia.org/wiki/' + title))

def sciagnij_obrazek(request, nazwa, numer):
    u = urlopen('http://www.mimuw.edu.pl/studia/informacje/zamawiane/zamawiane-pilotaz/kapital_ludzki.png')
    r = u.read();
    return HttpResponse(r)

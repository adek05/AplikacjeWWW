import re, io, urllib2

src_re = r'src="'
hyperlinks = r'<a.*?>([\s\S]*?)</a>'
contents = r'<table id="toc"[\s\S]*?</table>'
header = r'<!-- header -->[\S\s]*?<!-- /header -->'
panel = r'<!-- panel -->[\S\s]*?<!-- /panel -->'
footer = r'<!-- footer -->[\S\s]*?<!-- /footer -->'
image_source = r'([\S\s]*?src=")([\S\s]*?)("[\S\s]*)'

def load_html(url):
    headers = {'User-Agent' : 'Mozilla/5.0'}
    req = urllib2.Request(url, None, headers)
    return urllib2.urlopen(req).read()

def parse(url):
    html = load_html(url)
    html = html.replace('href="/', 'href="http:') # links to styles, images etc.
    html = re.sub(header, '', html) # fuck off header
    html = re.sub(panel, '', html) # fuck off panel
    html = re.sub(footer, '', html) # fuck off panel
    html = re.sub(contents, '', html) # fuck off contents
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
            print match.group(0)
            print match_src.group(1) + 'obrazek' + str(img_num) + '.png' + match_src.group(3)
            res += html[prev:match.start()] + match_src.group(1) + 'obrazek' + str(img_num) + '.png' + match_src.group(3)
            img_num += 1
        prev = match.end()
            
    file = open(url[url.rfind('/') + 1:] + '.html', 'w')
    file.write(res)
    file.close()

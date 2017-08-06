#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, locale, bs4, unicodedata, re
from bs4 import BeautifulSoup
ch_file = sys.argv[1]
raw_html = open(ch_file).read().decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#raw_html = "".join(line.strip() for line in raw_html.split("\n"))
html = BeautifulSoup(raw_html, "lxml")

#html = BeautifulSoup(open(sys.argv[1]).read().decode(sys.stdin.encoding or locale.getpreferredencoding(True)), "lxml")
# html es <class 'bs4.BeautifulSoup'>

# <div class="storytext xcontrast_txt nocopy" id="storytext">
chapter = html.find("div",attrs={"id":"storytext"})
cnum = chapter.find_all("strong")[0]
ctitle = chapter.find_all("strong")[1]
title = cnum.text + ": " + ctitle.text
title = title.replace("Chapter 0","Chapter ")
title = title.replace("Chapter 0","Chapter ")

print '<h2>'+title+'</h2>\n'
cnum.parent.extract()
ctitle.parent.extract()

print chapter.encode_contents().replace("</p><p>","</p>\n<p>")+'\n\n\n'



"""
title = html.find("h2",attrs={"class":"entry-title"})
title.find("a").unwrap()


for i in chapter.find_all("script"):
	i.extract()


for i in chapter.find_all("div",attrs={"class":"wpcnt"}):
	i.extract()

for i in chapter.find_all("div",attrs={"class":re.compile(r"sharedaddy.*")}):
	i.extract()


" ""
for i in chapter.find_all("span",attrs={"style":"font-family: Arial, sans-serif;"}):
	i.unwrap()

for i in chapter.find_all("span",attrs={"style":"font-size: medium;"}):
	i.unwrap()



for i in chapter.find_all("a",text=re.compile(r".*(Next|Previous) Chapter.*")):
	i.parent.extract()


print "\n" * 5

"""


#print "<h1>" + title.encode_contents() + "</h1>" + "\n"
#print chapter.encode_contents()
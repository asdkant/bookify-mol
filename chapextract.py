#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, locale, bs4, unicodedata, re
from bs4 import BeautifulSoup
ch_file = sys.argv[1]
raw_html = open(ch_file).read().decode(sys.stdin.encoding or locale.getpreferredencoding(True))

html = BeautifulSoup(raw_html, "lxml")

chapter = html.find("div",attrs={"id":"storytext"})
cnum = chapter.find_all("strong")[0]
ctitle = chapter.find_all("strong")[1]
title = (cnum.text + ": " + ctitle.text).replace("Chapter 0","Chapter ").replace("Chapter 0","Chapter ")

print '<h2>'+title+'</h2>\n'
cnum.parent.extract()
ctitle.parent.extract()

print chapter.encode_contents().replace("</p><p>","</p>\n<p>")+'\n\n\n'

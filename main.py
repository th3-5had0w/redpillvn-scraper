import weasyprint
import requests
from bs4 import BeautifulSoup as bs
import re


'''
pdf = weasyprint.HTML('https://redpillvn.com/tui-dan-ba-chi-co-thich-tien').write_pdf()

open('bruh.pdf', 'wb').write(pdf)
'''

document = requests.get('https://redpillvn.com/kho-luu-tru-bai-viet-redpillvn/')
#document = requests.get('https://redpillvn.com/category/stoicism/')

death = open('blacklist.txt', 'a')


for link in bs(document.text, 'html.parser').find_all('a'):
    if (link.get('href') != None):
        if ('forum.redpillvn.com' not in link.get('href')):
            blacklist = open('blacklist.txt', 'r').readlines()
            checklink = link.get('href')+'\n'
            if checklink not in blacklist:
                #pdf = weasyprint.HTML(link.get('href')).write_pdf()
                #open(link.title, 'wb').write(pdf)
                title = link.text
                if '#' in title:
                    title = re.sub('[#]', '', title)
                if '/' in title:
                    title = re.sub('[/]', '', title)
                path = 'pdfs/'+title
                pdf = weasyprint.HTML(link.get('href')).write_pdf()
                open(path, 'wb').write(pdf)
                death.write(checklink)
    print('Done! -', link.get('href'))

print(blacklist)

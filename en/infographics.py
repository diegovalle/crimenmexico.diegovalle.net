import glob
from datetime import datetime
import fileinput
from subprocess import call
import os
import re

os.system(r"find images/infographics/fulls -name '*.png' -exec sh -c 'convert {} -resize 30% images/infographics/thumbnails/$(basename "+ r'"{}"' + r")' \;")
os.system(r"find . -name '*.png' -exec sh -c 'optipng {}' \;")

#find './images/infographics/fulls' -name '*.png' -exec sh -c 'convert {} -resize 30% images/infographics/thumbnails/$(basename "{}")' \;

files_mun = glob.glob("images/infographics/thumbnails/mun*.png")
files_mun = sorted(files_mun, key = lambda x: str(datetime.strptime(x, 'images/infographics/thumbnails/municipios_%b_%Y.png')))
files_mun.reverse()

files_inf = glob.glob("images/infographics/thumbnails/inf*.png")
files_inf = sorted(files_inf, key = lambda x: str(datetime.strptime(x, 'images/infographics/thumbnails/infographic_%b_%Y.png')))
files_inf.reverse()

dates = map(lambda x: datetime.strptime(x, 'images/infographics/thumbnails/infographic_%b_%Y.png').strftime('%B %Y'), files_inf)


s = ''
for i in range(0, len(files_mun)):
  s += '''<p>{0}</p><div class="row">

									<div class="6u 12u(mobile)"><a href="{1}" class=" fit"><img class="lazy" data-original="{2}" alt=""></a></div>
									<div class="6u 12u(mobile)"><a href="{3}" class=" fit"><img src="{4}" alt=""></a></div>
								</div> '''.format(dates[i], files_inf[i].replace('thumbnails','fulls'), files_inf[i], files_mun[i].replace('thumbnails','fulls'), files_mun[i])

#locale.setlocale(locale.LC_ALL, "pt_PT")

f = open('infographics.template','r')
filedata = f.read()
f.close()


newdata = filedata.replace("{{INFOGRAPHICS}}", s)

f = open('infographics.html','w')
f.write(newdata)
f.close()



f = open('index.html','r')
filedata = f.read()
f.close()

newdata = re.sub(r"images/infographics/fulls/infographic_[a-z]+_[0-9]+.png", 
                 files_inf[0].replace('thumbnails','fulls'), filedata)
newdata = re.sub(r"images/infographics/thumbnails/infographic_[a-z]+_[0-9]+.png", 
                  files_inf[0], newdata)
newdata = re.sub(r"images/infographics/fulls/municipios_[a-z]+_[0-9]+.png", 
                  files_mun[0].replace('thumbnails','fulls'), newdata)
newdata = re.sub(r"images/infographics/thumbnails/municipios_[a-z]+_[0-9]+.png", 
                   files_mun[0], newdata)
#newdata = filedata.replace("{{INFOGRAPHICS}}", s)

f = open('index.html','w')
f.write(newdata)
f.close()

find en -type f -print0 | xargs -0 sed -i 's/infographic_may_2015\.png/infographic_jun_2015\.png/g'
find en -type f -print0 | xargs -0 sed -i 's/municipios_may_2015\.png/municipios_jun_2015\.png/g'

find es -type f -print0 | xargs -0 sed -i 's/infographic_es_may_2015\.png/infographic_es_jun_2015\.png/g'
find es -type f -print0 | xargs -0 sed -i 's/municipios_es_may_2015\.png/municipios_es_jun_2015.png/g'

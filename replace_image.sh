find en -type f -print0 | xargs -0 sed -i 's/infographic_feb_2015\.png/infographic_mar_2015\.png/g'
find en -type f -print0 | xargs -0 sed -i 's/municipios_feb_2015\.png/municipios_mar_2015\.png/g'

find es -type f -print0 | xargs -0 sed -i 's/infographic_es_feb_2015\.png/infographic_es_mar_2015\.png/g'
find es -type f -print0 | xargs -0 sed -i 's/municipios_es_feb_2015\.png/municipios_es_mar_2015.png/g'

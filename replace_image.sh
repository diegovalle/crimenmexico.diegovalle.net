find en -type f -print0 | xargs -0 sed -i 's/infographic_mar_2015\.png/infographic_apr_2015\.png/g'
find en -type f -print0 | xargs -0 sed -i 's/municipios_mar_2015\.png/municipios_apr_2015\.png/g'

find es -type f -print0 | xargs -0 sed -i 's/infographic_es_mar_2015\.png/infographic_es_abr_2015\.png/g'
find es -type f -print0 | xargs -0 sed -i 's/municipios_es_mar_2015\.png/municipios_es_abr_2015.png/g'

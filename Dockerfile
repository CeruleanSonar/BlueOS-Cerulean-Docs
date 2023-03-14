from python:3.9-slim-bullseye

COPY static /static

LABEL version "1.1.0"
LABEL permissions '\
    {\
    "NetworkMode": "host"\
    }'
LABEL authors '[\
    {\
    "name": "Nick Nothom",\
    "email": "nick.nothom@ceruleansonar.com"\
    }\
    ]'
LABEL docs ''
LABEL company '{\
    "about": "",\
    "name": "Cerulean Sonar",\
    "email": "dennys.bisogno@ceruleansonar.com"\
    }'
LABEL readme 'https://raw.githubusercontent.com/CeruleanSonar/BlueOS-Cerulean-Docs/master/Readme.md'
LABEL website 'https://ceruleansonar.com'
LABEL support 'https://forum.ceruleansonar.com/categories'
LABEL requirements "core >  1"

ENTRYPOINT cd /static && ./server.py
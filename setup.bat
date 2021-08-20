@echo off

timeout /t 1
echo 'prapre for install dependcencies'

cls
echo 1...
timeout /t 1 /nobreak > NUL
echo 2...
timeout /t 1 /nobreak > NUL
echo 3...
timeout /t 1 /nobreak > NUL

pip install colorama 
pip install imdb
pip install pip install IMDbPY
pip install git+https://github.com/alberanid/imdbpy
pip install imdbpy 


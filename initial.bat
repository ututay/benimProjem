del db.sqlite3
py manage.py makemigrations rango
py manage.py migrate
py dmoz_vtDoldur.py https://www.dmoz.org/World/T%%C3%%BCrk%%C3%%A7e/Bas%%C4%%B1n_ve_Yay%%C4%%B1n/Haberler/
py dmoz_vtDoldur.py https://www.dmoz.org/World/T%%C3%%BCrk%%C3%%A7e/Bas%%C4%%B1n_ve_Yay%%C4%%B1n/Gazeteler/
py dmoz_vtDoldur.py https://www.dmoz.org/World/T%%C3%%BCrk%%C3%%A7e/Al%%C4%%B1%%C5%%9Fveri%%C5%%9F/Al%%C4%%B1%%C5%%9Fveri%%C5%%9F_Rehberleri/
py dmoz_vtDoldur.py https://www.dmoz.org/World/T%%C3%%BCrk%%C3%%A7e/Al%%C4%%B1%%C5%%9Fveri%%C5%%9F/Oyuncaklar_ve_Oyunlar/
py dmoz_vtDoldur.py https://www.dmoz.org/World/T%%C3%%BCrk%%C3%%A7e/Bilgisayar/Programlama/
py dmoz_vtDoldur.py https://www.dmoz.org/World/T%%C3%%BCrk%%C3%%A7e/Bilim/Astronomi/
::py manage.py createsuperuser
start chrome 127.0.0.1
py manage.py runserver 127.0.0.1:80
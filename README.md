# Compfest Backend

### Django Rest Framework (Python)
Cara run backend
1. Buka terminal pada directory
2. Ketik ```venv\Scripts\activate```
3. Run dengan command ```python manage.py runserver```
4. Lalu Anda buka di browser **http://127.0.0.1:8000/**
5. Sesuaikan link yang ada karena ini hanya API backend untuk frontend

Note : 
1. Harus sudah menginstall Django dan Python
2. Terkadang command laptop lain ada yang berbeda seperti ```python3 manage.py runserver```, dan ada command yang lain
3. Pada saat run local bisa terjadi error karena belum menginstall dependency yang saya pakai, seperti djangorestframework, psycopg2-binary, django-cors-headers (seinget saya hanya pakai 3 ini)
```
pip install djangorestframework
pip install psycopg2-binary
pip install django-cors-headers
```
4. Lebih baik buka disini, sudah saya deploy dengan link **https://compfest-be.vercel.app**

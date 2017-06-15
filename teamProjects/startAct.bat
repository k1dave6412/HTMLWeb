@ECHO OFF
CALL "E:\onedrive\teamProjects\env\Scripts\activate.bat"
cd/d "E:\onedrive\teamProjects\backend"
CALL python manage.py runserver
CMD.EXE 

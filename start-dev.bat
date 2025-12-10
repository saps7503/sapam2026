@echo off
echo Iniciando entorno de desarrollo...
cd /d c:\sistemas\aplicacionespy
docker-compose up -d
echo.
echo Servicios iniciados:
docker-compose ps
echo.
echo URLs:
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo MySQL: localhost:3306
pause
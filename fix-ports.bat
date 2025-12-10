@echo off
echo ============================================
echo  SOLUCIONADOR DEFINITIVO DE PUERTOS
echo ============================================
echo.

echo [1/4] Deteniendo todo...
docker-compose down

echo.
echo [2/4] Modificando docker-compose.yml para usar puerto 3307...
powershell -Command "(Get-Content docker-compose.yml) -replace '3306:3306', '3307:3306' | Set-Content docker-compose.yml"
powershell -Command "(Get-Content docker-compose.yml) -replace '\"3306\"', '\"3307\"' | Set-Content docker-compose.yml"

echo.
echo [3/4] Actualizando archivo .env...
if exist .env (
    powershell -Command "(Get-Content .env) -replace 'MYSQL_PORT=3306', 'MYSQL_PORT=3307' | Set-Content .env"
    powershell -Command "(Get-Content .env) -replace 'MYSQL_HOST=db', 'MYSQL_HOST=localhost' | Set-Content .env"
)

echo.
echo [4/4] Iniciando servicios...
docker-compose up -d
timeout /t 5 /nobreak > nul
docker-compose ps

echo.
echo ============================================
echo           ✅ CONFIGURACIÓN ACTUALIZADA
echo ============================================
echo Backend Django:    http://localhost:8000
echo Admin Django:      http://localhost:8000/admin
echo Frontend:          http://localhost:5173  (Vite/React)
echo MySQL:             localhost:3307 (root/sin pass)
echo ============================================
echo.
echo NOTA: El frontend usa puerto 5173 (Vite)
echo.
pause
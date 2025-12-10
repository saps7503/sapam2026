@echo off
echo ============================================
echo  SOLUCIÓN DEFINITIVA MySQL 8.0
echo ============================================
echo.

echo [1/5] Deteniendo todo...
docker-compose down -v

echo.
echo [2/5] Creando .env CORRECTO para MySQL 8.0...
(
echo # Django
echo DJANGO_SECRET_KEY=changeme
echo DJANGO_DEBUG=True
echo.
echo # MySQL - Configuración CORRECTA para MySQL 8.0
echo # NO uses MYSQL_USER=root con MYSQL_ALLOW_EMPTY_PASSWORD
echo MYSQL_DATABASE=bd_sapam
echo MYSQL_HOST=db
echo MYSQL_PORT=3306
REM ¡IMPORTANTE! No definir MYSQL_USER para root
) > .env

echo.
echo [3/5] Creando docker-compose.yml optimizado...
(
echo services:
echo   db:
echo     image: mysql:8.0
echo     container_name: appagua_db
echo     command: --default-authentication-plugin=mysql_native_password --skip-log-bin
echo     environment:
echo       MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
echo       MYSQL_DATABASE: bd_sapam
echo       # ¡NO definir MYSQL_ROOT_PASSWORD cuando usas MYSQL_ALLOW_EMPTY_PASSWORD!
echo     volumes:
echo       - mysql_data:/var/lib/mysql
echo     ports:
echo       - "3307:3306"
echo     healthcheck:
echo       test: ["CMD", "mysqladmin", "ping"]
echo       interval: 5s
echo       timeout: 5s
echo       retries: 30
echo.
echo   web:
echo     build: ./backend
echo     container_name: appagua_web
echo     env_file:
echo       - .env
echo     environment:
echo       # Django usará estas credenciales para root
echo       MYSQL_USER: root
echo       MYSQL_PASSWORD: ""
echo     depends_on:
echo       db:
echo         condition: service_healthy
echo     volumes:
echo       - ./backend:/app
echo     ports:
echo       - "8000:8000"
echo     command: sh -c "sleep 10 && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
echo.
echo volumes:
echo   mysql_data:
) > docker-compose.yml

echo.
echo [4/5] Iniciando MySQL primero...
docker-compose up -d db
echo Esperando 30 segundos para inicialización...
timeout /t 30 /nobreak > nul

echo.
echo [5/5] Verificando conexión...
docker-compose logs db --tail=10
echo.
docker exec appagua_db mysql -u root -e "SHOW DATABASES;" 2>nul
if %errorlevel% equ 0 (
    echo ✅ MySQL funciona correctamente!
    echo.
    echo Iniciando Django...
    docker-compose up -d web
    timeout /t 5 /nobreak > nul
    docker-compose ps
) else (
    echo ❌ MySQL aún tiene problemas
    echo Últimos errores:
    docker-compose logs db --tail=20
)

echo.
echo ============================================
echo           🎯 CONFIGURACIÓN FINAL
echo ============================================
echo MySQL: localhost:3307 (root/sin password)
echo Django: http://localhost:8000
echo.
echo Para acceder a MySQL desde tu PC:
echo   mysql -u root -h localhost -P 3307
echo.
echo Para crear un usuario específico en MySQL:
echo   docker exec -it appagua_db mysql -u root
echo   CREATE USER 'appuser'@'%%' IDENTIFIED BY 'password';
echo   GRANT ALL PRIVILEGES ON bd_sapam.* TO 'appuser'@'%%';
echo ============================================
pause
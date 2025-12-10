@echo off
echo ============================================
echo  DETENIENDO ENTORNO DE DESARROLLO
echo ============================================
echo.

cd /d "c:\sistemas\aplicacionespy"

echo [1/2] Deteniendo servicios...
docker-compose stop

echo.
echo [2/2] Verificando...
docker-compose ps

echo.
echo Servicios detenidos correctamente.
echo Para eliminar contenedores: docker-compose down
echo.
pause
# socIAlis
Equipo rosa

Despliegue local

Instalar python 3.*
  ejecutable o comando

Instalar pipenv:
  pip install pipenv

Clonar el repositorio con:
  git clone https://github.com/FelixAscWii/socIAlis.git

instalar todos los paquetes y librerias con:
  pipenv install --ignore-pipfile
o para installar una libreria nueva:
  pipenv install {{ nombre }}

Migraciones(    
  Crear migraciones:
    python manage.py makemigrations    
  Ejecutar migraciones:
    python manage.py migrate)

Para correr el servidor:
  python manage.py runserver    
  si sale un cohete, significa que vamos por buen camino

para crear un usuario admin:
  python manage.py createsuperuser    
  acceder al panel de administracion en:
    /admin


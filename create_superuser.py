# create_superuser.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tu_proyecto.settings")  # 👈 reemplaza 'tu_proyecto' por el nombre real del settings.py
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="ABI").exists():
    User.objects.create_superuser(
        username="ABI",
        password="GATITOS123",
        email="abi@example.com",  # puedes cambiar el email si lo deseas
        role="staff"  # 👈 opcional, si quieres que tenga el rol de staff personalizado
    )
    print("Superuser 'ABI' creado con éxito.")
else:
    print("El superuser 'ABI' ya existe.")

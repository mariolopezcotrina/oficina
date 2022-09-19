from django.contrib.auth.models import BaseUserManager

class AuthManager(BaseUserManager):
    def create_superuser(self, correo, password, nombre, apellido,rol):
        if not correo:
            raise ValueError('El super usuario no puede tener el correo vacio')
        
        correo_normalizado = self.normalize_email(correo)
        nuevoUsuario = self.model(correo=correo_normalizado, nombre=nombre, apellido=apellido, rol=rol, is_staff = True, is_superuser = True)
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()

        return nuevoUsuario
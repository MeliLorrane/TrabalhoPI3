from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # extendendo User padrão caso queira campos extras no futuro
    empresa = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=30, blank=True)

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(blank=True)
    contatos = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='contatos_de')

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_enviados')
    convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')
    aceito = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('solicitante', 'convidado')

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Perfil, Convite

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'empresa', 'telefone')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # cria Perfil associado
        Perfil.objects.create(user=user)
        Token.objects.create(user=user)
        return user

class PerfilSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pode_convidar = serializers.SerializerMethodField()

    class Meta:
        model = Perfil
        fields = ('id', 'user', 'bio', 'pode_convidar')

    def get_pode_convidar(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        try:
            meu_perfil = request.user.perfil
            return not obj in meu_perfil.contatos.all() and obj != meu_perfil
        except Exception:
            return False

class ConviteSerializer(serializers.ModelSerializer):
    solicitante = PerfilSerializer(read_only=True)
    convidado = PerfilSerializer(read_only=True)

    class Meta:
        model = Convite
        fields = ('id', 'solicitante', 'convidado', 'aceito', 'criado_em')

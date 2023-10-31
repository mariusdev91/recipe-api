from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
                        style={'input_type': 'password'},
                        write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            serializers.ValidationError({
                'Password validation':
                    'Passwords do not match!'
            })

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({
                'Email error':
                    'User already exists!'
            })

        account = User(email=self.validated_data['email'],
                       username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account

from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate


class CreateUserSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'password_confirmation',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """Verficar que las contraseñas coinciden"""
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(
                "Password confirmation doesn't match"
            )
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return get_user_model().objects.create_user(**validated_data)


class ObteinAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        user = authenticate(
            request=self.context.get('request'),
            username=data['email'],
            password=data['password']
        )
        if user is not None:
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError(
                'Unable to authenticate with provided credentials',
                code='authentication'
            )

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'phone', 'gender', 'country', 'state', 'medication_history']

        def create(self, validated_data):
            user = User.objects.create(
                email = validated_data['email'], 
                phone= validated_data['phone'],
                gender= validated_data['gender'],
                country= validated_data['country'],
                state= validated_data['state'],
                medication_history= validated_data['medication_history']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
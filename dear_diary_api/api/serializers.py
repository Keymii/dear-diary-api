from rest_framework import serializers
from main.models import userLogin

class userLoginSerializer (serializers.ModelSerializer):
    class Meta:
        model=userLogin
        fields='__all__'
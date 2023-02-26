from rest_framework import serializers
from main.models import userLogin, MasterTable

class userLoginSerializer (serializers.ModelSerializer):
    class Meta:
        model=userLogin
        fields='__all__'

class MasterTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=MasterTable
        fields='__all__'

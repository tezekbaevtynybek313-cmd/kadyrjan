from requests import Response
from rest_framework import serializers
from .models import Tasks



class TasksSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=True, max_length=50)
    class Meta:
        model = Tasks
        fields = '__all__'


    def validate_name(self, value):
        if value.strip() == "":
            raise serializers.ValidationError("Аты бош болбошу керек")
        return value


    def validate_phone(self, value):
        if len(value) < 9:
            raise serializers.ValidationError('телефон номери кыска')
        return value



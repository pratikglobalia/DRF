from rest_framework import serializers
from .models import Student

#Validators
def start_with_r(value):
    if value[0].lower() != 'p':
        raise serializers.ValidationError('name should be start with R')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    #Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'pratik' and ct.lower() != 'surat':
            raise serializers.ValidationError('city must be surat')
        return data
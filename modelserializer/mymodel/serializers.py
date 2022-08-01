from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    #validators
    def start_with_p(value):
        if value[0].lower() != 'p':
            raise serializers.ValidationError('name should be start with p')
    name = serializers.CharField(validators=[start_with_p])
    
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # fields = '__all__'
        # read_only_fields = ['name', 'roll']

    #Field level validation
    def validate_roll(self, value):
        if value >= 150:
            raise serializers.ValidationError('Seat Full')
        return value

    #Object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'pratik' and ct.lower() != 'keshod':
            raise serializers.ValidationError('Name must be pratik and city must be keshod')
        return data
from rest_framework import serializers
from ApiRest.models import People

class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['cod', 'name', 'height']

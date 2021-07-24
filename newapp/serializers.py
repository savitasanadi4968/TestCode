from rest_framework import serializers
from newapp.models import newapps


class newappSerializer(serializers.ModelSerializer):
    class Meta:
        model = newapps
        fields = ('id',
                  'title',
                  'description',
                  'published')
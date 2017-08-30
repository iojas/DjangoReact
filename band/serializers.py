from rest_framework import serializers
from models import *
class BandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Band
    fields = '__all__'

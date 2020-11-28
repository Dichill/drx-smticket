from rest_framework import serializers
from .models import SMVenuesResult
from .models import EventResult
from .models import OtherVenuesResult
from .models import AttractionsResult

class SMVenuesSerializer(serializers.ModelSerializer):
    class Meta():
        model = SMVenuesResult
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta():
        model =  EventResult
        fields = '__all__'

class OtherVenueSerializer(serializers.ModelSerializer):
    class Meta():
        model = OtherVenuesResult
        fields = '__all__'

class AttractionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = AttractionsResult
        fields = '__all__'

from rest_framework import serializers
from .models import Reservation
from branch.serializers import BranchSerializer
from users.serializers import CustomerSerializerGet
class ReservationGet(serializers.ModelSerializer):
    name = CustomerSerializerGet()
    branch = BranchSerializer()
    class Meta:
        model = Reservation
        fields = ("id","name","branch","type_of_service","datetime_start","datetime_end","is_done","rating","feedback")

class ReservationPost(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id","name","branch","type_of_service","datetime_start","datetime_end","is_done","rating","feedback")
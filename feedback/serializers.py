from .models import Feedback
from rest_framework import serializers
from users.serializers import CustomerSerializerGet
from branch.serializers import BranchSerializer
class FeedbackGet(serializers.ModelSerializer):
    name = CustomerSerializerGet()
    branch = BranchSerializer()
    class Meta:
        model = Feedback
        fields = ("id","branch","name","rating","feedback","datetime_given")

class FeedbackPost(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("id","branch","name","rating","feedback","datetime_given")
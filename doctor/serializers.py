from rest_framework import serializers
from .models import Specialization, Designation, AvailableTime, Doctor, Review

class SpecializationSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Specialization
        fields = '__all__'
        # ManyToMany field in Django doesn't support SerializerMethodField so we need to
        # use StringRelatedField instead which is read-only and works fine for our case
        # Used by the viewset to create a new specialization instance linked to an existing doctor
class DesignationSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Designation
        fields = '__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = AvailableTime
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'
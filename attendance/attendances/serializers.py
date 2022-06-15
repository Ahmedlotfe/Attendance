from rest_framework import serializers

from .models import Attendance

# serializer for attendance model
class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = [
            'user',
            'check_in',
            'check_out',
            'status',
            'duration'
        ]

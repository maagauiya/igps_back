from rest_framework import serializers

from .models import Messages, Devices

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['timeStamp', 'messageID', 'esn', 'unixTime', 'gps', 'payload']

class DevicesSerializer(serializers.ModelSerializer):
    messages = MessagesSerializer(many=True, read_only=True)
    class Meta:
        model = Devices
        fields = ['_id', 'esn', 'username', 'device']
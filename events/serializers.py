from allauth.account.templatetags.account import user_display_tag
from rest_framework import serializers, fields

from users.models import CustomUser
from events.models import Event, Transport, Place


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id'
        ]

    # name = serializers.SerializerMethodField()

    # def get_name(self, obj):
    #     return user_display_tag(obj)


class TransportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = [
            'id',
            'seats',
        ]


class PlaceEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            'title', 'description'
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 'transport', 'promoter'
        ]

    promoter = UserSerializer(many=True)
    transport = TransportEventSerializer(many=True)
    # place = PlaceEventSerializer()
    # user = UserSerializer()

    # def create(self, validated_data):
    #     transports_data = validated_data.pop('transport')
    #     event = Event.objects.create(**validated_data)
    #     for transport_data in transports_data:
    #         Transport.objects.create(event=event, **transport_data)
    #     return event
    #
    def update(self, instance, validated_data):
        transports_data = validated_data.pop('transport')
        transports = (instance.transport).all()
        transports = list(transports)
        promoters_data = validated_data.pop('promoter')
        promoters = (instance.promoter).all()
        promoters = list(promoters)

        for promoter_data in promoters_data:
            promoter = promoters.pop(0)
            promoter.id = promoter_data.get('id', promoter.id)
            promoter.save()

        for transport_data in transports_data:
            transport = transports.pop(0)
            transport.id = transport_data.get('id', transport.id)
            transport.seats = transport_data.get('seats') + transport.seats
            transport.save()
        return instance

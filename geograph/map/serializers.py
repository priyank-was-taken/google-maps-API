from rest_framework import serializers

# class AddressSerializer(serializers.Serializer):
#     city = serializers.CharField()
#     pincode = serializers.CharField()
#     address = serializers.CharField()
#     country = serializers.CharField()
#     address_components = serializers.ListField(child=serializers.DictField())


class AddressSerializer(serializers.Serializer):
    city = serializers.CharField()
    pincode = serializers.CharField()
    address = serializers.CharField()
    country = serializers.CharField()
    address_components = serializers.ListField(child=serializers.DictField())

class LocationSerializer(serializers.Serializer):
    lat = serializers.FloatField(min_value=-90, max_value=90)
    lng = serializers.FloatField(min_value=-180, max_value=180)    
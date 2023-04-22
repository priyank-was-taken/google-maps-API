import googlemaps
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from django.conf import settings

# class AddressView(APIView):
#     def get(self, request):
#         lat = 27.520965
#         lng = 76.622348

#         if not lat or not lng:
#             return Response({'error': 'Latitude and longitude are required parameters.'}, status=400)

#         gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
#         results = gmaps.reverse_geocode((lat, lng))

#         if not results:
#             return Response({'error': 'Could not retrieve address information.'}, status=404)

#         address_components = results[0]['address_components']
#         city = next((c['long_name'] for c in address_components if 'locality' in c['types']), '')
#         # pincode = next((c['long_name'] for c in address_components if 'postal_code' in c['types']), '')
#         postal_code_component = next((c for c in address_components if 'postal_code' in c['types']), {})
#         pincode = postal_code_component.get('long_name', postal_code_component.get('short_name', ''))
#         print(pincode, "hiihih")
#         address = results[0]['formatted_address']
#         country = next((c['long_name'] for c in address_components if 'country' in c['types']), '')

#         serializer = serializers.AddressSerializer({'city': city, 'pincode': pincode, 'address': address, 'country': country, 'address_components': address_components})
#         return Response(serializer.data)

# import googlemaps
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import AddressSerializer, LocationSerializer
# from django.conf import settings

# class AddressView(APIView):
#     def get(self, request):
#         lat = request.query_params.get('lat', None)
#         lng = request.query_params.get('lng', None)

#         if not lat or not lng:
#             return Response({'error': 'Latitude and longitude are required parameters.'}, status=400)

#         gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
#         results = gmaps.reverse_geocode((lat, lng))

#         if not results:
#             return Response({'error': 'Could not retrieve address information.'}, status=404)

#         address_components = results[0]['address_components']
#         # print(address_components)
#         city = next((c['long_name'] for c in address_components if 'locality' in c['types']), '')
#         pincode = next((c['long_name'] for c in address_components if 'postal_code' in c['types']), '')
#         # print(pincode)  # Debugging line
#         address = results[0]['formatted_address']
#         country = next((c['long_name'] for c in address_components if 'country' in c['types']), '')

#         serializer = AddressSerializer({'city': city, 'pincode': pincode, 'address': address, 'country': country, 'address_components': address_components, 'hello': 'world'})
#         return Response(serializer.data)

class AddressView(APIView):
    def get(self, request):
        serializer = serializers.LocationSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        lat = serializer.validated_data['lat']
        lng = serializer.validated_data['lng']

        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        results = gmaps.reverse_geocode((lat, lng))

        if not results:
            return Response({'error': 'Could not retrieve address information.'}, status=404)

        address_components = results[0]['address_components']
        city = next((c['long_name'] for c in address_components if 'locality' in c['types']), '')
        pincode = next((c['long_name'] for c in address_components if 'postal_code' in c['types']), '')
        address = results[0]['formatted_address']
        country = next((c['long_name'] for c in address_components if 'country' in c['types']), '')

        serializer = serializers.AddressSerializer({'city': city, 'pincode': pincode, 'address': address, 'country': country, 'address_components': address_components})
        return Response(serializer.data)
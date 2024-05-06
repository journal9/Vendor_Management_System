from rest_framework import serializers

from .models import VendorsModel


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorsModel
        fields = [
            'vendor_code',
            'name',
            'address', 
            'contact_details',
            'on_time_delivery_rate',
            'quality_rating_avg',
            'average_response_time',
            'fulfillment_rate',
        ]

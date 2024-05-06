from rest_framework import serializers

from .models import POModel


class POSerializer(serializers.ModelSerializer):

    class Meta:
        model = POModel
        fields = [
            "po_number",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgment_date"
        ]

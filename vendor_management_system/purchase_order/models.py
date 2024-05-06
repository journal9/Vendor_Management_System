from django.db import models
from vendor.models import VendorsModel
from django.utils.timezone import now

class OrderStatus(models.TextChoices):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class PO(models.Model):
    po_number= models.CharField(max_length=20,unique=True)
    vendor= models.ForeignKey(VendorsModel,on_delete=models.CASCADE)
    order_date=models.DateTimeField(default=now, editable=False)
    delivery_date=models.DateTimeField(null=False)
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.TextField(choices=OrderStatus.choices, default=OrderStatus.PENDING)
    quality_rating=models.FloatField(null=True)
    issue_date=models.DateTimeField(editable=False)
    acknowledgment_date=models.DateTimeField(null=True, editable=False)

    class Meta:
        ordering = ["-order_date"]

    def get_po(self):
        return{
            "po_number":self.po_number,
            "order_date":self.order_date,
            "delivery_date":self.delivery_date,
            "items":self.items,
            "quantity":self.quantity,
            "status":self.status,
            "quality_rating":self.quality_rating,
            "issue_date":self.issue_date,
            "acknowledgment_date":self.acknowledgment_date,
        }
    
class POModel(models.Model):
    po_id = models.AutoField(primary_key=True)
    po_number= models.CharField(max_length=20,unique=True)
    vendor= models.ForeignKey(VendorsModel,on_delete=models.CASCADE)
    order_date=models.DateTimeField(default=now, editable=False)
    delivery_date=models.DateTimeField(null=False)
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.TextField(choices=OrderStatus.choices, default=OrderStatus.PENDING)
    quality_rating=models.FloatField(null=True)
    issue_date=models.DateTimeField(editable=False)
    acknowledgment_date=models.DateTimeField(null=True, editable=False)

    class Meta:
        ordering = ["-order_date"]

    def get_po(self):
        return{
            "po_number":self.po_number,
            "order_date":self.order_date,
            "delivery_date":self.delivery_date,
            "items":self.items,
            "quantity":self.quantity,
            "status":self.status,
            "quality_rating":self.quality_rating,
            "issue_date":self.issue_date,
            "acknowledgment_date":self.acknowledgment_date,
        }
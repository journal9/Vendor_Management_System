from django.db import models

    
class Vendors(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(unique=True,max_length=20)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

    class Meta:
        ordering = ["vendor_code"]

    def get_vendor(self):
        return{
            "vendor_code":self.vendor_code,
            "name":self.name,
            "contact_details":self.contact_details,
            "address":self.address,
            "on_time_delivery_rate":self.on_time_delivery_rate,
            "quality_rating_avg":self.quality_rating_avg,
            "average_response_time":self.average_response_time,
            "fulfillment_rate":self.fulfillment_rate

        }
    
class VendorsModel(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(unique=True,max_length=20)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

    class Meta:
        ordering = ["vendor_code"]

    def get_vendor(self):
        return{
            "vendor_code":self.vendor_code,
            "name":self.name,
            "contact_details":self.contact_details,
            "address":self.address,
            "on_time_delivery_rate":self.on_time_delivery_rate,
            "quality_rating_avg":self.quality_rating_avg,
            "average_response_time":self.average_response_time,
            "fulfillment_rate":self.fulfillment_rate
        }
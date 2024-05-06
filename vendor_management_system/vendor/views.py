from django.shortcuts import render
from django.views import View
# from urllib.request import Request
from django.http.response import JsonResponse
from .models import VendorsModel
from .vendorSerializers import VendorSerializer
import traceback
import logging
import json

logger = logging.getLogger(__file__)

# Create your views here.
class VendorView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            vendor = VendorsModel(
                name=data.get('name'),
                address=data.get('address'),
                contact_details=data.get('contact_details'),
                vendor_code=data.get('vendor_code')
            )
            vendor.save()
            return JsonResponse({"v_id":vendor.vendor_id}, status=200) 
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

    def get(self,request):
        try:
            all_vendors = VendorsModel.objects.all()
            vendor_serializer = VendorSerializer(all_vendors, many=True, context={"request": request})
            return JsonResponse(vendor_serializer.data, safe=False, status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

class OnVEndor(View):
    def get(self,request,vendor_id):
        try:
            vendor = VendorsModel.objects.get(vendor_id=vendor_id)
            return JsonResponse(vendor.get_vendor(), status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

    def patch(self,request,vendor_id):
        try:
            vendor = VendorsModel.objects.get(vendor_id=vendor_id)
            entered_data = json.loads(request.body)
            if 'name' in entered_data.keys():
                vendor.name=entered_data['name']
            if 'contact_details' in entered_data.keys():
                vendor.contact_details=entered_data['contact_details']
            if 'address' in entered_data.keys():
                vendor.address = entered_data['address']
            vendor.save()
            return JsonResponse(vendor.get_vendor(), status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

    def delete(self,request,vendor_id):
        try:
            vendor = VendorsModel.objects.get(vendor_id=vendor_id)
            vendor.delete()
            return JsonResponse({'success':True}, status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)
    

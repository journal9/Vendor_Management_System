from django.shortcuts import render
from django.views import View
# from urllib.request import Request
from django.http.response import JsonResponse
from .models import POModel
from .po_serializers import POSerializer
import traceback
import logging
import json
from django.utils.timezone import now

logger = logging.getLogger(__file__)

# Create your views here.
class POView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            po = POModel(
                vendor=data.get('vendor'),
                order_date=data.get('order_date'),
                delivery_date=data.get('delivery_date'),
                items=data.get('items'),
                quantity=data.get('quantity')
            )
            po.issue_date = now()
            print(po.issue_date)
            po.save()
            return JsonResponse({"v_id":po.po_number}, status=200) 
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

    def get(self,request):
        try:
            all_orders = POModel.objects.all()
            po_serializer = POSerializer(all_orders, many=True, context={"request": request})
            return JsonResponse(po_serializer.data, safe=False, status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

class OnPOView(View):
    def get(self,request,po_id):
        try:
            order = POModel.objects.get(po_id=po_id)
            return JsonResponse(order.get_po(), status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

    def patch(self,request,po_id):
        try:
            order = POModel.objects.get(po_id=po_id)
            order_data = json.loads(request.body)
            if 'delivery_date' in order_data.keys():
                order.delivery_date=order_data['delivery_date']
            if 'items' in order_data.keys():
                order.items=order_data['items']
            if 'quantity' in order_data.keys():
                order.quantity = order_data['quantity']
            if 'status' in order_data.keys():
                order.status = order_data['status']
            if 'quality_rating' in order_data.keys():
                order.quality_rating = order_data['quality_rating']
            order.save()
            return JsonResponse(order.get_po(), status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

    def delete(self,request,po_id):
        try:
            order = POModel.objects.get(po_id=po_id)
            order.delete()
            return JsonResponse({'success':True}, status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

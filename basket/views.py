from django.shortcuts import render
from .basket import Basket
from django.shortcuts import get_object_or_404
from store.models import Product
from django.http import JsonResponse, HttpResponse

# Create your views here.

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {"basket": basket})


def basket_add(request):
    basket = Basket(request)
    if 'action' in request.POST:
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty= product_qty)
        basketqty = basket.__len__()

        response = JsonResponse({"qty": basketqty})
  
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.method == 'POST':
        data = request.data
        product_id = data['product_id']
        product = Product.objects.filter(id=product_id)
        product.delete()
    return basket
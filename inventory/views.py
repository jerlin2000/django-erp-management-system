from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum,Q
from .models import Product
@staff_member_required
def dashboard(request):
    products = Product.objects.annotate(purchased=Sum('transaction__quantity',filter=Q(transaction__kind='purchase'),default=0),sold=Sum('transaction__quantity',filter=Q(transaction__kind='sale'),default=0))
    return render(request,'inventory/dashboard.html',{'rows':[(p,p.opening_stock+p.purchased-p.sold) for p in products]})

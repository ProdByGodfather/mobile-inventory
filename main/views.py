from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from main.models import Brand, Mobile
from main.forms import BrandForm, MobileForm
from django.db.models import Q, F

def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'برند با موفقیت اضافه شد.')
            return redirect('brand_list')
    else:
        form = BrandForm()
    return render(request, 'inventory/create_brand.html', {'form': form})

def create_mobile(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'گوشی با موفقیت اضافه شد.')
            return redirect('mobile_list')
    else:
        form = MobileForm()
    return render(request, 'inventory/create_mobile.html', {'form': form})

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'inventory/brand_list.html', {'brands': brands})

def mobile_list(request):
    mobiles = Mobile.objects.all()
    brand_name = request.GET.get('brand_name', '')
    selected_brand_id = request.GET.get('selected_brand', '')
    filter_by_nationality = request.GET.get('filter_by_nationality', 'off') == 'on'
    filter_by_status = request.GET.get('selected_status','')
    
    if brand_name:
        mobiles = mobiles.filter(brand__name__icontains=brand_name)

    if selected_brand_id:
        mobiles = mobiles.filter(brand__id=selected_brand_id)

    if filter_by_nationality:
        mobiles = mobiles.filter(brand__nationality=F('manufacturing_country'))

    if filter_by_status:
        if filter_by_status == "unavailable":
            mobiles = mobiles.filter(status='unavailable')
        elif filter_by_status == "available":
            mobiles = mobiles.filter(status='available')
            
    
    brands = Brand.objects.all() 
    return render(request, 'inventory/mobile_list.html', {
        'mobiles': mobiles,
        'brands': brands,
        'brand_name': brand_name,
        'selected_brand_id': selected_brand_id,
        'filter_by_nationality': filter_by_nationality,
        'filter_by_status':filter_by_status
    })

def korean_brands(request):
    brands = Brand.objects.filter(nationality='Korea')
    return JsonResponse(list(brands.values('name', 'nationality')), safe=False)

def mobiles_by_brand(request):
    brand_name = request.GET.get('brand')
    if brand_name:
        mobiles = Mobile.objects.filter(brand__name=brand_name)
        return JsonResponse(list(mobiles.values('model', 'price', 'color')), safe=False)
    return JsonResponse([], safe=False)

def matching_nationality_mobiles(request):
    mobiles = Mobile.objects.filter(brand__nationality=F('manufacturing_country'))
    return JsonResponse(list(mobiles.values('model', 'brand__name', 'manufacturing_country')), safe=False)
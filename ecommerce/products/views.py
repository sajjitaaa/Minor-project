from django.shortcuts import render, Http404
from .models import Product, ProductImage
# Create your views here.


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query': q, 'products': products}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
    return render(request, template, context)



def home(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/home.html'
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        images = product.productimage_set.all() #kyuki product Product ka instance hai na
        context = {'product': product, 'images': images}
        template = 'products/single.html'

    except:
        raise Http404

    return render(request, template, context)

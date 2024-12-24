from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices  import price_choices, bedroom_choices, district_choices
# Create your views here.
def index(request):
    listings = Listing.objects.order_by ('-list_date').filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html', context)
                  
def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    context = {
        'price_choices': price_choices,
        'bedrroom_choices': bedroom_choices,
        'district_choices': district_choices
    }
    return render(request, 'listings/search.html', context)
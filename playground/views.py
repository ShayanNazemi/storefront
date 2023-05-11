from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q, F, Min, Max, Count, Avg, Sum, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from store.models import Product, OrderItem, Order, Customer, Collection

from tags.models import TaggedItem

def say_hello(request):
    try:
        pass
        #product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass

    # None if doesnt exists
    #product = Product.objects.filter(pk=0).first()
    
    # None if doesnt exists
    #exists = Product.objects.filter(pk=1).exists()
    
    #queryset = Product.objects.filter(unit_price__range=(20, 30))
    
    #queryset = Product.objects.filter(title__icontains='coffee')
    
    #queryset = Product.objects.filter(last_update__year=2021)
    
    #queryset = Product.objects.filter(description__isnull=True)
    
    #queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    #queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    #queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    
    #queryset = Product.objects.filter(inventory=F('unit_price'))
    #queryset = Product.objects.filter(inventory=F('collection__id'))
    
    ###########
    # Sorting
    ###########
    
    #queryset = Product.objects.order_by('title')
    #queryset = Product.objects.order_by('-title')
    
    #queryset = Product.objects.order_by('inventory', 'title')
    
    #queryset = Product.objects.order_by('unit_price')[0]
    #queryset = Product.objects.earliest('unit_price') # ascending order
    #queryset = Product.objects.latest('unit_price') # descending order
    
    ###########
    # Slicing
    ###########
    #queryset = Product.objects.all()[:5]
    #queryset = Product.objects.all()[5:10]
    
    ###########
    # Selecting
    ###########
    #queryset = Product.objects.values('id', 'title', 'collection__title')
    #queryset = Product.objects.values_list('id', 'title', 'collection__title')
    
    
    #queryset = Product.objects.filter(pk=F('orderitem__product_id'))
    #queryset = Product.objects.filter(pk=F('orderitem__product_id')).distinct()
    
    #queryset = OrderItem.objects.values('product_id')
    #queryset = OrderItem.objects.values('product_id').distinct()
    #queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())
    
    #queryset = Product.objects.all() # dangerous
    #queryset = Product.objects.select_related('collection').all()
    
    # select_related when other end of relationship is 1
    # prefetch_related when other end of relationship is n
    
    #queryset = Product.objects.prefetch_related('promotions').all()
    #queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    
    #queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    ##########
    # Aggregation
    ##########
    #results =  Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
    
    ##########
    # Annotation
    ##########
    #queryset = Customer.objects.annotate(is_new=Value(True))
    #queryset = Customer.objects.annotate(new_id=F('id'))
    #queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    #queryset = Customer.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
    
    #queryset = Customer.objects.annotate(orders_count=Count('order'))    
    
    #discounted_price=ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    #queryset = Product.objects.annotate(discounted_price=discounted_price)
    
    
    ##########
    # Generic Relationships
    ##########
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type, 
    #         object_id=1
    #     )
    # TaggedItem.objects.get_tags_for(Product, 1)
    
    ##########
    # Creating Objects
    ##########
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    
    ##########
    # Updating Objects
    ##########
    # collection = Collection(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()
    
    # Sets title to '' - DANGEROUS
    # collection = Collection(pk=11)
    # collection.featured_product = None
    # collection.save()
    
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()
    
    #Collection.objects.filter(pk=11).update(featured_product=None)
    
    ##########
    # Deleting Objects
    ##########
    #collection = Collection(pk=11)
    #collection.delete()
    
    #Collection.objects.filter(id__gt=5).delete()
    
    ##########
    # Transactions
    ##########
    # ...
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()
        
        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()
    
    
    return render(request, 'hello.html', 
                  {'name' : 'Shayan'}
                  )
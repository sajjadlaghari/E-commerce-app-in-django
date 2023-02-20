from django.shortcuts import render
from django.http import HttpResponseRedirect
from products.models import Product
from django.contrib.auth.models import User
from django.shortcuts import redirect
from products.models import Cart


def ProductAddToCart(request):

     
    if request.method == "POST":

        product_id = request.POST.get('product_id')
        user_id    = request.POST.get('user_id')
        price      = request.POST.get('product_price')
        quantity      = request.POST.get('quantity')

        price = float(price)
        quantity = int(quantity)

        print(type(price))

        product =  Product.objects.get(id=product_id)
        user  =  User.objects.get(id=user_id)
     

        try:
            get_product = Cart.objects.get(product_id = product_id,user_id= user_id)
            get_price = get_product.price
            old_quantity = get_product.quantity

            total_quantity = old_quantity+quantity
            totlal_price   = get_price+price
 

            old_product = Cart.objects.get(product_id = product_id)

            old_product.price = totlal_price
            old_product.quantity = total_quantity

            old_product.save()
            
            return  redirect('/product/'+product_id)

        except:
            cart = Cart()
            cart.product = product
            cart.user    = user
            cart.price   = price
            cart.quantity = quantity

            cart.save()

            print("EXCEPT WORKED")
            return  redirect('/product/'+product_id)
    return  HttpResponseRedirect(request.path_info)


def ViewCartProducts(request):

    current_user = request.user

    context = {'products':Cart.objects.filter(user_id = current_user.id)}

    print(context)

    return render(request,'product/products-cart.html',context)


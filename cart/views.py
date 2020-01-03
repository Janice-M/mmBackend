from django.shortcuts import render
from django.contrib import messages

# Create your views here.
# Add to Cart View

def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This car part was updated.")
            return redirect("mainapp:home")
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("mainapp:home")
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("mainapp:home")
    
    
    
    
    
#Removing item from the cart
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("mainapp:home")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("mainapp:home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:home")


#view for all items in the cart app

def CartView(request):
    user = request.user
    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user, ordered=False)
    
    
    
    if carts.exists():
        order = orders[0]
        return render(request, 'cart/home.html', {"carts": carts, 'order': order})
		
    else:
        messages.warning(request, "You do not have an active order at my mech")
        return redirect("core:home")
#decrease

def decreaseCart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                    order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
            messages.info(request, f"{item.name} quantity of spares has updated.")
            return redirect("mainapp:cart-home")
        else:
            messages.info(request, f"{item.name} quantity of spares has updated.")
            return redirect("mainapp:cart-home")
        else:
            messages.info(request, "You do not have an active order on my mech")
        return redirect("mainapp:cart-hom
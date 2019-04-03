from django.shortcuts import render, redirect, reverse

# Create your views here.

#view to render cart page
def view_cart(request):
    
    return render(request, "cart.html")
#add upvote to cart    
def add_to_cart(request, id):
    quantity = 1
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect('view_cart')

# view for deleting from cart
def adjust_cart(request, id):
    
    cart = request.session.get('cart', {})
    cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    

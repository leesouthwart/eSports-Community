from django.shortcuts import get_object_or_404
from issue_tracker.models import Content

def cart_contents(request):
    
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    content_count = 0
    
    for id, quantity in cart.items():
        content = get_object_or_404(Content, pk=id)
        total += quantity * content.price
        content_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'content': content})
    
    return {'cart_items': cart_items, 'total': total, 'content_count': content_count}
    
    
    
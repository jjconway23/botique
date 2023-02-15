from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from djang.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['curren_bag']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MEZy7BSEnCju9Q6u35N1aXl1t372dWOZEvS6t1IBtXyi3PSYF2K5LhamR2nAd2AY1gQtHyNpTkkntLQNEnylBZ9001CrWkwBg',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
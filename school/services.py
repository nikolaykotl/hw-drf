import stripe
from django.shortcuts import redirect

stripe.api_key = 'sk_test_51ONH6GHovNnm9EPfrzlsQiKzdZI2dUjI8duMjL5iQUDz38udmfI8prT087BYodPQuajNNfWP7AI54FUDvgIC7WgP00QBNyWSe6'


def link_to_pay(obj):

    product = stripe.Product.create(name=obj.name)

    price = stripe.Price.create(
        unit_amount=int(obj.price*100),
        currency="rub",
       # recurring={"interval": "month"},
        product=product.id,
    )

    payment_link = stripe.PaymentLink.create(
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            }
        ]
    )
    return payment_link.url


def payment():
    payments = stripe.Charge.list(limit=3)
    return payments
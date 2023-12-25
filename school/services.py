import stripe
from django.conf import settings

from school.models import Lessons, Course

stripe.api_key = settings.STRIPE_SECRET_KEY




def link_to_pay(obj):
    if obj in Lessons.objects.all():
        product = stripe.Product.create(name=f'lesson, {obj.id}, {obj.name}')
    elif obj in Course.objects.all():
        product = stripe.Product.create(name=f'course, {obj.id}, {obj.name}')

    price = stripe.Price.create(
        unit_amount=int(obj.price*100),
        currency="rub",
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


#def payment():
#    payments = 0#stripe.PaymentIntent.list()
 #   return payments
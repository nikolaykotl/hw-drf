import stripe
from django.conf import settings

from django.http import HttpResponse

from rest_framework.decorators import api_view

from rest_framework.response import Response

from school.models import Course


stripe_api_key = settings.STRIPE_SECRET_KEY


@api_view(['POST'])
def CourseStripeIntent(request,*args, **kwargs):

    if request.user.is_authenticated:
        user = request.user
        email = user.email
        pk = kwargs['pk']
        customer_data = stripe.Customer.list(email=email).data
        if len(customer_data) == 0:
            customer = stripe.Customer.create(email=email)
        else:
            customer = customer_data[0]
        product_id = pk
        product = Course.objects.get(id=product_id)
        payment_intent = stripe.PaymentIntent.create(amount= int(product.price*100), currency= 'rub', customer= customer['id'], metadata={'product_id':pk})
        id = payment_intent['id']
        response = stripe.PaymentIntent.retrieve(id)
        customer_id = response['customer']
        customer = stripe.Customer.retrieve(customer_id)
        return Response(response)
    return HttpResponse(status=200)

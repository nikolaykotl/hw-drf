from datetime import date

import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from school.models import Payments, Course, Lessons, Subscription
from users.models import User

@csrf_exempt
def stripe_webhook(request):
    global name, email, intent, amount
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)



    if event['type'] == 'product.created':
        product = event['data']['object']
        name = product.name.split(', ')

    elif event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        email = session.customer_details.email
    elif event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        amount = float(intent.amount)/100
        if name[0] == 'course':
            course = Course.objects.get(pk=name[1])
            user = User.objects.get(email=email)
            Payments.objects.create(
                date_payment=date.today(),
                payment_amount=amount,
                user_id= user.id,
                course=course,
                payment_method='перевод'
            )
            Subscription.objects.create(user=user, course=course)
        elif name[0] == 'lesson':
            lesson = Lessons.objects.get(pk=name[1])
            user = User.objects.get(email=email)
            Payments.objects.create(
                date_payment=date.today(),
                payment_amount=amount,
                user_id=user.id,
                lesson=lesson,
                payment_method='перевод'
            )
    return HttpResponse(status=200)


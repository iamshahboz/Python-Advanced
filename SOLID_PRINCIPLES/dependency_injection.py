
# violating dependency injection rule
# class PayPalService:
#     def process_payment(self, amount):
#         print(f"Processing payment of ${amount} through PayPal")


# class PaymentProcessor:
#     def __init__(self):
#         self.payment_service = PayPalService()

#     def pay(self, amount):
#         self.payment_service.process_payment(amount)


# processor = PaymentProcessor()
# processor.pay(100)

'''

What if you want the other payment service: Stripe
With dependency Injection we create dependency outside of 
the context and then inject it as a variable

'''

class PayPalService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through PayPal")


class PaymentProcessor:
    def __init__(self, payment_service):
        self.payment_service  = payment_service


    def pay(self, amount):
        self.payment_service.process_payment(amount)

payment_service = PayPalService()

processor = PaymentProcessor(payment_service)
processor.pay(250)


"""Demonstration of the Single Responsibility Principle (SRP) in Python"""

# Class to represent an order with basic attributes
class Order:
    def __init__(self, order_id, amount, weight):
        self.order_id = order_id  # Store the order's unique ID
        self.amount = amount      # Store the total amount of the order
        self.weight = weight      # Store the weight of the order
    def __str__(self):
        return f"Order ID: {self.order_id} with weight {self.weight} kg has a payable amount of ${self.amount:.2f}"


# Class responsible for saving and retrieving order data (simulated here)
class OrderRepository:
    def get_order(self, order_id: str, amount: float, weight: float) -> Order:
        return Order(order_id, amount, weight)

    def save_order(self, order: Order):
        # Simulate saving the order by printing a message
        print(f"updated Order: {order.order_id}")

# Class responsible for processing Stripe payments
class StripeProcessor:
    def pay(self, amount: float):
        # Simulate charging an amount using Stripe
        print(f"[Stripe] charged ${amount:.2f}")  # Format amount to 2 decimal places

    def refund(self, transaction_id):
        # Simulate refunding a transaction using Stripe
        print(f"[Stripe] Refund transaction {transaction_id}")

# Class responsible for processing Bank payments
class BankProcessor:
    def pay(self, transaction_id, amount: float):
        # Simulate charging an amount through a bank
        print(f"[Bank] charged ${amount:.2f}")  # Format amount to 2 decimal places

# Class responsible for handling the full order process (getting order, paying, saving)
class OrderProcessor:
    def __init__(self, repo: OrderRepository, payment=StripeProcessor()):
        self.repo = repo          # Store the repository used to get/save orders
        self.payment = payment    # Store the payment processor (Stripe or Bank)
    def process(self,order_id,amount:float,weight:float):
       # order = self.repo.get_order(order_id, amount, weight)#same line below but using self is more good 
       # Get the order details from the repository
        order=self.repo.get_order (order_id,amount,weight)
        print(order)
        # Process payment accessing stripeProcessor pay method by using attribute of payment in orderprocessor
        self.payment.pay(order.amount)

        # Save the order after payment
        self.repo.save_order(order)

        
    
#Example Usage
# --------------------

# Create an instance of OrderRepository
repo1 = OrderRepository()

# Create an instance of the payment processor (Stripe)
stripe_payment = StripeProcessor()

# You can also use BankProcessor like this:
# bank_payment = BankProcessor()

# Create the OrderProcessor using Stripe
processor = OrderProcessor(repo1, stripe_payment)

# Process the order with order ID, amount, and weight
processor.process("101", 250.0, 5.5)


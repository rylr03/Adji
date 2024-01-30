from django.db import models


class Customer(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer not to say'),
    )

    customer_name = models.CharField(max_length=50, null=True)
    user_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True)
    home_add = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    COLOR_CHOICES = (
        ('pink', 'Pink'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('gray', 'Gray'),
        ('black', 'Black'),
        ('green', 'Green'),
        ('purple', 'Purple'),
    )
    TYPE_CHOICES = (
        ('t-shirt', 'T-shirt'),
    )
    CATEGORY_CHOICES = (
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
    )


    product_name = models.CharField(max_length=100, null=True)
    product_type = models.CharField(max_length=100, choices= TYPE_CHOICES)
    product_category = models.CharField(max_length=100, choices= CATEGORY_CHOICES)
    color = models.CharField(max_length=50, choices= COLOR_CHOICES)
    price = models.IntegerField(null=True)
    info = models.TextField(max_length=100, blank=True)
    image = models.ImageField(upload_to='staticfiles', null=True, blank=True)
    
    def __str__(self):
        return self.product_name
    

class Order(models.Model):
    SIZE_CHOICES = (
        ('Small', 'S'),
        ('Medium', 'M'),
        ('Large', 'L'),
        ('Extra Large', 'XL'),
    )
    MOP_CHOICES = (
        ('cod', 'Cash on Delivery'),

    )
    

    order_name = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(Customer, related_name='order', on_delete=models.CASCADE)
    sizes = models.CharField(max_length=100, choices= SIZE_CHOICES, null=True)
    order_item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100, choices= MOP_CHOICES, null=True)


    def __str__(self):
        return self.order_name


class OrderApproval(models.Model):
    APPROVAL_TYPE_CHOICES = (
        ('pending', 'To be Process'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    )
    approval_for = models.CharField(max_length=200, null=True)
    order = models.ForeignKey(Order, related_name='approve', on_delete=models.CASCADE, null=True)
    approval_action = models.CharField(max_length=200, choices= APPROVAL_TYPE_CHOICES)
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.approval_for
    
    
class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, related_name='shipping', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.address

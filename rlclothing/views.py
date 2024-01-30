from django.shortcuts import get_object_or_404, render, redirect
from .models import *

#forms
from .forms import CustomerForm
from .forms import OrderForm
from .forms import ProductForm
from .forms import ShippingForm
from .forms import ApprovalForm




def dash_board(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    shippings = ShippingAddress.objects.all()
    order_status = OrderApproval.objects.all()
    who_orders = Customer.objects.select_related('customer_name').all()


    total_customer = customers.count()
    total_products = products.count()
    total_orders = orders.count()
    pending = order_status.filter(approval_action='pending').count()
    approved = order_status.filter(approval_action='approved').count()
    declined = order_status.filter(approval_action='declined').count()

    context = {
        'customers':customers,
        'products':products,
        'orders':orders,
        'shippings':shippings,
        'order_status':order_status,
        'who_orders': who_orders,

        'total_customer':total_customer,
        'total_products':total_products,
        'total_orders':total_orders,
        'pending':pending,
        'approved':approved,
        'declined':declined,
    }
    return render(request,'pages/adminpage.html', context)

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        customer.delete()
        return redirect('dashboard')  

    return render(request, 'deletecusto.html', {'customer': customer})

def product_admin(request):
    products = Product.objects.all()
    return render(request,'pages/Products.html', {'products':products})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard') 
    else:
        form = CustomerForm()

    return render(request, 'pages/createcusto.html', {'form': form})

def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'pages/updatecusto.html', {'form': form, 'customer': customer})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productadmin') 
    else:
        form = ProductForm()

    return render(request, 'pages/createprod.html', {'form': form})


def delete_product(request, product_id):
    product_to_delete = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product_to_delete.delete()
        return redirect('productadmin') 

    return render(request, 'deleteprodconfirm.html', {'product_to_delete': product_to_delete})

def update_product(request, pk):
    instance = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('productadmin') 
    return render(request, 'pages/update.html', {'form': form, 'instance': instance, 'pk': instance.pk})


def approvals_page(request):    
    orders = Order.objects.all()
    approves = OrderApproval.objects.all()

    context = {
        'approves': approves,
        'orders': orders,
    }

    return render(request, 'pages/approve.html', context)

def delete_orderapp(request, approves_id):
    ordapp_to_delete = get_object_or_404(OrderApproval, id=approves_id)

    if request.method == 'POST':
        ordapp_to_delete.delete()
        return redirect('approvalspage') 

    return render(request, 'deleteorderapp.html', {'ordapp_to_delete': ordapp_to_delete})

def update_orderapp(request, pk):
    instance = get_object_or_404(OrderApproval, pk=pk)
    form = ApprovalForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('approvalspage')
     
    return render(request, 'pages/updateorderapp.html', {'form': form, 'instance': instance, 'pk': instance.pk})

def create_orderapp(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('approvalspage') 
    else:
        form = ApprovalForm()

    return render(request, 'pages/createorderapp.html', {'form': form})

def product_page(request):
    products = Product.objects.all()

    context = {
        'products':products
    }
    return render(request,'pages/Productpage.html')


def home_page(request):
    return render(request,'pages/Homepage.html')

def about_page(request):
    return render(request,'pages/Aboutpage.html')


    
def orders_page(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipping_add')

    context = {'form': form}
    
    return render(request,'pages/orderspage.html', context)


def register_customer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    
    return render(request, 'pages/CustomerRegister.html', context)


def shipping_add(request):
    form = ShippingForm()

    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    
    return render(request, 'pages/shippingadd.html', context)



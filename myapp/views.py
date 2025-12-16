from django.shortcuts import render,redirect
from django.contrib import auth 
from .models import Product, Category
def index(request): 
    return render(request,'index.html') 
 
def about(request): 
    return render(request,'about.html') 
 
def blog(request): 
    return render(request,'blog.html') 
 


def contact(request): 
    return render(request,'contact.html') 
 
def services(request): 
    return render(request,'services.html') 
 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print('login successfully!')
        if user is not None:
            auth_login(request, user)  # Use Django's login
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')



def logout(request): 
    auth.logout(request) 
    print('Logout successfully!') 
    return redirect('/') 

def register(request): 
    return render(request,'register.html')

from django.shortcuts import render, redirect 
from django.contrib import auth 
from django.contrib.auth.models import User 
 
def register(request): 
    if request.method == 'POST': 
        fn=request.POST['first_name'] 
        ln=request.POST['last_name'] 
        em=request.POST['email'] 
        un=request.POST['uname'] 
        p1=request.POST['pass1'] 
        p2=request.POST['pass2'] 
        if p1 != p2: 
            print("Password doesn't Match!") 
            return redirect('/register/') 
 
        if User.objects.filter(username=un).exists(): 
            print('Username already exists! Try another Username') 
            return redirect('/register/') 
        if User.objects.filter(email=em).exists(): 
            print('Email already exists! Try Again') 
            return redirect('/register/') 
 
        User.objects.create_user( 
            first_name=fn, 
            last_name=ln, 
            email=em, 
            username=un, 
            password=p1 
        ) 
         
        print('UserID created Successfully') 
        return redirect('/login/') 
 
    # THIS LINE MUST BE OUTSIDE THE POST BLOCK 
    return render(request, 'register.html')

def icecream(request):
    products = Product.objects.all()
    return render(request, 'icecream.html', {'products': products})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product  # replace with your model

# Add item to cart
def add_to_cart(request, pid):
    product = get_object_or_404(Product, pid=pid)

    # Initialize cart if not exists
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    # Use string key for session dict
    if str(pid) in cart:
        cart[str(pid)]['quantity'] += 1  # Increase quantity
    else:
        cart[str(pid)] = {
            'name': product.pname,
            'price': float(product.pprice),
            'quantity': 1
        }

    request.session.modified = True
    return redirect('icecream')

# View cart
def cart(request):
    cart_items = []
    total_price = 0

    if 'cart' in request.session:
        for item_id, item in request.session['cart'].items():
            item_total = item['price'] * item['quantity']
            cart_items.append({
                'name': item['name'],
                'price': item['price'],
                'quantity': item['quantity'],
                'total': item_total
            })
            total_price += item_total

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })
from django.contrib import messages

def place_order(request):
    if request.method == "POST":
        payment_mode = request.POST.get('payment_mode')
        coupon_code = request.POST.get('coupon_code')

        cart = request.session.get('cart', {})

        # Calculate cart total
        total = 0
        for item in cart.values():
            total += item['price'] * item['quantity']

        # Apply coupon
        if coupon_code and coupon_code.upper() == 'ICE10':
            total = total * 0.9  # 10% discount

        # Clear cart after order
        request.session['cart'] = {}
        request.session.modified = True

        messages.success(
            request,
            f"Order placed successfully! Payment: {payment_mode}. Total: ₹{total:.2f}"
        )

        return redirect('icecream')

    return redirect('cart')



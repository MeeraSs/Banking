from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Details,District,Branch,Material

# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('banking_app:register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user created")
                return redirect('banking_app:login')
        else:
            print("password mismatch")
            return redirect('banking_app:register')
        return redirect('/')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def details(request):
    districts = District.objects.all()
    branchess = Branch.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        mail_id = request.POST['mail_id']
        address = request.POST['address']
        district_id = request.POST['district']
        branchess = Branch.objects.filter(district_id=district_id)

        branch_id = request.POST.get('branch')
        account = request.POST['account']
        materials_provide = request.POST.getlist('materials_provide')


        detail_dist = Details(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            mail_id=mail_id,
            address=address,
            district_id=district_id,
            branch_id=branch_id,
            account=account,
        )


        detail_dist.save()


        material_objects = Material.objects.filter(name__in=materials_provide)
        detail_dist.materials_provide.set(material_objects)


        messages.info(request, "Application accepted")

    return render(request, 'details.html', {'districts': districts, 'branchess': branchess})




# def allDistricts(request):
#     # if dist_slug != None:
#     #     c_page = get_object_or_404(Category, slug=c_slug)
#     #     products_list=Product.objects.all().filter(category=c_page,available=True)
#     # else:
#     #     products_list=Product.objects.all().filter(available=True)
#
#     # ,{'category': c_page, 'products': products}
#     return render(request,'Details.html')
#
#
# def branchDistrictDetail(request):
#     # try:
#     #     product = Product.objects.get(category__slug=c_slug,slug=product_slug)
#     # except Exception as e:
#     #     raise e
#     # , {'product': product}
#     return render(request,'Details.html')
#

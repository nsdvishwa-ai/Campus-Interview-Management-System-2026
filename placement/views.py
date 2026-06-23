from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Company, LoginHistory
from .forms import StudentRegisterForm, StudentLoginForm, AdminLoginForm, CompanyForm
from django.db.models import Q


# Home Page
def home(request):
    return render(request, 'home.html')


# Student Register
def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_login')
    else:
        form = StudentRegisterForm()

    return render(request, 'student_register.html', {'form': form})


# Student Login
def student_login(request):
    message = ""

    if request.method == 'POST':
        reg_no = request.POST['reg_no']
        password = request.POST['password']

        try:
            student = Student.objects.get(
                reg_no=reg_no,
                password=password
            )

            request.session['student_id'] = student.id

            ip = request.META.get('REMOTE_ADDR')

            LoginHistory.objects.create(
                username=student.reg_no,
                ip_address=ip
            )

            return redirect('student_dashboard')

        except Student.DoesNotExist:
            message = "Invalid Register Number or Password"

    return render(
        request,
        'student_login.html',
        {'message': message}
    )


# Admin Login
def admin_login(request):
    message = ""

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if username == "admin" and password == "admin123":

            ip = request.META.get('REMOTE_ADDR')

            LoginHistory.objects.create(
                username=username,
                ip_address=ip
            )

            request.session['admin'] = username

            return redirect('admin_dashboard')

        else:
            message = (
                "Password may have been changed. "
                "Contact the administrator."
            )

    return render(
        request,
        'admin_login.html',
        {'message': message}
    )


# Student Dashboard
def student_dashboard(request):
    return render(request, 'student_dashboard.html')


# Admin Dashboard
def admin_dashboard(request):
    companies = Company.objects.all()

    return render(
        request,
        'admin_dashboard.html',
        {'companies': companies}
    )


# Search Company
def search_company(request):

    companies = Company.objects.all()

    if request.method == 'POST':

        keyword = request.POST['keyword']

        companies = Company.objects.filter(
            Q(company_name__icontains=keyword)
        )

    return render(
        request,
        'search_company.html',
        {'companies': companies}
    )


# Company Detail
def company_detail(request, company_id):

    company = get_object_or_404(
        Company,
        id=company_id
    )

    return render(
        request,
        'company_detail.html',
        {'company': company}
    )


# Add Company
def add_company(request):

    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('view_companies')

    else:
        form = CompanyForm()

    return render(
        request,
        'add_company.html',
        {'form': form}
    )


# Update Company
def update_company(request, company_id):

    company = get_object_or_404(
        Company,
        id=company_id
    )

    if request.method == 'POST':

        form = CompanyForm(
            request.POST,
            instance=company
        )

        if form.is_valid():
            form.save()
            return redirect('view_companies')

    else:
        form = CompanyForm(instance=company)

    return render(
        request,
        'update_company.html',
        {'form': form}
    )


# Delete Company
def delete_company(request, company_id):

    company = get_object_or_404(
        Company,
        id=company_id
    )

    if request.method == 'POST':
        company.delete()
        return redirect('view_companies')

    return render(
        request,
        'delete_company.html',
        {'company': company}
    )


# View Companies
def view_companies(request):

    companies = Company.objects.all()

    return render(
        request,
        'view_companies.html',
        {'companies': companies}
    )


# Eligibility Check
def eligibility(request):

    companies = Company.objects.all()

    return render(
        request,
        'eligibility.html',
        {'companies': companies}
    )


# Deadlines
def deadlines(request):

    companies = Company.objects.all().order_by('deadline')

    return render(
        request,
        'deadlines.html',
        {'companies': companies}
    )


# Sort By Package
def sort_package(request):

    companies = Company.objects.all().order_by('-package')

    return render(
        request,
        'sort_package.html',
        {'companies': companies}
    )


# Placement Report
def placement_report(request):

    total_companies = Company.objects.count()

    return render(
        request,
        'placement_report.html',
        {'total_companies': total_companies}
    )


# Logout
def logout_user(request):
    request.session.flush()
    return redirect('home')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Loan
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LoanForm
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt


def home(request):
    return render(request, 'loan/user/index.html')


def stats(request):
    # graph = plt.plot(5)
    # return graph
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now += delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def register_user(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
        if (u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = User.objects.get(
                email__iexact=request.POST.get('email'))
            p_form.save()
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        else:
            messages.error(request, f'Please correct the errors below.')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileUpdateForm()
    return render(request, 'loan/user/apply.html', {
        'u_form': u_form,
        'p_form': p_form
    })


@login_required
def dashboard(request):
    context = {
        'users': User.objects.order_by('-id')[:5]
    }
    return render(request, 'loan/dashboard/index.html', context)


@login_required
def apply_loan(request):
    return render(request, 'loan/dashboard/applyloan.html',)


@login_required
def loans(request):
    if request.method == 'POST':
        print(request.user.profile)
        loan_form = LoanForm(request.POST)
        if loan_form.is_valid():
            loan_form.profile_id = request.user.profile.id
            loan_form.purpose = 0
            loan_form.save()
            messages.success(
                request, f'Your application has been received succesfully')
            return redirect('dashboard-loans')
        else:
            messages.error(request, f'Please correct the errors below.')
    # show all loans if user is super admin otherwise only user loans
    if request.user.is_superuser:
        loans = Loan.objects.all()
    else:
        loans = Loan.objects.filter(profile_id=request.user.profile.id)
    context = {
        'loans': loans,
        'loan_form': LoanForm()
    }
    return render(request, 'loan/dashboard/loans.html', context)


@login_required
def delete_loan(request):
    Loan.objects.get(pk=request.POST.get('id')).delete()
    return redirect('dashboard-loans')


@login_required
def users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'loan/dashboard/users.html', context)

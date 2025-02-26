from django.shortcuts import render

def home(request):
    return render(request, 'mainapp/home.html')

def about(request):
    return render(request, 'mainapp/about.html')

def contact(request):
    return render(request, 'mainapp/contact.html')
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import OrphanKid, OldAgeHome, AccidentSupport, EducationSupport
from .forms import OrphanKidForm, OldAgeHomeForm, AccidentSupportForm, EducationSupportForm

# Admin Check Function
def admin_required(user):
    return user.is_superuser

# Admin Dashboard (Restricted)
@login_required
@user_passes_test(admin_required)
def admin_dashboard(request):
    return render(request, 'mainapp/admin_dashboard.html')

# Orphan Kids CRUD
@login_required
@user_passes_test(admin_required)
def orphan_list(request):
    orphans = OrphanKid.objects.all()
    return render(request, 'mainapp/orphan_list.html', {'orphans': orphans})

@login_required
@user_passes_test(admin_required)
def orphan_create(request):
    if request.method == 'POST':
        form = OrphanKidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orphan_list')
    else:
        form = OrphanKidForm()
    return render(request, 'mainapp/orphan_form.html', {'form': form})

@login_required
@user_passes_test(admin_required)
def orphan_update(request, id):
    orphan = get_object_or_404(OrphanKid, id=id)
    if request.method == 'POST':
        form = OrphanKidForm(request.POST, instance=orphan)
        if form.is_valid():
            form.save()
            return redirect('orphan_list')
    else:
        form = OrphanKidForm(instance=orphan)
    return render(request, 'mainapp/orphan_form.html', {'form': form})

@login_required
@user_passes_test(admin_required)
def orphan_delete(request, id):
    orphan = get_object_or_404(OrphanKid, id=id)
    orphan.delete()
    return redirect('orphan_list')

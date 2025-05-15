from django.shortcuts import render,redirect
from adminPanel.models import Admin



# Create your views here.
def admin_dashboard(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)
    return render(request, 'admin_dashboard.html', {'admin': admin})

def admin_profile(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')  # Redirect to login if not authenticated

    try:
        admin = Admin.objects.get(id=admin_id)
    except admin.DoesNotExist:
        return redirect('login')

    return render(request, 'admin_profile.html', {'admin': admin})

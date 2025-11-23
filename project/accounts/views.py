from django.shortcuts import render,redirect
from .forms import*
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def SignupView(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignUpForm()
        
    return render(request, 'signup.html', {'form': form})
            
        
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on user type
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            elif user.user_type == 'doctor':
                return redirect('doctor_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})


@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('login')
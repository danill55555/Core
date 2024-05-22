from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(reqeust, 'registrations.html', {'form', form})

def logout_view(request):
    logout(request)
    return redirect('home')

def login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_date['username'])
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                return messages('Ошибка')
        else:
            return messages('Ошибка')
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})





def applications(request):
    if request.user.is_authenticated:
        applications = Application.objects.filter(user=request.user)
        return render(request, 'applications.html', {'applictions': applications})
    else:
        return render(request, 'applications.html')
# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from .forms import CustomUserCreationForm

# def register_user(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('browse_jobs')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browse_jobs')  # Redirect to the jobs app's browse page
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

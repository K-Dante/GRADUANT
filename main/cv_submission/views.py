from django.shortcuts import render, redirect
from .forms import CVForm

def submit_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cv_submission:success')
    else:
        form = CVForm()
    return render(request, 'cv_submission/submit_cv.html', {'form': form})

def submission_success(request):
    return render(request, 'cv_submission/submission_success.html')
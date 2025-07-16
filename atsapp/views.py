from django.shortcuts import redirect, render
from django.http import HttpResponse
from atsapp.models import resume_score
from ml_model.pdf_text import pdf_to_text
from ml_model.transformer import get_embeded
from ml_model.comparing import compute_similarity

# Create your views here.


def upload_resume_view(request):
    score = request.GET.get('score')
    offset = request.GET.get('offset')
    data = resume_score.objects.all()
    
    if request.method == 'POST':
        resume_file = request.FILES.get('resume')
        job_desc = request.POST.get('description')

        if not resume_file or not job_desc:
            return HttpResponse('please upload both resume and job description')
        
        try:
            resume_text = pdf_to_text(resume_file)

            resume_vec = get_embeded(resume_text)
            desc_vec = get_embeded(job_desc)

            # comparing the score 

            score = compute_similarity(resume_vec,desc_vec)
            # score_2dp = float(f"{score_raw:.2f}")
            
            

            # storing database
            obj = resume_score()
            obj.score = score
            obj.resume = resume_file
            obj.save()

            circumference = 2 * 3.1416 * 54  # r = 54
            offset = circumference * (1 - score / 100)
            return redirect(f'/?score={score:.2f}&offset={offset}')
           

           
        except Exception as e:
            return HttpResponse(f'error due to problem in your uploaded file please load a valid file')
    return render(request,'main.html',{'data':data,'score':score,'offset':offset})


def delete(request,id):
    resume_score.objects.get(id=id).delete()
    return redirect('/')


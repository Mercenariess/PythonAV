from django.shortcuts import render,HttpResponse

# Create your views here.


def bam_video(request):
    return render(request,"upload_video.html")

def bam_text(request):
    return  render(request,"text_editor.html")

def bam_personal(request):
    return render(request,"personal_data.html")
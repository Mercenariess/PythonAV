
from django.urls import path,re_path
from bam.views import bam_video
from bam.views import bam_text
from bam.views import bam_personal

urlpatterns = [
    re_path("video/$",bam_video),
    re_path("text/$",bam_text),
    re_path("personal/$",bam_personal),
]

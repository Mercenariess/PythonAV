from django.db import models


# Create your models here.

# 后台管理账号
class BamForm(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)


#  文章
class Article(models.Model):
    title = models.CharField(max_length=60)
    contend = models.TextField()
    article_img = models.ImageField(upload_to="img")


# 文章分类
class ArticleClassification(models.Model):
    article_classification_title = models.CharField(max_length=50)
    article = models.ManyToManyField(to="Article")


# 个人信息
class PersonalData(models.Model):
    name = models.CharField(max_length=20)
    personal_introduction = models.CharField(max_length=300)
    personal_photo = models.ImageField(upload_to="photo")
    personal_video = models.URLField(max_length=700)


# 视频
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField(max_length=(700))


# 建议
class Advice(models.Model):
    name = models.CharField(max_length=20)
    personal_advice = models.TextField()


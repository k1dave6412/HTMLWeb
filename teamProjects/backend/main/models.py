from django.db import models

# Create your models here.

class Theater(models.Model):
	theater_name = models.CharField(max_length=30)
	theater_phone = models.CharField(max_length=15, blank=True)
	theater_loc = models.CharField(max_length=100, blank=True)
	theater_id = models.IntegerField()
	theater_url = models.CharField(max_length=200, blank=True)
	
	def __str__(self):
		return self.theater_name

# 電影名稱=介紹=演員=導演=圖片url=縮圖url
class Movie(models.Model):
	movie_n = models.CharField(max_length=100, blank=True)
	movie_info = models.CharField(max_length=300, blank=True)
	movie_actor = models.CharField(max_length=100, blank=True)
	movie_director = models.CharField(max_length=100, blank=True)
	movie_pic_loc = models.CharField(max_length=200, blank=True)
	movie_thum_loc = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.movie_n

# 電影名稱=廳=日期=時間
class MoiveTimeTable(models.Model):
	movie_name = models.CharField(max_length=100)   
	movie_loc = models.CharField(max_length=100)
	movie_date = models.CharField(max_length=100, blank=True)
	movie_time = models.CharField(max_length=100, blank=True)
	movie_info = models.ForeignKey(Movie, null=True)
	theater = models.ForeignKey(Theater, null=True)

	def __str__(self):
		return self.theater.__str__() + " " +self.movie_name + "  " + self.movie_loc + "  " + self.movie_time

class Store(models.Model):
	store_name = models.CharField(max_length=100)
	stroe_loc = models.CharField(max_length=100)
	store_time  = models.CharField(max_length=10) 
	store_info = models.CharField(max_length=300, blank=True) 
	store_img = models.CharField(max_length=300, blank=True) 
	store_cata = models.CharField(max_length=30, blank=True) 
	theater = models.ForeignKey(Theater, null=True)


	def __str__(self):
		return self.store_name















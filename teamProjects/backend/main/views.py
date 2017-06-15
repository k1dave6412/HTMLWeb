from django.shortcuts import render, redirect
from django.http import HttpResponse
from pythonbat.Crawler import Crawler
from main.models import MoiveTimeTable, Movie, Theater, Store
from datetime import datetime
import logging


# Create your views here.
	

def index(request):
	theater_list = Theater.objects.all().order_by('theater_loc')

	for t in theater_list:
		movie_list = MoiveTimeTable.objects.filter(theater=t)
		movie_img = []
		movie_img_src = []

		for m in movie_list:
			if(movie_img.count(m.movie_name) == 0):
				movie_img.append(m.movie_name)

		for imgg in movie_img:
			mc = Movie.objects.filter(movie_n=imgg)
			movie_img_src.append(mc[0].movie_thum_loc)

		t.img = movie_img_src

	return render(request, 'index.html',{
		'theater_list':theater_list,
		})

def timetable(request, id, name):
	t = Theater.objects.filter(theater_id=id)
	movie = MoiveTimeTable.objects.filter(theater=t[0]).order_by('movie_name')
	movie_list = []
	movie_list_time = []

	
	# logger = logging.getLogger('sourceDns.webdns.views')

	for mlist in movie:
		
		
		if ((movie_list.count(mlist.movie_name)==0 and movie_list.count(mlist.movie_loc)==0)or movie_list.count(mlist.movie_loc)==0):
			movie_list_time.append(movie_list)
			movie_list = []
			movie_list.append(mlist.movie_name)
			movie_list.append(mlist.movie_loc)
			
		movie_list.append(mlist.movie_time)

	movie_list_time.append(movie_list)
	del movie_list_time[0]
	# logger.debug(movie_list_time)



	return render(request, 'timetable.html',{
		'movie_time':movie_list_time,
		'id':id,
		'name':name,
		})

def contact(request):
	return render(request, 'contact.html')

def abouts(request, tid, times, moviename):
	ntime = datetime.now()
	compate_min = ntime.hour * 60 +ntime.minute
	nt = times.split(':')
	timee = int(nt[0])*60+int(nt[1])
	mini =  timee - compate_min

	numlist = [1,1,1]


	t = Theater.objects.filter(theater_id=tid)
	store_list = Store.objects.filter(theater=t[0]).order_by('store_cata')
	store_list_one = []
	store_list_two = []
	store_list_three = []

	for s in store_list:
		if (int(s.store_time)<mini):

			if (s.store_cata == "路邊小吃"):
				numlist[0]+=1
				store_list_one.append(s)
			if (s.store_cata == "逛街搞文藝"):
				numlist[1]+=1
				store_list_two.append(s)
			if (s.store_cata == "餐廳"):
				numlist[2]+=1
				store_list_three.append(s)

	mov = Movie.objects.filter(movie_n=moviename)
	if (mov == ""):
		mov = Movie.objects.filter(movie_n="加勒比海盜")


	
	return render(request, 'about.html',{
		'number':numlist,
		's1':store_list_one,
		's2':store_list_two,
		's3':store_list_three,
		'movie':mov,
		})

def about(request):
	return render(request, 'about.html')

def re(request):

	c = Crawler();
	trash = MoiveTimeTable.objects.all()
	trash.delete()

	theaterlist = [2,4,8,6,53,9,5,3,7]
	for lt in theaterlist:
		data = c.movie_info(lt)


		for d in data:
			div = d.split('=')
			
			if Movie.objects.filter(movie_n=div[0]).count() == 0:
				table = Movie.objects.create(movie_n=div[0],
											 movie_info=div[1],
											 movie_actor=div[2],
											 movie_director=div[3],
											 movie_pic_loc=div[4],
											 movie_thum_loc=div[5]
											 )
				table.save()

		movies = c.movie(lt)
		t = Theater.objects.get(theater_id=lt)

		for m in movies:
			divv = m.split('=')
			movie = Movie.objects.get(movie_n=divv[0])
			table2 = MoiveTimeTable.objects.create(movie_name=divv[0],
												   movie_loc=divv[1],
												   movie_date=divv[2],
												   movie_time=divv[3],
												   movie_info=movie,
											       theater=t)
		table2.save()

	return redirect('index')

import json
import requests
import time as t
from datetime import datetime
import re



class Crawler(object):
    #movie in theater
#   2  欣欣秀泰
#   4  今日秀泰
#   8  東南亞秀泰
#   6  板橋秀泰
#   53 台中站前秀泰
#   9  嘉義秀泰
#   5  基隆秀泰
#   3  花蓮秀泰
#   7  台東秀泰

    def filter_tags(self, htmlstr):  
        re_br=re.compile('<br\s*?/?>')
        s=re_br.sub('\n',htmlstr)
        blank_line=re.compile('\n+')  
        s=blank_line.sub('\n',s)  
        s=re.sub('<[^<]+?>', '', s)
        return s  

    def movie(self, theater):
        self.data = []

        now = t.strftime("%Y-%m-%d")

        ntime = datetime.now()
        res = requests.get("https://api.showtimes.com.tw/1/events/listForCorporation/"+str(theater)+"?date="+now+"&limit=2000")
        doc = json.loads(res.text)

        for event in doc['payload']['events']:
            for program in doc['payload']['programs']:
                if(str(event['programId']) == str(program['id'])):
                    name=str(program['name'])
            date=str(event['startedAt'])[5:10]
            hour=int(str(event['startedAt'])[11:13])+8
            m=str(event['startedAt'])[14:16]

            time=''
            
            if(hour>24):
                hour-=24
            if(hour==24):
                hour=0
            if(hour<10):
                time+='0'


            time+=str(hour)
            time+=':'
            time+=m

            for venue in doc['payload']['venues']:
                if(str(event['venueId'])==str(venue['id'])):
                    room=str(venue['room'])

            item=''
            item+=name
            item+='='
            item+=room
            item+='='
            item+=date
            item+='='
            item+=time

            if(hour>ntime.hour or (hour==ntime.hour and int(m) > ntime.minute) or hour==0):
                self.data.append(item)
            # self.data.append(item)
            

        self.data.sort()

        return self.data

    def movie_info(self, theater):

        now = t.strftime("%Y-%m-%d")
        res = requests.get("https://api.showtimes.com.tw/1/events/listForCorporation/"+str(theater)+"?date="+now+"&limit=2000")
        doc = json.loads(res.text)

        self.data=[]

        for program in doc['payload']['programs']:
            name=str(program['name'])
            descriptions=''
            descriptions+=str(program['description'])
            
            authors=''
            for author in program['meta']['authors']:
                authors+=(str(author))
            director=''
            for directors in program['meta']['directors']:
                director+=(str(directors))
            image_url=str(program['coverImagePortrait']['url'])
            thumb=str(program['coverImagePortrait']['thumb'])
            
            item=''
            item+=name
            item+='='
            item+=descriptions
            item+='='
            item+=authors
            item+='='
            item+=director
            item+='='
            item+=image_url
            item+='='
            item+=thumb

            item = self.filter_tags(item)
            self.data.append(item)

        return self.data
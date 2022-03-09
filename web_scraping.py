from bs4 import BeautifulSoup
import requests
import json
 
url="https://www.imdb.com/india/top-rated-indian-movies/"
var=requests.get(url)
var2=BeautifulSoup(var.text,'html.parser')

def scrap_list():
    main_div=var2.find('div',class_='lister')
    body=main_div.find('tbody',class_='lister-list')
    trs=body.find_all('tr')

    
    list=[]
    position=0
    for tr in trs:
        position+=1
        number={}
        title=tr.find('td',class_="titleColumn").a.get_text()
        
        year=tr.find('td',class_="titleColumn").span.get_text()[1:5]
        
        rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        
        movie_url=tr.find('td',class_="titleColumn").a["href"]
        link = "https://www.imdb.com" + movie_url
        
        
        new_list={"position":position,"title":title,"year":year,"rating":rating,"link":link}
        list.append(new_list)
        with open("task_1.json","w")as k:
            json.dump(list,k,indent=4)
    return(list)
scrap_list()





    

# scrap_list()




        


        


    






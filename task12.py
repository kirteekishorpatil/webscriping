# from bs4 import BeautifulSoup
# import requests
# import json
# from task1 import adventure_movie
# data=adventure_movie()
# def main_fun(data):
#     def movie_cast(link,movie_name):
#         d1={}
#         link_data=requests.get(link)
#         soup=BeautifulSoup(link_data.text,'html.parser')
#         d1["Name"]=movie_name
#         table=soup.find('div',class_="castSection")
#         # print(table)
#         celebrity_link=table.find_all('a',class_="unstyled articleLink")
#         # print(celebrity_link)
#         celebrity_name=table.find_all('span',class_='characters subtle smaller')

#         d1={}
#         dict={}
#         movie_details=[]
#         for i in range(len(celebrity_link)):
#             Name=celebrity_name[i]['title']
#             link="https://www.rottentomatoes.com/"+celebrity_link[i]['href']
#             cast_id=""
#             id=len(link)-1

#             while id>=0:
#                 if link[id]!="/":
#                     cast_id+=link[id]
#                 else:
#                     break
#                 id=id-1
#             cast_id=list(cast_id)
#             cast_id.reverse()
#             cast_id=''.join(cast_id)
#             print(cast_id)
#             d1[cast_id]=Name
#             dict[movie_name]==d1

#             for j in data:
#                 for p in j:
#                     movie_name=j["movie_name"]
#                     if p=="movie URL":
#                         movie_dic=movie_cast(j[p],movie_name)
#                         movie_details.append(movie_dic)

#         with open("task_12.json","w")as file1:
#             json.dump(movie_details,file1,indent=4)
            
            
            
#         return movie_details
#         # with open("task_12.json","w")as file1:
#         #     json.dump(dict,file1,indent=4)

    
# var1=main_fun(data)
     
from bs4 import BeautifulSoup
import json
import requests



def movie_cast(movie_url):
    cast_list=[]
    data=requests.get(movie_url)
    soup=BeautifulSoup(data.text,"html.parser")
    main=soup.find_all("div",class_="panel-body content_body")
    section=main[1].find("div",class_="castSection")
    all=section.find_all("div",class_="cast-item")
    for i in all:
        cast_list.append(i.find("span")["title"])
    # return cast_list
    with open("CastData.json","w") as f:
        json.dump(cast_list,f,indent=3)
    return cast_list    

data=movie_cast("https://www.rottentomatoes.com/m/black_panther_2018")




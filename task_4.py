from bs4 import BeautifulSoup
import requests
import json

movie_details=[]
def scrap_movie_details(link):
    d1={}
    link_data=requests.get(link)
    soup=BeautifulSoup(link_data.text,'html.parser')
    d1["name"]="Black panther"
    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    d1["Bio"]=movie_bio
    title=soup.find_all("div",class_="meta-label subtle")
    value=soup.find_all("div",class_="meta-value")

    for i in range(len(title)):
        d1[str(title[i].get_text().strip())[:-1]]=value[i].get_text().strip()
    movie_details.append(d1)
    with open("scrap_movie.json","w")as file:
        json.dump(movie_details,file,indent=4)

        

scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")

    
# # from task1 import adventure_movie
# # import json
# from bs4 import BeautifulSoup
# import json
# import requests
# movie_details=[]
# def scrap_movie_details(link):
#     d1={}
#     link_data=requests.get(link)
#     soup=BeautifulSoup(link_data.text,'html.parser')
#     movie_find_2=soup.find("ul",class_="content-meta info")
#     movie_find_3=movie_find_2.find_all("li",class_="meta-row clearfix")
#     my_dict={}
#     for i in movie_find_3:
#         alldata=i.find("div",class_="meta-label subtle").get_text().strip()
#         allvalue=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
#         my_dict.update({alldata:allvalue})
#     movie_details.append(my_dict)
# # scrapped=adventure_movie()
# # def get_movie_list_details(movies): 
# #     j=0
# # list4=[]
# #     while j<len(movies):
#         # newurl=movies[j]["movie URL"]
#         # url=newurl
#         # x=requests.get(url)
#         # soup=BeautifulSoup(x.text,"html.parser")
#         # movie_find_2=soup.find("ul",class_="content-meta info")
#         # movie_find_3=movie_find_2.find_all("li",class_="meta-row clearfix")
#         # my_dict={}
#         # for i in movie_find_3:
#         #     alldata=i.find("div",class_="meta-label subtle").get_text().strip()
#         #     allvalue=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
#         #     my_dict.update({alldata:allvalue})
#         # list4.append(my_dict)
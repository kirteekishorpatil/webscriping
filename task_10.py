from bs4 import BeautifulSoup
import requests
import json
with open("task_5.json","r") as f:  
    data1=json.load(f)

def language_and_directores(movie_list):
    directores_dic={}
    for movie in movie_list:
        for director in movie:
            if director=="Director":
                directores_dic[movie[director]]={}
    for i in range(len(movie_list)):
        for director in directores_dic:
            if director in movie_list[i]["Director"]:
                for language in movie_list[i]:
                    if language=="Original Language":
                        a=movie_list[i][language]
                        directores_dic[director][a]=0
    for i in range(len(movie_list)):
        for director in directores_dic:
            if director in movie_list[i]["Director"]:
                for language in movie_list[i]:
                    if language=="Original Language":
                        for l in directores_dic[director]:
                            directores_dic[director][l]+=1
    return directores_dic

directore_language=language_and_directores(data1)
with open("directore_by_language.json","w")as f:
    json.dump(directore_language,f,indent=4)
print(directore_language)
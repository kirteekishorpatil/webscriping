from web_scraping import scrap_list
import json 

screpped=scrap_list()
def scrape_top_list_1(movie):
    years=[]
    for i in movie:
        year =i["year"]
        if year not in years:
            years.append(year)
    movie_dic = {i:[]for i in years}
    for i in movie:
        year = i["year"]
        for x in movie_dic:
            if str(x)==str(year):
                movie_dic[x].append(i)
        with open("task2.json","w") as file:
            json.dump(movie_dic,file,indent=4)
    return movie_dic
scrape_top_list_1(screpped)









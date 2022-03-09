from task1 import adventure_movie
import json 

screpped=adventure_movie()
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
        with open("all_movie_data.json","w") as file:
            json.dump(movie_dic,file,indent=4)
    return movie_dic
scrape_top_list_1(screpped)
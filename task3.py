from task1 import adventure_movie
import json
name=adventure_movie()
def group_by_decade(movise):
    movisedec={}
    list1=[]
    for index in movise:
        mod=index["year"]%10
        decode=index["year"]-mod
        if decode not in list1:
            list1.append(decode)  
    list1.sort()
    for i in list1:
        movise_list=[]
        for x in movise:
            if x["year"]>=i and x["year"]<=i+10:
                movise_list.append(x)
                movisedec[i]=movise_list
                with open("naini.json","w")as file:
                    json.dump(movisedec,file,indent=3)                
group_by_decade(name)
























































# from task1 import adventure_movie
# from task_2 import scrape_top_list_1
# import json


# list=adventure_movie()
# dec=scrape_top_list_1(list)
# # dec=group_by_year()
# def group_by_decade(movie):
#     moviesdic={}
#     list1=[]
#     for i in movie:
#         mod=i%10
#         dec=i-mod
#         if dec not in list1:
#             list1.append(dec)
#         list1.sort
#     for i in list1:
#         moviesdic[i]=[]
#     for i in moviesdic:
#         dec=i+9
#         for x in movie:
#             if x<=dec and x>=i:
#                 for j in movie[x]:
#                     moviesdic[i].append(j)
#                     with open("n.json","w")as _data:
#                         json.dump(moviesdic,_data,indent=4)
#     # return moviesdic
# var2=group_by_decade(dec)





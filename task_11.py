
import json
def  movie_directors():
    file2=open("my_file_5.json","r")
    p=json.load(file2)
    list=[]
    list2=[]
    list3=[]
    for i in p:
        m=i["Genre:"].split()
        for i in m:
            if i[-1]==",":
                i=i[:-1]
                # print(i)
                
                list3.append(i)
        
    # print(list3)
       
    for i in list3:

        if i not in list:
            if len(i)>1:
                list.append(i)
    # print(list)
    dict={}
    for k in list:
        i=0
        count=0
        while i<len(list3):
            if k==list3[i]:
                count+=1
            i+=1
        dict.update({k:count})
    list.append(dict)
    print(dict)
    with open("task_11.json","w")as file:
        json.dump(dict,file,indent=4)
    return dict
movie_directors()


       




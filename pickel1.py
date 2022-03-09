from bs4 import BeautifulSoup
import requests
import json
def scrap_pickel():
    pickel_url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    pickel_api=requests.get(pickel_url)
    htmlcontent=pickel_api.content
    # print(htmlcontent)
    soup=BeautifulSoup(htmlcontent,"html.parser")
    # print(soup)
    pickel_tag=soup.find("div",class_="_3RA-")
    # print(pickel_tag)
    main=pickel_tag.find_all("div",class_="_1fje") 


    list=[]
    position=0
    for div in main:
        all=div.find_all("div",class_="_2i1r")
        for i in all:
            position+=1
        
            pickel_name=i.find("div",class_="_2PhD").text

            pickel_price=i.find("div",class_="_1kMS").text
            
            link=i.find("a",class_="_8vVO")["href"]
            pickel_link="https://paytmmall.com/"+link
            

            a=i.find("div",class_="_3nWP")
            for i in a:
                pickle_image=(i['src'])
            # print(image_link)
            new_list={"position":position,"pickel_name":pickel_name,"pickel_price":pickel_price,"pickel_l":pickel_link,"pickle_image":pickle_image}
            list.append(new_list)
            with open("task_pickel.json","w")as k:
                json.dump(list,k,indent=4)
    return(list)
    
    
scrap_pickel() 
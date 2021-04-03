#IMPORT IMPORTANT PACKAGE THAT ARE USING IN THE PROGRAM 
from plyer import notification #USED TO SHOW THE NOTIFICATION LOG OR BLOCK 
#ALL THESE PACKAGE USED TO DO WEB SCRAPPING THE DATA FROM THE SOURCE WEBSITE
import requests
from bs4 import BeautifulSoup
import time 

#FUNCTION THAT SHOW THE POP UP MESSAGE OR THE NOTIFICATION
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=5
    )

#FUNCTION WHICH REQUEST TO THE WEBSITE THAT URL IS GIVEN
def getData(url):
    r=requests.get(url)
    return r.text

#MAIN FUNCTION THAT PERFORM OPERATIONS AND CALL THE ABOVE FUNCTION TO PERFORM THEIR RESPECTIVE WORK
if __name__=="__main__":
    myHtmlData = getData("https://www.goodreturns.in/gold-rates/")
    soup=BeautifulSoup(myHtmlData,"html.parser")
    tableData=soup.find_all('div',{'class':'gold_silver_table'})
    useData=tableData[2].text
    useData=useData.split()
    useData=useData[9:]
    for i in useData:
        if i == '₹':
            useData.remove(i)
    for i in range(0,72,3):
        nTitle=" Today Gold Price"
        nText=f"{useData[i]} \n 22 Carat Gold Price:{useData[i+1]} \n 24 Carat Gold Price:{useData[i+2]}"
        notifyMe(nTitle,nText)
        #print(i)
        time.sleep(2)
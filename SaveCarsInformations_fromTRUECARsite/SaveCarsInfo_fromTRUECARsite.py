import requests
import re
import mysql.connector
from bs4 import BeautifulSoup
cnx = mysql.connector.connect(user='amir',password='1234',host='127.0.0.1',database='car') # table mashin (name,price,miles)
mycursor = cnx.cursor()
carname = input("enter car name : ")
link = "https://www.truecar.com/used-cars-for-sale/listings/carname/?sort[]=best_match"
d = re.sub('carname',carname,link)
a = requests.get(d)
s = BeautifulSoup(a.text,'html.parser')
div1 = s.find_all('li',attrs={'class':'margin-top-3 d-flex flex-grow col-md-6 col-xl-4'}) #find all cars

if (len(div1)>=20):
    for i in range(0,20):
        x = div1[i]
        car_name = x.find('span','vehicle-header-make-model text-truncate')
        car_price = x.find('div','heading-3 margin-y-1 font-weight-bold')
        p = re.sub(',',"",car_price.text) 
        car_miles = x.find('div',attrs={'data-test':'vehicleMileage'})
        m = re.sub(',',"",car_miles.text) 
        mycursor.execute("INSERT INTO mashin VALUES (\'%s\',\'%s\',\'%s\')"%(car_name.text,p,m))
        cnx.commit()
        print(mycursor.rowcount, "was inserted.")
elif(len(div1)==0):
    print ("nothing")
else:
    for i in range(0,len(div1)):
        x = div1[i]
        car_name = x.find('span','vehicle-header-make-model text-truncate')
        car_price = x.find('div','heading-3 margin-y-1 font-weight-bold')
        p = re.sub(',',"",car_price.text) 
        car_miles = x.find('div',attrs={'data-test':'vehicleMileage'})
        m = re.sub(',',"",car_miles.text) 
        mycursor.execute("INSERT INTO mashin VALUES (\'%s\',\'%s\',\'%s\')"%(car_name.text,p,m))
        cnx.commit()
        print(mycursor.rowcount, "was inserted.")
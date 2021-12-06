from os import stat
from flask import Flask,render_template,request,jsonify,url_for
import json,requests


app = Flask(__name__,static_folder="static")
summary_url_temp = "https://api.covid19api.com/summary" #api raw şeklinde 



@app.route("/",methods=["GET"])
def home():
    response = requests.get(summary_url_temp) # request sonrası bir response dönüyor 

    if response.ok:
        resp_data = response.json() #responsu json formatına çevirdi
        message = resp_data["Message"]

        if(message != ""): #api page yükleniyor 
            return str(message) + "!! Please refresh the page..."
        
        else:
            Global = resp_data["Global"] #json beautifer da bak. Tüm global listesini aldık yani elimizde yeni bir liste var
            new_deaths = Global["NewDeaths"]
            total_deaths = Global["TotalDeaths"]
            new_cases = Global["NewConfirmed"]
            total_cases = Global["TotalConfirmed"]
            new_recovered = Global["NewRecovered"]
            total_recovered = Global["TotalRecovered"]
            updated = Global["Date"]

            

            return render_template("index.html",nd_n=new_deaths,td_n=total_deaths,nc_n=new_cases,nr_n=new_recovered,tc_n=total_cases,tr_n=total_recovered,date=updated)








    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
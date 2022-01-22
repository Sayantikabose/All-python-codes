import smtplib
import requests

apikey="ada4dc2f2cc7bcb041f832f0526e674d" 

URL="https://api.openweathermap.org/data/2.5/onecall"
PARAMS={
    "lat":36.27,
    "lon":167.10,
    "appid": apikey,
    "exclude":"current,minutely,daily"
}
connection=smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user="sayantikahacky@gmail.com",password="abcd1234()")
r=requests.get(url=URL, params=PARAMS)
data=r.json()
hourly_data = []
# weather_code = data["hourly"][:12]
for i in range(0, 12):
    weather_code = data["hourly"][i]["weather"][0]["id"]
    hourly_data.append(weather_code) 
print(hourly_data)
is_raining = False
for data in hourly_data:
    if data < 700:
        is_raining = True
if is_raining:
    connection.sendmail(from_addr="sayantikahacky@gmail.com",to_addrs="sayantikamimibose@gmail.com",msg="Subject:Rain alert \n\nIt is going to rain Bring your umbrella")
else:
    print("You don't need an umbrella")
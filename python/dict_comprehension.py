weather={
    "Monday" : 12,
    "Tuesday" :23,
    "Wednesday" : 10,
    "Thrusday" :19,
    "Friday" : 30,
    "Saturday" :22,
    "Sunday" : 18,

} 
new={wea:(num*(9/5)+32) for(wea,num) in weather.items()}
print(new)
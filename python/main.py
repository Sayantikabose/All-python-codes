
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 

my_Coffee=CoffeeMaker()
my_menu =Menu()
my_Money=MoneyMachine()

is_on=True




while(is_on):
    options=my_menu.get_items() 
    choice=input("What do you want")
    if(choice=="off"):
        is_on=False
    elif(choice=="report"):
        report_item2=my_Money.report() 
        report_item1=my_Coffee.report()
    else:
        drink=my_menu.find_drink(choice)
        if(my_Coffee.is_resource_sufficient(drink)) :
            if(my_Money.make_payment(drink.cost)):
                my_Coffee.make_coffee(drink)


 

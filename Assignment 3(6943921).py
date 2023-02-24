#script for sales of available  cars 
#all available car prices
vitz=50000
yaris=25000 
camry=30000
prius=55000
rav4=54700
hilux=60000
highlander=80000
fortuner=85000
avalon=100000
mirai= 75000

civic=700000
accord=150000
fit=330000
city=500000
amaze=600000
passport=800000
pilot=670000
hatch=900000
integra=650000
clarity=400000

juke=700000
murano=65000
sentra=55000
rogue=30000
maxima=200000
titan=640000
versa=80000
patrol=30000
frontier=45000
cube=50000

from tabulate import tabulate

print('Car brands available')
print('(1)Toyota \
      (2)Honda \
      (3)Nissan ')
    
    
brand=int(input('Specify car Brand using interger attached: '))   


if brand==1:
    print('These are the TOYOTA Cars Available')
    data = [["vitz ", 50000], 
        ["yaris", 25000], 
        ["camry", 30000],
        ["prius", 55000],
        ["rav4", 54700],
        ["hilux", 60000],
        ["highlander", 80000],
        ["fortuner", 85000],
        ["avalon", 100000],
        ["mirai", 750000]]
    col_names = ["Cars", "Prices"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    totype=str(input('Specify Toyota using : '))
    if totype=='vitz':
     print('this car costs {}'.format(vitz))
    elif totype=='yaris':
      print('this car costs {}'.format(yaris))
    elif totype=='camry':
        print('this car costs {}'.format(camry))
    elif totype=='prius':
        print('this car costs {}'.format(prius))
    elif totype=='rav4':
            print('this car costs {}'.format(rav4))
    elif totype=='hilux':
        print('this car costs {}'.format(hilux))
    elif totype=='highlander':
        print('this car costs {}'.format(highlander))
    elif totype=='fortuner':
            print('this car costs {}'.format(fortuner))
    elif totype=='avalon':
        print('this car costs {}'.format(avalon))
    elif totype=='mirai':
        print('this car costs {}'.format(mirai))


elif brand==2:
    print('These are the Honda Cars Available')
    data = [["civic",700000 ], 
        ["accord",150000 ], 
        ["fit",330000], 
        ["city", 500000],
        ["amaze", 600000],
        ["passport", 800000],
        ["pilot", 670000],
        ["hatch", 900000],
        ["integra", 650000],
        ["clarity", 400000]]
    col_names = ["Cars", "Prices"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    hontype=str(input('Specify Honda unit : '))
    if hontype=='civic':
        print('this car costs {}'.format(civic))
    elif hontype=='accord':
        print('this car costs {}'.format(accord))
    elif hontype=='fit':
        print('this car costs {}'.format(fit))
    elif hontype=='city':
        print('this car costs {}'.format(city))
    elif hontype=='amaze':
        print('this car costs {}'.format(amaze))
    elif hontype=='passport':
        print('this car costs {}'.format(passport))
    elif hontype=='pilot':
        print('this car costs {}'.format(pilot))
    elif hontype=='hatch':
        print('this car costs {}'.format(hatch))
    elif hontype=='integra':
        print('this car costs {}'.format(integra))
    elif hontype=='clarity':
        print('this car costs {}'.format(clarity))
        
elif brand==3:
    print('These are the Nissan Cars Available')
    data = [["juke", 700000], 
        ["murano", 65000], 
        ["sentra", 55000], 
        ["rogue", 30000],
        ["maxima", 200000],
        ["titan", 640000],
        ["versa", 80000],
        ["patrol", 30000],
        ["frontier", 45000],
        ["cube", 50000]]
    col_names = ["Cars", "Prices"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    nistype=str(input('Specify Nissan unit : '))
    if nistype=='juke':
        print('this car costs {}'.format(juke))
    elif nistype=='murano':
        print('this car costs {}'.format(murano))
    elif nistype=='sentra':
        print('this car costs {}'.format(sentra))
    elif nistype=='rogue':
        print('this car costs {}'.format(rogue))
    elif nistype=='maxima':
        print('this car costs {}'.format(maxima))
    elif nistype=='titan':
        print('this car costs {}'.format(titan))
    elif nistype=='versa':
        print('this car costs {}'.format(versa))
    elif nistype=='patrol':
        print('this car costs {}'.format(versa))
    elif nistype=='frontier':
        print('this car costs {}'.format(frontier))
    elif nistype=='cube':
        print('this car costs {}'.format(cube))    

#https://github.com/Tonyame10

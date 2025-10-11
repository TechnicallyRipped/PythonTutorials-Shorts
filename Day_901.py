





def introduce(Name,Age,Pet=None):
    print(f'{Name} (Age {Age}) has a {Pet}.')

x = {'Name':'Joe','Age':30}

introduce(**x)







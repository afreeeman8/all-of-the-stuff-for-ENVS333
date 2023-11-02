def cflat():
    
    directionlat = float(input("Enter the direction lat(1 for N/E, -1 for S/W): "))
    degreelat = float(input("Enter the degrees lat.: "))
    minutelat = float(input("Enter the minutes lat.: "))
    secondslat = float(input("Enter the seconds lat.: "))
    convertedlat = directionlat*(degreelat + (minutelat + secondslat/60)/60)
    
    return convertedlat


def cflong():
    
    directionlong = float(input("Enter the direction long.(1 for N/E, -1 for S/W): "))
    degreelong = float(input("Enter the degrees long.: "))
    minutelong = float(input("Enter the minutes long.: "))
    secondslong = float(input("Enter the seconds long.: "))
    convertedlong = directionlong*(degreelong + (minutelong + secondslong/60)/60)
    
    return convertedlong


def convert_SI(val, unit_in, unit_out):
    
    SI = { 'pm':0.0000000000001, 'Am':0.00000000001, 'nm':0.0000000001, 'um':0.000001,'mm':0.001, 'cm':0.01, 'dm':0.01, 'm':1.0, 'dam':10.0, 'hm':100.0, 'km':1000, 'Mm':1000000, 'Gm':1000000000, 'Tm':1000000000000, 'Pm':1000000000000000.}
    return val*SI[unit_in]/SI[unit_out]


def rackverter():
    
    inputinches = float(input("How many inches ya got?: "))
    rackertime = inputinches/1.75
                #https://en.wikipedia.org/wiki/Rack_unit     Please and thank you for reading this
    return print(f'You got {rackertime} racks')

def plaid():
    
    inputcm = float(input("How many cm are you traveling?: "))
    nanosecs = inputcm/29.9792458 
    
    return print(f'You have traveled {nanosecs} light-nanoseconds')

def m2miles(value):
    return print(f'You have {(value/1609.344)} miles')

def miles2m(value):
    return print(f'You have {(value*1609.344)} meters')
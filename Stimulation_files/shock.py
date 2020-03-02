import time
import sys

"""
	Description - Shock the user for shock_for amount of time
	Parameters - (shock_for - the amount time you want to shock the user) 
"""
def distribute_shock (peripheralsmanager, shock_for):
    for _ in range(shock_for):
        peripheralsmanager.shockOn()
        print('- - - shocking - - -')
        time.sleep(0.1)
        peripheralsmanager.shockOff()

def main():
    #creating a PheripheralsManager 
    try:
        peripheralsmanager = peripheralsManagerCompoundSerial.PeripheralsManager()
    except:
        print('[Error] Failed connection to Labjack / Digitimer.')
        return -1
    
    if len(sys.argv) < 2:
        print("[Error] No arguments passed in. Require argument(s): [Number of Shocks]")
        return
    
    shock_for = 0
    
    try:
        shock_for = int(sys.argv[1])
    except:
        print("[Error] Argument is not an integer.")
        return

    # Laptop mode... Not connected to LabJack
    print('[Laptop Mode] Shocking!')

    ## Desktop mode... LabJack Connected
    # try:
    #     import peripheralsManagerCompoundSerial                                     #everything to manage labjack
    #     peripheralsmanager = peripheralsManagerCompoundSerial.PeripheralsManager()  #creating a PheripheralsManager 
    #     distribute_shock(peripheralsmanager, shock_for)
    # except IOError as myerror:
    #     print(myerror)
    #     print('Exiting script')


if __name__ == '__main__':
    main()



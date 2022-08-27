#Program Name: vendingMachine
#Author: Cole Pedersen
#Date: 10/23/2021
#Program Description: This program uses a compound lists to act like a vending machine

# I have a question, when i was making this program this appeared (from ast import Str) I do not know why, as I did not enter it in,
# and I don't know what it does but i removed it and this program still works. I think it auto imported itself from old logic in this
# program that got cut when finishing it but I'm not sure

#Other then creating the list from a text file the main function dosen't do anything that crazy.
#It calls functions and gives the program some ways of ending Which is why their are two different Again = 'N'
def main():
    Again = 'Y'
    Vending_Items = open('items.txt', 'r')
    Vending_List = [Vending_Items.readline().rstrip('\n').split(','), Vending_Items.readline().rstrip('\n').split(','), Vending_Items.readline().rstrip('\n').split(','), Vending_Items.readline().rstrip('\n').split(','), Vending_Items.readline().rstrip('\n').split(',')]
    Vending_Items.close
    while Again == 'Y':
        start_up_message(Vending_List)
        Row, Quantity = Row_Quant_Selection(Vending_List)
        if Row != str:
            print('\n------------------------')
            print(f'You\'ve selected {Vending_List[Row][1]} (x{Quantity})')
            print('------------------------\n')
            pay = input('Would you like to [P]ay of [C]ancel (P/C): ').upper()
            print (pay)
            if pay == 'P':
                checkout(Row, Quantity, Vending_List)
                New_Qty = str(int(Vending_List[Row][3]) - Quantity)
                Vending_List[Row][3] = New_Qty
                print (Vending_List)
                Again = input('Would you like to make another purchase (Y/N): ').upper()
            else:
                Again = 'N'
        else:
            Again = 'N'

#This has a bulk of the programing, it essentually checks if the given Item number is stocked or entered incorrectly
#It then takes note of the row that the given item is in and how many you want, returning that to main
#It has one flaw in that it will count something as found and like you entered the right item number if the item number
#is put in, so if you put in 3 it will count you like you put in C3, if you put in C it will count you as putting in C3
def Row_Quant_Selection(Vending_List):
    Valid = 'N'
    item = input('> Select Item #: ').upper()
    while Valid == 'N':
        if item in Vending_List[0][0]:
            if int(Vending_List[0][3]) == 0:
                print('I am sorry but we are all out of that Item #')
                Chose_Anoth_item = input('Would you like to pick another Item # (Y/N): ').upper()
                if Chose_Anoth_item == 'N':
                    return 'No', 'No'
            else:
                Valid = 'Y'
                Row = 0
        if item in Vending_List[1][0]:
            if int(Vending_List[1][3]) == 0:
                print('I am sorry but we are all out of that Item #')
                Chose_Anoth_item = input('Would you like to pick another Item # (Y/N): ').upper()
                if Chose_Anoth_item == 'N':
                    return 'No', 'No'
            else:
                Valid = 'Y'
                Row = 1
        if item in Vending_List[2][0]:
            if int(Vending_List[2][3]) == 0:
                print('I am sorry but we are all out of that Item #')
                Chose_Anoth_item = input('Would you like to pick another Item # (Y/N): ').upper()
                if Chose_Anoth_item == 'N':
                    return 'No', 'No'
            else:
                Valid = 'Y'
                Row = 2
        if item in Vending_List[3][0]:
            if int(Vending_List[3][3]) == 0:
                print('I am sorry but we are all out of that Item #')
                Chose_Anoth_item = input('Would you like to pick another Item # (Y/N): ').upper()
                if Chose_Anoth_item == 'N':
                    return 'No', 'No'
            else:
                Valid = 'Y'
                Row = 3
        if item in Vending_List[4][0]:
            if int(Vending_List[4][3]) == 0:
                print('I am sorry but we are all out of that Item #')
                Chose_Anoth_item = input('Would you like to pick another Item # (Y/N): ').upper()
                if Chose_Anoth_item == 'N':
                    return 'No', 'No'
            else:
                Valid = 'Y'
                Row = 4
        if Valid == 'N':
            item = input('> Enter a Valid Item #: ')
    Valid = 'N'
    Quantity = int(input('> Select Quantity: '))
    while Valid == 'N':
        if Quantity <= int(Vending_List[Row][3]):
            Valid = 'Y'
            print('good')
        else:
            Quantity = int(input('> Enter a Valid Quantity: '))
    return Row, Quantity

#Does the start up message and is formated to look pretty
def start_up_message(Vending_List):
    print ('   Vending Machine')
    print ('---------------------')
    print ('##  ITEM   PRICE   QTY')
    print (f'{Vending_List [0][0]:<4}{Vending_List [0][1]:<7}${Vending_List [0][2]:<7}{Vending_List [0][3]:<3}')
    print (f'{Vending_List [1][0]:<4}{Vending_List [1][1]:<7}${Vending_List [1][2]:<7}{Vending_List [1][3]:<3}')
    print (f'{Vending_List [2][0]:<4}{Vending_List [2][1]:<7}${Vending_List [2][2]:<7}{Vending_List [2][3]:<3}')
    print (f'{Vending_List [3][0]:<4}{Vending_List [3][1]:<7}${Vending_List [3][2]:<7}{Vending_List [3][3]:<3}')
    print (f'{Vending_List [4][0]:<4}{Vending_List [4][1]:<7}${Vending_List [4][2]:<7}{Vending_List [4][3]:<3}')

#Preforms the check out functions includeing calculating change and getting mad if you don't put in enough money
#Originally it was also going to give you a choice to exit the program if you did not put in enough money this was cut due to time as I have family visiting, I was not warned of this
def checkout(Row, Quantity, Vending_List):
    print('\n----------------')
    print('    Checkout')
    print('----------------')
    print(f'TOTAL: ${float(Vending_List[Row][2])*Quantity:,.2f}')
    payment = float(input('> Payment Amount: '))
    Valid = 'N'
    while Valid == 'N':
        if payment > float(Vending_List[Row][2])*Quantity:
            print(f'Your change is: ${abs(float(Vending_List[Row][2])*Quantity-payment):,.2f}')
            Valid = 'Y'
        elif payment < float(Vending_List[Row][2])*Quantity:
            print('That is not enough money')
            payment = float(input('Enter a valid payment: '))
        else:
            Valid == 'Y'
    print('\n** Thank you! **')

main()
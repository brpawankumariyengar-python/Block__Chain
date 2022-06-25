import random
from datetime import datetime



def Pawan__Block__Chain__Creator(From__Person, To__Person, Amount__Transferred, Payment__Method,Interest__Rate, Previous__Block__Hash__Code):
	From__Person = From__Person
	To__Person = To__Person
	Amount__Transferred = Amount__Transferred
	Payment__Method = Payment__Method
	Interest__Rate = Interest__Rate
	Previous__Block__Hash__Code = Previous__Block__Hash__Code
	Hash__Code__Input = Pawan_Random_Password_Create(32, From__Person, To__Person, Amount__Transferred, Payment__Method, Interest__Rate, Previous__Block__Hash__Code)
	Pawan__Final__Hash__Code = hash(Hash__Code__Input)
	print(Hash__Code__Input)
	print(Pawan__Final__Hash__Code)


def Pawan_Random_Password_Create(Password_Length, From__Person, To__Person, Amount__Transferred, Payment__Method, Interest__Rate, Previous__Block__Hash__Code):
	From__Person = From__Person
	To__Person = To__Person
	Amount__Transferred = Amount__Transferred
	Payment__Method = Payment__Method
	Interest__Rate = Interest__Rate
	Previous__Block__Hash__Code = Previous__Block__Hash__Code
	today = datetime.now() 
	print("Today's date:", today)
	Password_Length = str(Password_Length) 
	Uppercase_Aphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
	lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"
	Digits = "0123456789" 
	Special_Chatecters = "@!#$&*?-_|" 
	All_Combined = Uppercase_Aphabets + lowercase_alphabets + Digits + Special_Chatecters 
	if Password_Length.isnumeric() == True: 
		Password_Generated = "".join(random.sample(All_Combined,int(Password_Length))) 
		Password_Generated = Password_Generated + str(today) + "From  :" + From__Person + "To person:  " + To__Person + "Amount Transferred" + Amount__Transferred + "Payment Method:   " + Payment__Method + "Interest Rate:  "+ Interest__Rate + "Prev Chain:"+ Previous__Block__Hash__Code
		return Password_Generated 
	else: 
		print("Invalid input .... Please try again")

def main():
	From__Person = input("Please enter from person:     ")
	To__Person = input("Please enter to person:     ")
	Amount__Transferred = input("Please enter the amount Transferred:     ")
	Payment__Method = input("Please enter the Payment Method:     ")
	Interest__Rate = input("Please enter the interest rate:     ")
	Previous__Block__Hash__Code = input("Please enter previous block hash:     ")
	Pawan__Block__Chain__Creator(From__Person, To__Person, Amount__Transferred, Payment__Method, Interest__Rate, Previous__Block__Hash__Code)

if __name__ == "__main__":
	main()
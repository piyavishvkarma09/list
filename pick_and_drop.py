print("\U0001f600","**pick and drop**","\U0001f600")
print("wellcome to pick and drop services")
print('enjoy your trip with **pick and drop:**)')
currunt_location=["pune","toll plaza","katraz","your currunt location"]
droping_point=["katraj","pune","nagpur","other location"]
cab_typ=["auto","taxi","cab","prime"]
cab_details=[["1.auto: rider;suresh, contact;9876543211, 100 inr for first km and 10inr for next so on, ratings;good"],
            ["2.taxi: rider;yash, contact;7896543201,ratings;okey!,150 inr for first km and 20inr for next so on"],
            ["3.cab: rider;dev, contact;9878768675, good, 200 inr for first km and 25inr for next so on"],
            ["not available"]]
print(currunt_location)
pick_point=input('enter  your currunt location  :')#pune 
i=0
while i<len(currunt_location):
    if pick_point==currunt_location[i]:
        print(droping_point)
    location=input("enter droping location:")#katraj
    j=0
    while j<len(droping_point):
        if location== droping_point[j]:
            print(cab_typ)       
        j=j+1 #i+=1
        type=input('select your type:')#any type from given list
        l=0
        while l<len(cab_typ):
            if type== cab_typ[0]:
                print (cab_details[0])
            elif type==cab_typ[1]:
                    print(cab_details[1])
            elif type==cab_typ[2]:
                        print(cab_details[2])
                        confirm=input("plese confirm by yes: ")
                        if confirm=="yes":
                            print("your cab is booked, please wait")
                            print()
                            print("your selcted cab service will arrive within 20 minuts")
                            otp=int(input("enter your 4 digit otp"))
                            print("happy journey")
                            print("you have reached,please do your payment")
                            payment=input("choose your :/n.1)online /n.2)cash")
                            if payment=="1" or payment=="2":
                                print("yes")
                            feedback=input("plese give your valuable feedback")
                            print("thanks for being a part of p&d")
                        else:
                            print('not available')
            l+=1
    i+=1       
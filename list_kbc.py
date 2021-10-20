print("** *wellcome to KBC***")
question_list=["1.Taj Mahal is the symbol of ----?",
                "2.what is the capital of india?",
                "3.which course is teaching in NG?"]
option_list=[["love","laathe","honour","respect"],
             ["kashmir","dehli","madhyprdesh","gujarat"],
             ["tourism","software engineering","cultural","agricultural"]]
solution_list=["1","2","2"]
answere_list=[["1.love","2.laathe"],
               ["1.kashmir","2.delhi"],
               ["1.tourism","2.softaware engineering",]]
print("koun banega cororepati(KBC)")
i=0
s=0
count=0
sum=0
while i<len(question_list):
    print(question_list[i])
    j=0
    k=1
    while j<len(option_list[i]):
        print(k,".",option_list[i][j])
        j+=1
        k=k+1
    lfln=input("Do you want to use 50 50 lifeline? ")
    if lfln=="yes":
        print(" 50 50 lifeline is here: ")
        if count<1:
            print(answere_list[i])
            user=input("Choose the option given above  🕑⬆️: ")
            if user==solution_list[i]:
                sum=sum+1000
                print("u win Rs/",sum)
            else:
                print(" 😢WRONG answer  😢 ;sorry you lost the game  😢; ")
                break
            count=count+1
            # print()
        else:
            # print()
            print(" 🤫you have already used lifeline .")
            # print()
            user1=input(" choose the option : ")
            if user1==solution_list[i]:
                sum=sum+1000
                print("u win Rs/",sum)
            else:
                print("😢 WRONG answer ;sorry you lost the game  😢")
                print("YOU LOST THE CHANCE!!!")
                break
            print()
    elif lfln=="no":
        print("")
        user2=input("Choose the option: ")
        if user2==solution_list[i]:
            sum=sum+1000
            print("u win Rs/",sum,"🎊🎉congratulation you are the winner of KBC🎊🎉")
        else:
            print("😓YOU MISS THE CHANCE!!! WRONG ANS...BETTER LUCK NEXT TIME")
            break
    else:
        print("nothing")
     
    i+=1
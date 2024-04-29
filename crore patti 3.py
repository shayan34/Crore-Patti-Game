questions = [["which language is used to create facebook ?", "python ", "french " , "javascript" , "Php", "none" , 4] , 
             ["which language is used to create facebook ?", "python ", "french " , "javascript" , "Php", "none" , 4] ,
             ["which language is used to create facebook ?", "python ", "french " , "javascript" , "Php", "none" , 4],
             ["which language is used to create facebook ?", "python ", "french " , "javascript" , "Php", "none" , 4],
             ]

levels = [1000,2000, 3000, 5000, 10000, 20000,40000,80000,160000,320000]

for i in range ( 0 ,len(questions) ):
    question = questions[i]
    print(f"Question is for RS , {levels[i]}")
    print(f"a. {question[1]}         b. {question[2]}")
    print(f"a. {question[3]}         b. {question[4]}")
    reply = int(input("Please any number between 1 to 4 :"))
    if (reply==question[-1]):
        print(f" you won the RS . {levels[i]}")
    else:
        print("Wrong input")
        break
import random
response="yes"
while response!="no":
    generated_number=random.randint(1,30)
    won=False


    for guess in range(3):
       user_guess=int(input("Enter a number of your choise : "))
       if user_guess==generated_number:
              won=True 
              print("You have guessed correctly.")
              break
       elif user_guess<generated_number:
           print("You have guessed lower than the generated number.")
       else:
           print("You have guessed higher than the generated number.")



    if won==True:
        print("You have won the game.Congrats.")
    else:
        print("You didn't won this round.")


    raw_response=input("care to try again: ").lower()
    if raw_response.lower()=="yes" or raw_response.lower()=="y" or raw_response.lower()=="1":
        response="yes"
    else:
        response="no"
        break

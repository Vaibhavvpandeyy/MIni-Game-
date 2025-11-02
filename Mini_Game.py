import random #importing module for getting random outputs from computer

options = ("Stone","Paper","Scissors")

rand_comp= random.choice(options)

user=input('''Stone Paper or Scissors?
Type st pp or sc : ''')
st = ("Stone")
sc = ("Scissors")
pp= ("Paper")

if(user=="st"):
    user_choice="Stone"
elif(user=="sc"):
    user_choice="Scissors"
elif(user=="pp"):
    user_choice="Paper"
else:
    print("enter st / sc / pp.!")
    exit()
    
print(f"Your Choice: {user_choice}")
print(f"Computer's choice: {rand_comp}")
    

if (user_choice==rand_comp):
    print("Thats a draw try again!")
    
else:
    if(user_choice==st and rand_comp=="Paper"):
        print("you lose!")
    elif(user_choice== sc and rand_comp=="Paper"):
        print("You Win!")
    elif(user_choice== st and rand_comp=="Scissors"):
        print("You Win!")
    elif(user_choice== pp and rand_comp=="Scissors"):
        print("You lose!")
    elif(user_choice== sc and rand_comp=="Stone"):
        print("You lose!")
    elif(user_choice==pp and rand_comp=="Stone"):
        print("You win")
    else:
        print("error!")


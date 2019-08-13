#Asks name of person and gives a random fact generated from a list.


#Input name
print('Hello! What is your name?' )
name = input()

#Asks if you want a fact
print('Well, '+ name + ', would you like a random fact? (y/n)')
answer = input()

#Generate fact if person answers with yes
if answer =='y':
  import random
  facts_list = ['At birth, a baby panda is smaller than a mouse.', 'Iceland does not have a railway system.', 'The Roman – Persian wars are the longest in history, lasting over 680 years. They began in 54 BC and ended in 628 AD.', 'The Shawshank Redemption', 'The voice actor of SpongeBob and the voice actor of Karen, Plankton’s computer wife, have been married since 1995.']

  givenFact = random.choice(facts_list)
  print (givenFact)
  
#Answer if no
else:
  print('Ok then not.')


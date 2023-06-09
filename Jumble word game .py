#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
def choose():
    word = ['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board']
    pick = random.choice(word)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,' Your score is ',p1)
    print(p2n,' Your score is ',p2)
    print('Thanks for playing')
    print('Have a great day!!')
    

def play():
    p1name = input("Player 1, Enter your name: ")
    p2name = input("Player 2, Enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        #computer
        picked_word = choose()
        #create question
        qn = jumble(picked_word)
        print(qn)
        #player1
        if(turn % 2 == 0):
            print(p1name,'Your turn.')
            ans = input('What is on my mind?')
            if(ans == picked_word):
                pp1 = pp1 + 1
                print('Your score is: ',pp1)
            else:
                print('Better luck next time. I thought : ',picked_word)
            c = int(input('Press 1 to continue and 0 to quit'))
            if(c == 0):
                thank(p1name,p2name,pp1,pp2)
                break
        #player2
        else:
            print(p2name,'Your turn.')
            ans = input('What is on my mind?')
            if(ans == picked_word):
                pp2 = pp2 + 1
                print('Your score is: ',pp2)
            else:
                print('Better luck next time. I thought : ',picked_word)
            c = int(input('Press 1 to continue and 0 to quit'))
            if(c == 0):
                thank(p1name,p2name,pp1,pp2)
                break
        turn = turn + 1
play()


# In[ ]:

from random import choice
import os

A = "John Wick"

# You can add more participants

Givers = [A] #Do not forget to add them in the list
Receivers = Givers[:]
pairs = [[None for y in range(2)] for x in range(0, len(Receivers))]

def CanadianChristmas(Receivers):
    for i in range(0, len(Givers)):
        Giver_name = Givers[i]
        Receiver_name = choice(Receivers)
        pairs[i][0] = Giver_name
        pairs[i][1] = Receiver_name
        Receivers.remove(Receiver_name)
    for i in range(0, len(pairs)):
        if pairs[i][0] == pairs[i][1]:
            print("Duplicate found, reshuffling!")
            Receivers = Givers[:]
            CanadianChristmas(Receivers)

CanadianChristmas(Receivers)

if not os.path.exists('School/'):
    os.makedirs('School/')

with open('School/_message.txt', 'w', encoding='utf-8-sig') as m:
    for i in range(0, len(pairs)):
        with open(('The Society/' + pairs[i][0] + '.txt'), 'w', encoding='utf-8-sig') as f:
            f.write(pairs[i][0] + " --> " + pairs[i][1] + "\n")
            f.write("\nHi " + pairs[i][0] + " How are you? 😏\nIt's time for the 2019 Secret Santa! 🎅\nCheck the file to know whom you're gifting ✨🎁\nYou'll need to offer a gift between €10 and €20! 😱\nLove you! 💖\n\n")
        f.close()
m.close()

print("Done :)\n-> Go check the School folder, buddy!")

import os
import sys
import json
import random
import platform
import matplotlib.pyplot as plt

if platform.system() == 'Windows':
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')

clear()
xaxis = []
yaxis = []

with open('data.json', 'r') as jfile:
    data = json.load(jfile)

print('Game started! Type in \'0\' to exit.')
yaxis.append(data['balance'])
xaxis.append(0)

def info():
    print('Your balance is: ' + str(data['balance']))
    print('Min: ' + str(data['min']))
    print('Max: ' + str(data['max']))

def graph():
    plt.plot(xaxis, yaxis)
    plt.xlabel('Tries')
    plt.ylabel('Balance')
    plt.title('Graph')
    plt.savefig('GameGraph.png')

def save():
    with open('data.json', 'w') as jfile:
        json.dump(data, jfile)

while True:
    try:
        info()
        count = int(input(': '))

        while count < 0:
            clear()
            print('Bet value could not be negative!')
            info()
            count = int(input(': '))

        while count > data['balance']:
            clear()
            print('Bet value could not be bigger than current balance!')
            info()
            count = int(input(': '))

        if count == 0:
            clear()
            print('Exiting game and writing data to graph...')
            info()
            save()
            graph()
            break

        clear()
        x = random.randint(0, 1)

        if x == 0:
            data['balance'] = data['balance'] - count
            print('You lost ' + str(count) + ' coins!')
        else:
            data['balance'] = data['balance'] + count
            print('You won ' + str(count) + ' coins!')

        if data['balance'] > data['max']:
            data['max'] = data['balance']
        if data['balance'] < data['min']:
            data['min'] = data['balance']

        yaxis.append(data['balance'])
        xaxis.append(xaxis[-1] + 1)

        if data['balance'] == 0:
            clear()
            print('Game over! Writing data to graph...')
            info()
            data['balance'] = 100
            data['min'] = 100
            data['max'] = 100
            save()
            graph()
            break

    except:
        clear()
        print('Bet value must be a number!')

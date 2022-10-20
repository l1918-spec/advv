name = input('type your name : ')
print('welcome', name, 'to this amazing game')
answer =  input('you are in a dirt path, you can go left or right , what would you choose ?').lower()

if answer == 'left' :
    answer = input('you come to a river, you can walk next to it or swim across , type walk or swim : ')
    if answer == 'swim':
        print('you will end up eaten by an alligator')
    elif answer =='walk' :
        print('wise choice keep walking, but you lose anyways lmao')
    else :
        print('not a valid option')

elif answer == 'right' :
    answer = input('you walk to a bridge, do you wanna cross it or head back ? choose cross or head back : ')
    if answer == 'head back':
        print('you lose ')
    elif answer == 'cross':
        answer = input('you gonna find a stranger, wanna talk to him ? yes or no :')
        if answer == 'yes':
            print('he gave you a gold, you won')
        if answer == 'no':
            print('you ignored the stranger you lost the gold')

    else:
        print('not a valid option')

else :
    print('not a valid option ')
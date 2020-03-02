movie_intro = 'Welcome to J-Bone Cinema!'
movie_intro += '\nPlease input your age: '

active = True

while active:
    message = input(movie_intro)
    message = int(message)

    if message < 3:
        print('This ticket is free.')
        break
    elif 3 <= message <= 12:
        print('This ticket is $10.')
        break
    elif message > 12:
        print('This ticket is $15.')
        break

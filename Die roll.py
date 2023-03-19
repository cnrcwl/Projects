import random

play_again = 'r'
while play_again == 'r':
    num = random.randint(1,6)
    if num == 1:
        print(
            '''
            [---]
            [-0-]
            [---]
            '''
        )
    if num == 2:
        print(
            '''
            [0--]
            [---]
            [--0]
            '''
        )
    if num == 3:
        print(
            '''
            [---]
            [000]
            [---]
            '''
        )
    if num == 4:
        print(
            '''
            [0-0]
            [---]
            [0-0]
            '''
        )
    if num == 5:
        print(
            '''
            [0-0]
            [-0-]
            [0-0]
            '''
        )
    if num == 6:
        print(
            '''
            [0-0]
            [0-0]
            [0-0]
            '''
        )
    play_again = input("Press 'r' to roll or Enter to exit:")
print("Goodbye!")

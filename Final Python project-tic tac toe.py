import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])

# class used to control program if user type anything other asked values
class NotinList(Exception):
    "Raised when input is not in list"
    pass

#checks to see if any rows match up with 
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol, 'won')
            return True
    return False

# checks to see if any columns line up with X's or O's 
def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol, 'won')
            return True
    return False

#checks diagonals to see if they are either filled with only X's or only O's
def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    return False

# determines whether user has won or not 
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

# controls the places of X and O in the matrix
def place(symbol):
    print(numpy.matrix(board))
    try:
        while(1):
                row=int(input('Enter row- 1 or 2 or 3:'))
                col=int(input('Enter column- 1 or 2 or 3:'))
        
                if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
                    break

                else:
                    print('Invalid input.Please enter again')
        board[row-1][col-1]=symbol
# in case user types in anything other than numbers, as a penalty his chance is skipped.
    except:
        print("Wrong input.Please enter values between 1 and 3 only.")
        
#starts the game. shows the tic tac toe matrix 
def play():
    a=['X','O']
    if (board[0][0] in a or board[0][1] in a or board[0][2] in a or board[1][0] in a or board[1][1] in a or board[1][2] in a or board[2][0] in a or board[2][1] in a or board[2][2] in a):
        board[0][0]='-'
        board[0][1]='-'
        board[0][2]='-'
        board[1][0]='-'
        board[1][1]='-'
        board[1][2]='-'
        board[2][0]='-'
        board[2][1]='-'
        board[2][2]='-'
    print(numpy.matrix(board))
    p1s=''
    p2s=''
    #asks user to enter their choice of X and O. 
    while(p1s not in a):   
        try:
            p1s=input("Choose a symbol between X and O:")
            p2s=''
            if (p1s in a):
                if p1s=='X':
                    p1s='X'
                    p2s='O'
                elif p1s=='O':
                    p1s='O'
                    p2s='X'
            else:
                raise NotinList
#in case user types in anything other than X or O     
        except NotinList:
            print("Wrong input. Choose X or O only.")
#this code exectues during the game. In case any player wins it breaks.
    for turn in range(9):
        if turn%2==0:
            print(p1s,'turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print(p2s, 'turn')
            place(p2s)
            if won(p2s):
                break
#In case match is drawn prints out following
    if not(won(p1s)) and not(won(p2s)):
        print('Draw')
    #prompts user to either continue or quit
    f=input("Press R to rematch or Q to quit:")
    if (f=='R'):
        welcome()      
    elif(f=='Q'):
            print("Thank you very much for your time.")
    else:
            print("invalid input")

#Asks user to prompt their choice
def choice():
    a=input("Press Y to continue:")   
    if (a=="Y"):
        play()

#Introduction to the game. Welcomes user and gives intructions    
def welcome():
    print("Welcome to my Game -Tic Tac Toe")
    print("This Game has some basic rules and directions:")
    print("1. This game will only use X and O. No other entries will be allowed.")
    print("2. The first player will get a choice between O and X.The game will only move forward if you choose between X and O.")
    print("3. The player who chooses will get the first chance to play.")
    print("4. You will have to specify row and column each time you play.")
    print("5. If you type in incorrect numbers, it will prompt you to type again. If you type anything other than positive integers, your chance will be skipped and passed on to your opponent.")
    choice()

#starts the program with code
p1s=''
p2s=''
welcome()

    


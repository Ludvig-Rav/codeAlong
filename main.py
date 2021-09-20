# Python - intro codealong
 
# - Funktioner
 
hello = 'This is a string inside a variable'
universe = 42
bar = 1.25
foo = '42'
space = ' .:. '
 
# print(type(hello))
# print(type(world))
# print(type(d))
# print('hello' + space + 'world' + space + str(bar))
# print(type(bar))
 
# skriv en funktionsdefinition som tar in en parameter
# parametern består av en sträng som består av en fråga
# funktionen ska ställa frågan till användaren
# det användaren svarar skall konverteras till int eller float
# samt returneras tillbaka till anropande kod
 
 
def ask_user(prompt):
    #print(f'The function was called with argument {prompt}')
    s = input(prompt)
    #print(type(s))
    return eval(s)
 
def calculate_area (length):
     # Skriv en funktion som tar in en längd som argument
     # och returnera ytan av en kvadrat med denna längd
    area = length ** 2
    return area 
 
answer = ask_user('please enter a length in meters: ')
# print(f'The user answered {answer}')
#s = eval(input('please enter a distance in cm: '))
# print(s)

result = calculate_area(answer)
print(f'The area av the squere is {result}')
#area = s ** 2
# print('The area of a square with side ' + str(s) +
#      ' cm is equal to ' + str(area) + ' cm^2')
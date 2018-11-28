import requests
import json

#r = requests.get('http://10.42.0.1:5000/', auth=('oep211', 'secret'))
# http://10.42.0.1:5000/<command-family>/<username>/<secret>/<action>/<index>

command_family = 'login'
host = 'http://10.42.0.1:5000'
user = 'kbm383'
secret = 'secret'
index = '1' #amount of time it's held for
startH = 'start_holding'
stopH = 'stop_holding'
tick = 'tick'
direction = 'select_direction'
benchmark = 'B'
attempt = 'attempt_heal'
heal = 'heal_solution'
solution = 'solution'


#login
r = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + benchmark)
print (r.text)

command_family = 'game'
s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

s3 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + startH)
r3 = requests.post(s3)
print(r3.text)

s4 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + stopH)
r4 = requests.post(s4)
print(r4.text)

s5 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + stopH)
r5 = requests.post(s5)
print(r5.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])
#Lines 55-60 show us direction to proceed in.

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

#check the number of options until you check one that's not one

#loop 1
while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])
  

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print("++++++++++++Liver_0++++++++++++")

#loop 2

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])
#Lines 55-60 show us direction to proceed in.

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print("++++++++++++++Liver_5++++++++++++++++++")

#loop 3

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])
#Lines 55-60 show us direction to proceed in.

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print('==================ENDLOOP3===================')


#loop 4

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])
#Lines 55-60 show us direction to proceed in.

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

s7 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
r7 = requests.post(s7)
print(r7.text)

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + heal + '/' + solution)
r8 = requests.post(s8)
print(r8.text)

print('++++++++++ENDLOOP4++++++++++++')

index ='1'

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

s7 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
r7 = requests.post(s7)
print(r7.text)

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + heal + '/' + solution)
r8 = requests.post(s8)
print(r8.text)


'''
#loop 5

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])
#Lines 55-60 show us direction to proceed in.

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print('++++++++++++++++ENDLOOP5++++++++++++++++')
'''

'''    
s7 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
r7 = requests.post(s7)
print(r7.text)


s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + solution)
r8 = requests.post(s8)
print(r8.text)
'''

action = 'reset'
logout = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(logout.text)
#Game is used for logout.

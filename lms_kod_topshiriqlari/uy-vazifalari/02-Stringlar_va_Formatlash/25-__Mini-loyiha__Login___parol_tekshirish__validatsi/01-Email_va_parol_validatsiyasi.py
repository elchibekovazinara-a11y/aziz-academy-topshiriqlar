email = input()
parol = input()
             
natiqa = '@' in email and '.' in email and 8 <= len(parol) <= 16 and email.islower()
             
print(natiqa)
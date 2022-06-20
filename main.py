import os, random, string

if os.name == 'nt':
    def clear():
        os.system('cls')

else:
    def clear():
        os.system('clear')

chars = list('''!"#$%&'*+-./:<=>?''' + string.ascii_letters + string.digits)
random.shuffle(chars)

clear()
while 1:
	len_ = input('Saisissez la longueur du mot de passe (par défaut 20 ~ 30 caractères) :\n> ')

	try:
		if len_.strip(' \t') == '':
			len_ = random.randint(20, 30)

		len_ = int(len_)

	except ValueError:
		clear()
		print("La valeur saisie doit être un nombre\n")
		continue

	else:
		pwd = []
		for i in range(len_):
			pwd.append(random.choice(chars))

		break

clear()
print(''.join(pwd))

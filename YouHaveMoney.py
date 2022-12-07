purchase = input("\nВведите то что вы хотели бы купить: \n>>> ")

def YouHaveMoney():
	return f"Купите {purchase}!!!"
answer = YouHaveMoney()

print("\nВыбирайте цифру для ответа на вопрос!")

ask1 = input(f"\nУ вас есть деньги?? \n1 - Да\n2 - Нет\n3 - Не для {purchase}\n>>> ")
if ask1 == "1":
	print(f"\n{answer}")
elif ask1 == "2":
	ask2 = input("\nУ вас есть работа? \n1 - Да\n2 - Нет\n>>> ")
	if ask2 == "1":
		ask3 = input("\nОни вам платят? \n1 - Да\n2 - Нет\n>>> ")
		if ask3 == "1":
			print(f"\n{answer}")
		elif ask3 == "2":
			ask4 = input("\nУ вас есть имущество? \n1 - Да\n2 - Нет\n>>> ")
			if ask4 == "1":
				print(f"\nПродавайте\n{answer}")
			elif ask4 == "2":
				ask5 = input("\nУ вас есть душа? \n1 - Да\n2 - Нет\n>>> ")
				if ask5 == "1":
					print(f"\nПродавайте\n{answer}")
				elif ask5 == "2":
					while True:
						print("Ложь")
						ask5 = input("\nУ вас есть душа? \n1 - Да\n2 - Нет\n>>> ")
						if ask5 == "2":
							True
						elif ask5 == "1":
							print(f"\nПродавайте\n{answer}")
							break
	elif ask2 == "2":
		ask6 = input("\nУ вас есть имущество? \n1 - Да\n2 - Нет\n>>> ")
		if ask6 == "1":
			print(f"\nПродавайте\n{answer}")
		elif ask6 == "2":
			ask7 = input("\nУ вас есть душа? \n1 - Да\n2 - Нет\n>>> ")
			if ask7 == "1":
				print(f"\nПродавайте\n{answer}")
			elif ask7 == "2":
				while True:
					print("Ложь")
					ask7 = input("\nУ вас есть душа? \n1 - Да\n2 - Нет\n>>> ")
					if ask7 == "2":
						True
					elif ask7 == "1":
						print(f"\nПродавайте\n{answer}")
						break
elif ask1 == "3":
	print(f"\nЖмот\n{answer}")
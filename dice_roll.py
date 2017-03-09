#CMD + backslash after highlighting all text will add hastags before all lines. otherwise, can wrap in triple apostrophes, like in Slack

# count = 0
# while (count < 9):
#    print "The count is:", count
#    count = count + 1

# print "Good bye!"


# count = 0
# while count < 5:
#    print count, " is  less than 5"
#    count = count + 1
# else:
#    print count, " is not less than 5"



# import random

# result = random.randint(1,6)

# if result == 2:
# 	print(result)
# 	print("Congrats, you rolled my favorite number!")
# elif result == 1:
# 	print(result)
# 	print("Congrats, you're number 1!")
# else:
# 	print(result)


import random

prompt = raw_input("If you want to roll, first you have to provide Berk's first name:\n")

if prompt == "David":
	print("Congrats, here are your rolls...")
	get_to_roll = 1
elif prompt in ["Davy","Dave"]:
	fix_prompt = raw_input("Berk doesn't really like being called that, please try again:\n")
	if fix_prompt == "David":
		print("Second time's a charm. Here are your rolls...")
		get_to_roll = 1
	else:
		print("Wrong again...")
		get_to_roll = 0
else:
	print("Uh, no...go away")
	get_to_roll = 0

if get_to_roll == 1:
	roll_num = 1
	snake_eyes_count = 0

	while roll_num <= 10:
		first_roll = random.randint(1,6)
		second_roll = random.randint(1,6)
		if first_roll == second_roll:
			#print("You rolled a " + str(first_roll) + " and a " + str(second_roll) + ". Snake eyes!")
			print ("You rolled a {} and a {}. Snake eyes!".format(first_roll, second_roll))
			snake_eyes_count +=1
		else:
			print("You rolled a " + str(first_roll) + " and a " + str(second_roll))
		roll_num += 1
	if snake_eyes_count >= 3:
		points_earned = snake_eyes_count * 3
		print("Wow you rolled {} Snake Eyes! {} points to Gryffindor!".format(snake_eyes_count,points_earned))
















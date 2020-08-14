def looping_through(lst):
	for item in lst:
		print(item)

clothing = ['coat', 'shirt', 't-shirt', 'sweater', 'jeans', 'denem jeans', 'overals']

looping_through(clothing)

the_counter = 0

def loopin_through(lst):
	while the_counter < len(lst):
		print(lst[the_counter])


def multiply(s, e):
	return s * e

multiply(567, 5)


def get_longest_lst(lst_1, lst_2):
	if len(lst_1) > len(lst_2):
		return lst_1
	elif len(lst_2) > len(lst_1)
		return lst_2

g = get_longest_lst(ice_cream_shape, ball_discription)

ice_cream_shape = ['tall', 'small bean', 'medium', 'huge', 'kuhkgfkdjh', 'fhkhkfhajk', 'hfkuhuak']

ball_discription = ['round', 'bouncy(some)', 'colorful(some)']

print(g)


def get_longest_first_item(lst_1, lst_2):
	if len(lst_1[0]) > len(lst_2[0]):
		return lst_1
	elif len(lst_2[0]) > len(lst_1[0])
		return lst_2

ge = get_longest_first_item(ice_cream_shape, ball_discription)

print(ge)

# Compare length of a random list and a random number. Check if the length of the list is less than the number.

games = ['ROBLOX', 'Animal Crossing', 'Mario Party', 'scribble.io', 'Hole.io', 'Mario Cart', 'MapleStory', 'MapleStory 2', 'Human: Fall Flat', ' Animal Jam', 'Slither.io']

def comapre_lst_num(lst, number):
	if len(lst) > number:
		return lst
	elif len(lst) < number:
		return number

comapre_lst_num(games, 5)

# Compare length of a random string and a random list. Check if the length of the string is longer than the length of the list.

if len(str) < len(lst):
	return lst
elif len(str) > len(lst):
	return str

# Compare the first item of a list and the second item of a list. Check if they are equal.
 if len(games[0]) == len(games[1]):
 	return 'cool'
 elif len(games[0])!= len(games[1])
 	return ' saddnes'


miley_shop_items_things = ['stuffies', 'food', 'snack', 'restrooom', 'drinks', 'groceries', 'balls', 'clothing', 'bikes']

miley_shop_enemy_shop_items_things = ['food', 'snacks', 'drinks', 'restroom', 'groceries']

def len_of_stores(store_1, store_2):
	if len(store_1) > len(store_2):
		return 'oofy'
	elif len(store_1) < len(store_2)
		return 'cool!'

len_of_stores(miley_shop_items_things, miley_shop_enemy_shop_items_things)

def check_len_of_item(store_1, store_2):
	if len(store_1[5]) > len(store_2[3]):
		return True
	elif len(store_1[5]) < len(store_2[3]):
		return False

check_len_of_item(miley_shop_items_things, miley_shop_enemy_shop_items_things)

def change_status(hp):
	if hp > 0:
		status = 'alive'
	elif  hp < 0:
		status = 'dead'
	return status

def limit_name(name):
	if len(name) <= 12:
		return '✓'
	else:
		return 'Uh oh! Your name is too long. Please shorten your name.'



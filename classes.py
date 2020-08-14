class Person:
	def __init__(self, name):
		type_person = 'human'
		self.status = 'alive' # property
		self.hp = 100
		self.name = limit_name(name)
		self.level = 1
		self.equipped_weapon = None
		self.equipped_armor = None
		self.equpipped_pet = None
		self.talk_to_npc = talk_to_npc


	def use_potion(potion, target):
		if target == 'self':
			self.hp = self.hp + potion.power

	def equip_armor(armor):
		if self.level >= armor.level_limit
			self.equipped_armor = armor

	def change_status: # method
		if self.hp > 0:
			self.status = 'alive'
		elif  self.hp < 0:
			self.status = 'dead'

	def limit_name:
		if len(self.name) <= 20:
			return self.name
		else:
			return 'Uh oh! Your name is too long. Please shorten your name.'

	def equip_weapon(weapon):
		if self.level >= weapon.level_limit:
			self.equipped_weapon = weapon

	def attack_with_weapon(target):
		if self.equipped_weapon == None:
			print('Must equip weapon to attack!')
		else:
			target.hp = target.hp - self.equipped_weapon.strength

	def equipped_pet(pet):
		if self.equipped_pet == None:
			self.equipped_pet = pet	
	

class NPC:
	def __init__(self, name):
		self.name = name


	

class Enemy:
	def __init__(self, name, hp, strength, level):
		self.name = name
		self.hp = hp
		self.strength = strength
		self.status = 'alive'
		self.level = level
		self.heal = 1

	def change_status:
		if self.hp > 0:
		   	 self.status = 'alive'
		elif  self.hp < 0:
			self.status = 'dead'

# The enemies takes away hp from the target depending on the enemies strenth 
	def enemy_attack(target):
		target.hp = target.hp - self.strength

	def enemy_heal(hp):
		self.hp = self.hp + hp


class Potion:
	def  __init__(self, type_potion, power):
		self.power = power
		self.type = type_potion


class Weapon:
	def __init__(self, strength, type_weapon, ability, level_limit):
		self.strength = strength
		self.ability = ability
		self.type_weapon = type_weapon
		self.level_limit = level_limit


class Item:
	def __init__(self, name, description, color):
		self.name = name
		self. description =  description
		self.color = color


class  Armor:
	def __init__(self, protection, level_limit, name)
		self.protection = protection
		self.level_limit = level_limit
		self.name = name


class Game:
	def __init__(self, players, enemies):
		self.players = players
		self.enemies = enemies


class Pet:
	def __init__(self, name, speed, level, strength, rarity)
		self.name = name
		self.speed = speed
		self.level = level
		self.strength = strenth
		self.rarity = rarity


game_potions = {
	'poison_potion': {
		'name': 'Poison',
		'power': 10,
	},
	'hp_potion': {
		'name': 'Hp',
		'power': 10,
	},
	'better_attack_potion': {
		'name': 'Better Acttack (10 Min)',
		'power': 10
	}
}

game_armor = {
	'leather_armor_set': {
		'protection': 2,
		'level_limit': 1,
		'name': 'Leather Armor'
	},
	'icey_chestplate': {
		'protection': 4,
		'level_limit': 3,
		'name': 'Icey Chestplate'
	}
}

game_weapons = {
	'noob_sword': {
		'strength': 5,
		'type_weapon': 'sword',
		'ability': 'stun',
		'level_limit': 1
	},
	'noob_wand': {
		'strength': 6,
		'type_weapon': 'wand',
		'ability': 'freeze',
		'level_limit': 1
	}
}

game_items = {
	'star_fragment': {
		'name': 'Star Fragment',
		'description': 'When you wish upon a shooting star... you see a tiny, shiny item falling down from the sky. Could it be?! Yes! It\'s a Star Fragment!',
		'color': 'Light Yellow'
	},
	'upgrade_weapon_scroll': {
		'name': 'Upgrade Weapon Scroll',
		'description': 'Press A to upgrade weapon',
		'color': 'Teal Blue'
	},
	'old_paper': {
		'name': 'Old Paper',
		'description': 'Used to make an Upgrade All Scroll with a The Finest Jar of Magic in the Enchanted Forest',
		'color': 'Papaya Whip'
	},
	'mcoins': {
		'name': 'Mcoins (Vurtual Curencey)',
		'description': 'Use Mcoins to buy things in shops.',
		'color':'Golden Yellow'
	},
	'upgrade_armor_scroll': {
		'name': 'Upgrade Armor Scroll',
		'description': 'Press S to upgrade armor',
		'color': 'Royal Purple'
	},
	'upgrade_all_scroll': {
		'name': 'Upgrade All Scroll',
		'description': 'Can upgrade armor, weapons, etc.',
		'color': 'Ruby Red'
	},
	'pink_shell':{
		'name': 'Pale Pink Sea Shell',
		'description': 'A beautiful shade of pink on a sea shell found on the beach.'
		'color': 'Pale Pink'
	}
		
}	

# game instance
my_game = Game(players, enemies)

inventory = {}

# inventory = {'Hp': Potion('Hp',10), 'Poison': Potion('Poison', 10), 'Better Acttack (10 Min)': Potion('Better Acttack (10 Min)', 10)}


def genorate_instances:
	for key, value in game_potions.items():
		name = value['name']
		inventory[name] = Potion(name, value['power'])

		# dictionary[key] = value



	for key, value in game_weapons.items():
		name = value['type_weapon']
		weapon = Weapon(value['strength'], name, value['ability'], value['level_limit'])
		inventory[name] = weapon

	for key, value in game_items.items():
		name = value['name']
		item = Item(name, value[' description'], value['color'])
		inventory[name] = item

	for key, value in game_armor.items():
		Armor(value['protection'], value['level_limit'], value['name'])

# inventory['Poison']
# Potion('Poison', 10)

# instances of the class Person
miley = Person('Miley')
brenda = Person('Brenda')
players = [miley, brenda]

# instances of the class NPC
npc = NPC('Maria')
npc_1 = NPC('Lean')
npc_2 = NPC('Lena')
npc_3 = NPC('Sir Sherman')
npc_4 = NPC('Armor Shop Keeper')
npc_5 = NPC('Weapon Shop Keeper')
npc_6 = NPC('Potion Shop Keeper')
npc_7 = NPC('Scoll Shop Keeper')

npcs = {
	'npc': {
		'name': 'Maria',
	},
	'npc_1': {
		'name': 'Lean',
	},
	'npc_2': {
		'name': 'Lena',
	},
	'npc_3': {
		'name': 'Sir Sherman',
	},
	'npc_4': {
		'name:': 'Armor Shop Keeper',
	},
	'npc_5': {
		'name': 'Weapon Shop Keeper',
	},
	'npc_7':{
		'name': 'Potion Shop Keeper',
	},
	'npc_8': {
		'name': 'Scroll Shop Keeper'
	}	
}	


# instances of the class Enemy
slime = Enemy('Slimey', 10, 2, 1)
troll = Enemy('Trollio', 15, 3, 2)
mushroom = Enemy('Mooshroom', 20, 5, 4)
fungi_with_shell_to_protect = Enemy('Felly', 100, 10, 10)
enemies = [slime, troll]

miley.attack_with_weapon(slime)

return inventory['Hp'] # Potion('Hp', 10)

# You get a property from a object by using dot notation (object.property)

# you get a property from a object by using dot notation (object.property)

# you get a property from a object by using dot notation (oboject.property)


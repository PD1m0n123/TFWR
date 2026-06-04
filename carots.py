import logs, hay, config

def carots_farming():
	clear()
	
	#Делаем проверку на лимит для посадки и сбора моркови
	#Когда достигли лимита, мы должны проверить что мы пойдем собирать
	if num_items(Items.Carrot) >= config.LIMIT_CAROTS:
		#Если в банке у нас меньше травы, то идем фармить траву
		if num_items(Items.Hay) < num_items(Items.Wood):
			hay.hay_farming()
		#Если в банке у нас больше травы чем бревен, то идем фармить бревна
		elif num_items(Items.Hay) > num_items(Items.Wood):
			logs.logs_farming()
	
	#Если недостаточно ресурсов для посадки моркови, то идем фармить(выбор):
	if num_items(Items.Hay) <= 8:
		hay.hay_farming() #Либо сено(трава)
	if num_items(Items.Wood) <= 8:
		logs.logs_farming() #Либо бревна
	
	#Начальный цикл посадки моркови(1 цикл)
	for cols in range(get_world_size()):
		for rows in range(get_world_size()):
			till()
			plant(Entities.Carrot)
			if get_water() < 0.6:
				use_item(Items.Water)
			use_item(Items.Water)
			move(East)
		move(North)
	
	#Основной цикл посадки и сбора
	while num_items(Items.Hay) >= 8 and num_items(Items.Wood) >= 8:
		for cols in range(get_world_size()):
			for rows in range(get_world_size()):
				if can_harvest():
					harvest()
					plant(Entities.Carrot)
					use_item(Items.Water)
				move(East)
			move(North)
	
	if num_items(Items.Hay) <= 8:
		hay.hay_farming()
	if num_items(Items.Wood) <= 8:
		logs.logs_farming()
		
if __name__ == "__main__":
	clear()
	carots_farming()
	
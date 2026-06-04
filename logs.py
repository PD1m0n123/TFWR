import carots,hay, config

def logs_farming():
	clear()
	
	#Действия, если достигли лимита моркови:
	if num_items(Items.Carrot) >= config.LIMIT_CAROTS:
		while num_items(Items.Wood) <= config.LIMIT_WOOD:
			for harvesting in range(get_world_size()):
				for Hay_and_woods in range(get_world_size()):
					if can_harvest():
						harvest()
						plant(Entities.Bush)
					move(East)
				move(North)
		
		# Если мы собрали миллион дерева
		# И при этом сено ТОЖЕ уже на максимуме — полностью выходим
		if num_items(Items.Hay) >= config.LIMIT_HAY:
			return
		# А если сена не хватает — отправляем дрона добирать сено
		else:
			hay.hay_farming()

	#Начальный цикл фарма - это посадка(1 круг)
	for planting in range(get_world_size()):
		for rows in range(get_world_size()):
			plant(Entities.Bush)
			move(East)
		move(North)
	
	#Основной цикл сбора
	while num_items(Items.Wood) <= 100000:
		for harvesting in range(get_world_size()):
			for Hay_and_woods in range(get_world_size()):
				if can_harvest():
					harvest()
					plant(Entities.Bush)
				move(East)
			move(North)
	carots.carots_farming()#Делаем после выхода со сбора кустов

if __name__ == "__main__":
	clear()
	logs_farming()
import carots,logs,config

def hay_farming():
	clear()
	
	#Действия, если достигли лимита моркови(попали на фарм сена):
	if num_items(Items.Carrot) >= config.LIMIT_CAROTS:
		while num_items(Items.Hay) <= config.LIMIT_HAY:
			for harvesting in range(get_world_size()):
				for Hay_and_woods in range(get_world_size()):
					if can_harvest():
						harvest()
					move(East)
				move(North)
		
		# Если мы собрали миллион сена
		# И при этом дерево ТОЖЕ уже замаксено — вот тогда полностью завершаем программу
		if num_items(Items.Wood) >= config.LIMIT_WOOD:
			return
		#А если дерево ЕЩЁ НЕ замаксено — отправляем дрона максить дерево!
		else:
			logs.logs_farming()
	
	#Базовый цикл сборки, если не достигли лимита моркови:
	while num_items(Items.Hay) <= 50000:
		for harvesting in range(get_world_size()):
			for Hay_and_woods in range(get_world_size()):
				if can_harvest():
					harvest()
				move(East)
			move(North)
	carots.carots_farming()

if __name__ == "__main__":
	clear()
	hay_farming()
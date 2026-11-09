# ---------- ПОДСОЛНУХИ (ЭНЕРГИЯ) ----------

def sunflower_gathering():
	change_hat(Hats.Brown_Hat)
	
	if get_entity_type() == Entities.Sunflower:
		if can_harvest():
			# Собираем только те, у которых 15 лепестков (максимум энергии)
			# Если лепестков меньше, оставляем расти (занимаем место, но экономим ходы)
			if measure() == 15:
				harvest()
				# Сразу сажаем новый на освободившееся место
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Sunflower)
	else:
		# Если клетка пустая — сажаем подсолнух
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
#         return False
# 
#     current = get_entity_type()
# 
#     # Нужное растение уже есть
#     if current == wanted:
#         companions[pos] = None
#         return True
# 
#     # Проверяем текущее растение
#     if current != None:
# 
#         if not can_harvest():
#             return True
# 
#         harvest()
# 
#     if get_ground_type() != Grounds.Soil:
#         till()
# 
#     plant(wanted)
# 
#     if get_entity_type() == wanted:
#         companions[pos] = None
# 
#     return True
# 
# 
# 
# def prepare_soil():
# 
#     if get_ground_type() != Grounds.Soil:
#         till()
# 
# 
# def gather_and_plant(entity):
# 
#     prepare_soil()
# 
#     if can_harvest():
#         harvest()
# 
#     plant(entity)
# 
# 
# def hay_gathering():
# 
#     change_hat(Hats.brown_Hat)
# 
#     if can_harvest():
#         harvest()
# 
# 
# def wood_gathering():
# 
#     change_hat(Hats.brown_Hat)
# 
#     gather_and_plant(Entities.Tree)
# 
# 
# def bone_gathering():
# 
#     change_hat(Hats.Dinosaur_Hat)
# 
#     if can_harvest():
#         harvest()
# 
# 
# def carrot_gathering():
# 
#     change_hat(Hats.brown_Hat)
# 
#     gather_and_plant(Entities.Carrot)
# 
# 
# def pumpkin_gathering():
# 
#     change_hat(Hats.brown_Hat)
# 
#     gather_and_plant(Entities.Pumpkin)
# 
# 
# def cactus_gathering():
# 
#     change_hat(Hats.brown_Hat)
# 
#     gather_and_plant(Entities.Cactus)
# 
# 
# def fertilizer_gathering():
# 
#     change_hat(Hats.brown_Hat)
# 
#     if can_harvest():
#         harvest()
# 
# 
# def next_move(route, count):
# 
#     direction = route[count]
# 
#     if direction == "north":
#         move(North)
# 
#     elif direction == "south":
#         move(South)
# 
#     elif direction == "west":
#         move(West)
# 
#     elif direction == "east":
#         move(East)
# 
# 
# def smallest_item():
# 
#     items = [
#         Items.Hay,
#         Items.Wood,
#         Items.Carrot,
#         Items.Pumpkin,
#         Items.Cactus,
#         Items.Bone,
#         Items.Fertilizer
#     ]
# 
#     smallest = items[0]
#     smallest_num = num_items(smallest)
# 
#     for item in items:
# 
#         count = num_items(item)
# 
#         if count < smallest_num:
#             smallest_num = count
#             smallest = item
# 
#     return smallest
# 
# 
# 
# def job():
# 
#     smallest = smallest_item()
# 
#     if smallest == Items.Hay:
#         return "hay"
# 
#     elif smallest == Items.Wood:
#         return "tree"
# 
#     elif smallest == Items.Carrot:
#         return "carrot"
# 
#     elif smallest == Items.Pumpkin:
#         return "pumpkin"
# 
#     elif smallest == Items.Cactus:
#         return "cactus"
# 
#     elif smallest == Items.Fertilizer:
#         return "fertilizer"
# 
#     elif smallest == Items.Bone:
#         return "bone"
# 
# def select_route(job):
# 
# 	if job == "hay":
# 		size = get_world_size()
# 		route = []
# 
# 		for x in range(size):
# 			direction = "north"
# 
# 			if x % 2 != 0:
# 				direction = "south"
# 
# 			for y in range(size - 1):
# 				route.append(direction)
# 
# 			if x < size - 1:
# 				route.append("east")
# 
# 		return route
# 
# 
# 	elif job == "tree":
# 		size = get_world_size()
# 		route = []
# 
# 		for x in range(size):
# 			direction = "north"
# 
# 			if x % 2 != 0:
# 				direction = "south"
# 
# 			for y in range(size - 1):
# 				route.append(direction)
# 
# 			if x < size - 1:
# 				route.append("east")
# 
# 		return route
# 
# 	elif job == "bone":
# 		size = get_world_size()
# 		route = []
# 
# 		for x in range(size):
# 			direction = "north"
# 
# 			if x % 2 != 0:
# 				direction = "south"
# 
# 			for y in range(size - 1):
# 				route.append(direction)
# 
# 			if x < size - 1:
# 				route.append("east")
# 
# 		return route
# 
# 	elif job == "carrot":
# 		size = get_world_size()
# 		route = []
# 
# 		for x in range(size):
# 			direction = "north"
# 
# 			if x % 2 != 0:
# 				direction = "south"
# 
# 			for y in range(size - 1):
# 				route.append(direction)
# 
# 			if x < size - 1:
# 				route.append("east")
# 
# 		return route
# 
# 	elif job == "pumpkin":
# 		size = get_world_size()
# 		route = []
# 
# 		for x in range(size):
# 			direction = "north"
# 
# 			if x % 2 != 0:
# 				direction = "south"
# 
# 			for y in range(size - 1):
# 				route.append(direction)
# 
# 			if x < size - 1:
# 				route.append("east")
# 
# 		return route
# 
# 	elif job == "cactus":
# 		size = get_world_size()
# 		route = []
# 
# 		for x in range(size):
# 			direction = "north"
# 
# 			if x % 2 != 0:
# 				direction = "south"
# 
# 			for y in range(size - 1):
# 				route.append(direction)
# 
# 			if x < size - 1:
# 				route.append("east")
# 
# 		return route
# 
# 	elif job == "fertilizer":
# 		size = get_world_size()
# 		route = []
# 
# 		for x in range(size):
# 			direction = "north"
# 
# 			if x % 2 != 0:
# 				direction = "south"
# 
# 			for y in range(size - 1):
# 				route.append(direction)
# 
# 			if x < size - 1:
# 				route.append("east")
# 
# 		return route
# 
# 	return []
# 
# def gathering_step(state):
# 
#     if polyculture_step():
#         return
# 
#     current_job = state["job"]
# 
#     if current_job == "hay":
#         hay_gathering()
# 
#     elif current_job == "tree":
#         wood_gathering()
# 
#     elif current_job == "carrot":
#         carrot_gathering()
# 
#     elif current_job == "pumpkin":
#         pumpkin_gathering()
# 
#     elif current_job == "cactus":
#         cactus_gathering()
# 
#     elif current_job == "bone":
#         bone_gathering()
# 
#     elif current_job == "fertilizer":
#         fertilizer_gathering()
# 
# def main():
# 
#     clear()
# 
#     while True:
# 
#         next_job = job()
# 
#         state = {
#             "job": next_job,
#             "step": 0,
#             "route": select_route(next_job)
#         }
# 
#         for i in range(len(state["route"]) + 1):
# 
#             state["step"] = i
# 
#             gathering_step(state)
# 
#             if i < len(state["route"]):
#                 next_move(state["route"], i)
# 
# if __name__ == "__main__":
#     main()











# ============================================================
# SINGLE-DRONE VERSION (ИСПРАВЛЕНА ПОД СИНТАКСИС ИГРЫ)
# ============================================================

companions = {}      # (x, y) -> entity, которую просят как компаньона
bad_tiles = []       # для тыкв: координаты проблемных клеток

# ---------- БАЗОВЫЕ УТИЛИТЫ ----------

def go_to(x, y):
	size = get_world_size()
	while get_pos_x() != x:
		if (get_pos_x() - x) % size <= size // 2:
			move(West)
		else:
			move(East)
	while get_pos_y() != y:
		if (get_pos_y() - y) % size <= size // 2:
			move(South)
		else:
			move(North)


def sweep(step_func):

	size = get_world_size()
	for column in range(size):
		# Исправлено: убрали тернарный оператор
		if column % 2 == 0:
			direction = North
		else:
			direction = South
			
		for row in range(size):
			step_func()
			if row < size - 1:
				move(direction)
		if column < size - 1:
			move(East)


def till_if_needed():
	if get_ground_type() != Grounds.Soil:
		till()


# ---------- ПОЛИКУЛЬТУРА + ПОСАДКА ----------

def plant_tile(main_crop):
	
	pos = (get_pos_x(), get_pos_y())

	# Сначала собираем урожай, если он есть
	if can_harvest():
		harvest()

	# Если на эту клетку была заявка — сажаем компаньона
	if pos in companions:
		want = companions.pop(pos)
		till_if_needed()
		plant(want)
		return

	# Иначе сажаем основную культуру
	if main_crop == Entities.Carrot:
		till_if_needed()
	if main_crop == Entities.Tree:
		till_if_needed()

	plant(main_crop)

	# Запоминаем заявку этого растения
	result = get_companion()
	if result != None:
		want, target = result
		if target not in companions:
			companions[target] = want


def harvest_and_polyculture(crop):
	plant_tile(crop)


# ---------- СЕНО / ДЕРЕВО / МОРКОВЬ (ПОЛИКУЛЬТУРА) ----------

def hay_gathering():
	change_hat(Hats.Brown_Hat)
	harvest_and_polyculture(Entities.Grass)


def wood_gathering():
	change_hat(Hats.Brown_Hat)
	harvest_and_polyculture(Entities.Tree)


def carrot_gathering():
	change_hat(Hats.Brown_Hat)
	harvest_and_polyculture(Entities.Carrot)


# ---------- ТЫКВЫ (ОТСЛЕЖИВАНИЕ ПЛОХИХ КЛЕТОК) ----------

def pumpkin_gathering():
	change_hat(Hats.Brown_Hat)

	global bad_tiles
	bad_tiles = []

	# Первичный проход: сажаем везде, где пусто/мертво
	def first_pass():
		if get_entity_type() == Entities.Dead_Pumpkin:
			harvest()
		if can_harvest():
			harvest()
		if get_entity_type() != Entities.Pumpkin:
			till_if_needed()
			plant(Entities.Pumpkin)
		if not can_harvest():
			bad_tiles.append((get_pos_x(), get_pos_y()))

	sweep(first_pass)

	# Повторяем, пока есть проблемные клетки
	while len(bad_tiles) > 0:
		x, y = bad_tiles.pop(0)
		go_to(x, y)

		if get_entity_type() == Entities.Dead_Pumpkin:
			harvest()
		if can_harvest():
			harvest()
		if get_entity_type() != Entities.Pumpkin:
			till_if_needed()
			plant(Entities.Pumpkin)

		if not can_harvest():
			bad_tiles.append((x, y))

	# Когда все клетки готовы — собираем гигантскую тыкву
	harvest()

# ---------- ПОДСОЛНУХИ (ЭНЕРГИЯ) ----------

def sunflower_gathering():
	change_hat(Hats.Brown_Hat)
	
	if get_entity_type() == Entities.Sunflower:
		if can_harvest():
			# Собираем только те, у которых 15 лепестков (максимум энергии)
			# Если лепестков меньше, оставляем расти (занимаем место, но экономим ходы)
			if measure() == 15:
				harvest()
				# Сразу сажаем новый на освободившееся место
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Sunflower)
	else:
		# Если клетка пустая — сажаем подсолнух
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)

	
# ---------- КАКТУСЫ (SHEAR SORT ТОЛЬКО ЗРЕЛЫХ) ----------

def sort_cacti():

	size = get_world_size()

	def sort_line(direction, length):

		for _ in range(length - 1):
			for _ in range(length - 1):
				if get_entity_type() == Entities.Cactus and can_harvest():
					current = measure()
					neighbor = measure(direction)
					if current != None and neighbor != None:
						if current > neighbor:
							swap(direction)
				move(direction)
			# Возвращаемся в начало линии
			for _ in range(length - 1):
				move(opposite(direction))

	# Строки
	for y in range(size):
		go_to(0, y)
		sort_line(East, size)

	# Столбцы
	for x in range(size):
		go_to(x, 0)
		sort_line(North, size)


def opposite(direction):
	# Исправлено: убрали однострочные return, чтобы не было ошибок
	if direction == North:
		return South
	if direction == South:
		return North
	if direction == East:
		return West
	if direction == West:
		return East


def cactus_gathering():
	change_hat(Hats.Brown_Hat)

	if get_entity_type() != Entities.Cactus:
		till_if_needed()
		plant(Entities.Cactus)

	if can_harvest():
		sort_cacti()
		harvest()


# ---------- КОСТИ (ПРОСТАЯ ЗМЕЙКА) ----------

def bone_gathering():
	change_hat(Hats.Dinosaur_Hat)

	steps = 0
	max_steps = get_world_size() * get_world_size() * 4

	while steps < max_steps:
		if get_entity_type() == Entities.Apple:
			harvest()

		if get_pos_x() < get_world_size() - 1:
			move(East)
		elif get_pos_y() < get_world_size() - 1:
			move(North)
		else:
			move(West)

		steps += 1


# ---------- ПРИОРИТЕТЫ ----------

# def choose_job():
#     if num_items(Items.Hay) < 500:
#         return "hay"
#     if num_items(Items.Wood) < 300:
#         return "tree"
#     if num_items(Items.Carrot) < 200:
#         return "carrot"
#     if num_items(Items.Pumpkin) < 100:
#         return "pumpkin"
#     if num_items(Items.Cactus) < 50:
#         return "cactus"
#     if num_items(Items.Bone) < 20:
#         return "bone"
# 
#     return "hay"

def choose_job():
	if num_items(Items.Hay) < 500:
		return "hay"
	if num_items(Items.Wood) < 300:
		return "tree"
	if num_items(Items.Carrot) < 200:
		return "carrot"
	if num_items(Items.Pumpkin) < 100:
		return "pumpkin"
	if num_items(Items.Cactus) < 50:
		return "cactus"
	
	# ДОБАВЛЕНО: Если энергии мало - идем за подсолнухами
	if num_items(Items.Power) < 50:
		return "sunflower"
		
	if num_items(Items.Bone) < 20:
		return "bone"

	return "hay"


# ---------- MAIN ----------

# def main():
#     clear()
# 
#     while True:
#         job = choose_job()
# 
#         if job == "hay":
#             sweep(hay_gathering)
#         elif job == "tree":
#             sweep(wood_gathering)
#         elif job == "carrot":
#             sweep(carrot_gathering)
#         elif job == "pumpkin":
#             pumpkin_gathering()
#         elif job == "cactus":
#             sweep(cactus_gathering)
#         elif job == "bone":
#             bone_gathering()

def main():
	clear()

	while True:
		job = choose_job()

		if job == "hay":
			sweep(hay_gathering)
		elif job == "tree":
			sweep(wood_gathering)
		elif job == "carrot":
			sweep(carrot_gathering)
		elif job == "pumpkin":
			pumpkin_gathering()
		elif job == "cactus":
			sweep(cactus_gathering)
			
		# ДОБАВЛЕНО: Обработка подсолнухов
		elif job == "sunflower":
			sweep(sunflower_gathering)
			
		elif job == "bone":
			bone_gathering()
if __name__ == "__main__":
	main()

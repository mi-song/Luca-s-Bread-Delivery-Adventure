import os
import pygame

image_folder_path = "C:/Users/rlaqhdrb/Desktop/pygame/resource/배경제거"

"""
image path 
"""

#### ingredient ####

one_butter_image_path = os.path.join(image_folder_path, "낱개버터_.png")
butter_image_path = os.path.join(image_folder_path, "버터통_.png")

caraway_seed_image_path = os.path.join(image_folder_path, "카라웨이씨알_.png")
caraway_image_path = os.path.join(image_folder_path, "카라웨이씨통_.png")

tilted_milk_image_path = os.path.join(image_folder_path, "기울어진우유_.png")
milk_image_path = os.path.join(image_folder_path, "우유_.png")
pouring_milk_image_path = os.path.join(image_folder_path, "흐르는우유_.png")

water_image_path = os.path.join(image_folder_path, "물담긴통_.png")
pouring_water_image_path = os.path.join(image_folder_path, "흐르는물통_.png")

flour_image_path = os.path.join(image_folder_path, "밀가루봉지_.png")
# flour_with_powder_image = os.path.join(image_folder_path, "밀가루가루_.png")

spreading_salt_image_path = os.path.join(image_folder_path, "소금뿌리기_.png")
salt_image_path = os.path.join(image_folder_path, "소금통_.png")

bowl_image_path = os.path.join(image_folder_path, "그릇_.png")

#### equipment ####

spoon_image_path = os.path.join(image_folder_path, "계량스푼_.png")
spoon_with_powder_image_path = os.path.join(image_folder_path, "담긴계량스푼_.png")
pouring_powder_image_path = os.path.join(image_folder_path, "밀가루가루_.png")

oven_image_path = os.path.join(image_folder_path, "오븐_.png")

order_sheet_image_path = os.path.join(image_folder_path, "주문서_.png")

#### bread ####

dough_image_path = os.path.join(image_folder_path, "반죽_.png")

cooked_baguette_image_path = os.path.join(image_folder_path, "바게트_.png")
baguette_dough_image_path = os.path.join(image_folder_path, "바게트반죽_.png")
burnt_baguette_image_path = os.path.join(image_folder_path, "탄바게트_.png")

croissant_dough_image_path = os.path.join(image_folder_path, "크루와상 반죽_.png")
cooked_croissant_image_path = os.path.join(image_folder_path, "크루와상_.png")
burnt_croissant_image_path = os.path.join(image_folder_path, "탄크루와상_.png")

cooked_bread_image_path = os.path.join(image_folder_path, "식빵_.png")
bread_dough_image_path = os.path.join(image_folder_path, "식빵반죽_.png")
burnt_bread_image_path = os.path.join(image_folder_path, "탄식빵_.png")

cooked_pretzel_image_path = os.path.join(image_folder_path, "프레젤_.png")
pretzel_dough_image_path = os.path.join(image_folder_path, "프레젤반죽_.png")
burnt_pretzel_image_path = os.path.join(image_folder_path, "탄프레젤_.png")

cooked_ryebread_image_path = os.path.join(image_folder_path, "호밀빵_.png")
ryebread_dough_image_path = os.path.join(image_folder_path, "호밀빵반죽_.png")
burnt_ryebread_image_path = os.path.join(image_folder_path, "탄호밀빵_.png")


"""
image road 
"""

#### ingredient ####

one_butter_image = pygame.image.load(one_butter_image_path)
one_butter_image = pygame.transform.scale(one_butter_image, (100, 100))

butter_image = pygame.image.load(butter_image_path)
butter_image = pygame.transform.scale(butter_image, (100, 100))

caraway_seed_image = pygame.image.load(caraway_seed_image_path)
caraway_seed_image = pygame.transform.scale(caraway_seed_image, (100, 100))

caraway_image = pygame.image.load(caraway_image_path)
caraway_image = pygame.transform.scale(caraway_image, (100, 100))

tilted_milk_image = pygame.image.load(tilted_milk_image_path)
tilted_milk_image = pygame.transform.scale(tilted_milk_image, (100, 100))

milk_image = pygame.image.load(milk_image_path)
milk_image = pygame.transform.scale(milk_image, (100, 100))

pouring_milk_image = pygame.image.load(pouring_milk_image_path)
pouring_milk_image = pygame.transform.scale(pouring_milk_image, (100, 100))

water_image = pygame.image.load(water_image_path)
water_image = pygame.transform.scale(water_image, (100, 100))

pouring_water_image = pygame.image.load(pouring_water_image_path)
pouring_water_image = pygame.transform.scale(pouring_water_image, (100, 100))

flour_image = pygame.image.load(flour_image_path)
flour_image = pygame.transform.scale(flour_image, (100, 100))

spreading_salt_image = pygame.image.load(spreading_salt_image_path)
spreading_salt_image = pygame.transform.scale(spreading_salt_image, (100, 100))

salt_image = pygame.image.load(salt_image_path)
salt_image = pygame.transform.scale(salt_image, (100, 100))

bowl_image = pygame.image.load(bowl_image_path)
bowl_image = pygame.transform.scale(bowl_image, (100, 100))

#### equipment ####

spoon_image = pygame.image.load(spoon_image_path)
spoon_image = pygame.transform.scale(spoon_image, (100, 100))

spoon_with_powder_image = pygame.image.load(spoon_with_powder_image_path)
spoon_with_powder_image = pygame.transform.scale(spoon_with_powder_image, (100, 100))

pouring_powder_image = pygame.image.load(pouring_powder_image_path)
pouring_powder_image = pygame.transform.scale(pouring_powder_image, (100, 100))

oven_image = pygame.image.load(oven_image_path)
oven_image = pygame.transform.scale(oven_image, (100, 100))

order_sheet_image = pygame.image.load(order_sheet_image_path)
order_sheet_image = pygame.transform.scale(order_sheet_image, (100, 100))

#### bread ####

dough_image = pygame.image.load(dough_image_path)
dough_image = pygame.transform.scale(dough_image, (100, 100))

cooked_baguette_image = pygame.image.load(cooked_baguette_image_path)
cooked_baguette_image = pygame.transform.scale(cooked_baguette_image, (100, 100))

baguette_dough_image = pygame.image.load(baguette_dough_image_path)
baguette_dough_image = pygame.transform.scale(baguette_dough_image, (100, 100))

burnt_baguette_image = pygame.image.load(burnt_baguette_image_path)
burnt_baguette_image = pygame.transform.scale(burnt_baguette_image, (100, 100))

croissant_dough_image = pygame.image.load(croissant_dough_image_path)
croissant_dough_image = pygame.transform.scale(croissant_dough_image, (100, 100))

cooked_croissant_image = pygame.image.load(cooked_croissant_image_path)
cooked_croissant_image = pygame.transform.scale(cooked_croissant_image, (100, 100))

burnt_croissant_image = pygame.image.load(burnt_croissant_image_path)
burnt_croissant_image = pygame.transform.scale(burnt_croissant_image, (100, 100))

cooked_bread_image = pygame.image.load(cooked_bread_image_path)
cooked_bread_image = pygame.transform.scale(cooked_bread_image, (100, 100))

bread_dough_image = pygame.image.load(bread_dough_image_path)
bread_dough_image = pygame.transform.scale(bread_dough_image, (100, 100))

burnt_bread_image = pygame.image.load(burnt_bread_image_path)
burnt_bread_image = pygame.transform.scale(burnt_bread_image, (100, 100))

cooked_pretzel_image = pygame.image.load(cooked_pretzel_image_path)
cooked_pretzel_image = pygame.transform.scale(cooked_pretzel_image, (100, 100))

pretzel_dough_image = pygame.image.load(pretzel_dough_image_path)
pretzel_dough_image = pygame.transform.scale(pretzel_dough_image, (100, 100))

burnt_pretzel_image = pygame.image.load(burnt_pretzel_image_path)
burnt_pretzel_image = pygame.transform.scale(burnt_pretzel_image, (100, 100))

cooked_ryebread_image = pygame.image.load(cooked_ryebread_image_path)
cooked_ryebread_image = pygame.transform.scale(cooked_ryebread_image, (100, 100))

ryebread_dough_image = pygame.image.load(ryebread_dough_image_path)
ryebread_dough_image = pygame.transform.scale(ryebread_dough_image, (100, 100))

burnt_ryebread_image = pygame.image.load(burnt_ryebread_image_path)
burnt_ryebread_image = pygame.transform.scale(burnt_ryebread_image, (100, 100))
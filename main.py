#Objektumok 

# Step 1 - Create a class

from Food import Food
from Worker import Worker
from functions import print_menu, get_foods_average_cost, get_most_expensive_food_name, get_pay_sum, get_oldest_worker_name, get_number_of_beosztott, get_name_of_smallest_payed

food1 = Food("Húsleves",23000,1.9)
food2 = Food("Husi",10000,2.3)
food3 = Food("Popcorn",340,0.2)
food4 = Food("Sandwich",400,0.1)

foodsList:list = []
foodsList.append(food1)
foodsList.append(food2)
foodsList.append(food3)
foodsList.append(food4)

food1.makefood()

print_menu(foodsList)
print(f"Az ételek átlag ára: {get_foods_average_cost(foodsList)}")

print(f"A legdrágább étel: {get_most_expensive_food_name(foodsList)}")


workersList:list = [Worker("Alma Aladár", 1982, 250000, "Programozó"), Worker("Banán Béla", 1977, 300000, "Mérnők"), Worker("Sajt Sára", 2001, 500000, "Grafikus"), Worker("Narancs Nóra", 1991, 990000, "Marketinges"), Worker("Eper Elemér", 1979, 1500000, "COO")]

print(f"\nA dolgozók össz fizetése: {get_pay_sum(workersList)}")
print(f"A legidősebb dolgozó: {get_oldest_worker_name(workersList)}")
print(f"{get_number_of_beosztott(workersList)} \"beosztott\" van")
print(f"A legkevesebbet kereső dolgozó: {workersList[get_name_of_smallest_payed(workersList)]}")

print(f"\n{workersList[get_name_of_smallest_payed(workersList)]}")
workersList[get_name_of_smallest_payed(workersList)].give_raise(15)
print(f"{workersList[get_name_of_smallest_payed(workersList)]}")

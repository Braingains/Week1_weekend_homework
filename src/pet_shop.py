# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(shop):
    return shop ["name"]

def get_total_cash(cash):
    return cash ["admin"]["total_cash"]

def add_or_remove_cash(current_cash, cash_added_or_removed):
    current_cash["admin"]["total_cash"] += cash_added_or_removed
#this works for both q3 and 4, because adding a negative is the same as taking away

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(current_pets_sold, additional_pets_sold):
    current_pets_sold["admin"]["pets_sold"] += additional_pets_sold

def get_stock_count(pet_stock):
    return len(pet_stock["pets"])

def get_pets_by_breed(pet_shop, breed):
    animals = []
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            animals.append(pet)
    return animals

def find_pet_by_name(pet_shop, name):
    found_pet = None
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            found_pet = pet
    return found_pet

def remove_pet_by_name(pet_shop, name):
    counter = 0
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            del(pet_shop["pets"][counter])
        else: counter += 1

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    for customer in customers:
        return customers["cash"]

def remove_customer_cash(customer, amount_removed):
    customer["cash"] -= amount_removed

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else: return False
    

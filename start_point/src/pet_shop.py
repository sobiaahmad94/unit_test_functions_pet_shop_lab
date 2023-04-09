# 1. Get pet shop name
# put pet_shop_name in the parameter
# look at cc_pet_shop dict
# the name is in the cc_pet_shop dict, at the end - "Camelot of Pets"
# grab ["name"] key to get the value
# "name" : "Camelot of Pets"
def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

# 2. Get total cash
# look for total_cash, found it in pet_shop dict
# pet_shop dict --> ["admin"] key which eventually leads to 1000 which is the total_cash
# pet_shop dict --> ["admin"] key --> ["total_cash"]
# create get_total_cash function
# pass in pet_shop in the parameter
# return total_cash key
def get_total_cash(pet_shop):
    pet_shop_total_cash = pet_shop["admin"]["total_cash"]
    return pet_shop_total_cash

# # 3 and 4. Add or remove cash
# # I think cash is in reference to pet_shop dict again, not customers list
# # pet_shop dict --> ["admin"] key --> ["total_cash"]
# # total_cash is 1000 and test shows 990 
# # create add_or_remove_cash function
# # add pet_shop to the parameter 
# # add cash_deduct_amount - so the user would for example give 10 to be deducted
# # create pet_shop_total_cash var as in the previous question, that var had local scope
# # make pet_shop_total_cash equal to 1000 value using the keys
# # return pet_shop_total_cash and - 10
# def add_or_remove_cash(pet_shop, cash_amount):
#     pet_shop_total_cash = pet_shop["admin"]["total_cash"]
#     return pet_shop_total_cash - 10

# # Add or remove cash (I think it's a continuation from the previous question)
# # def add_or_remove_cash(pet_shop, cash_plus_amount):
# #     pet_shop_total_cash = pet_shop["admin"]["total_cash"]
# #     return pet_shop_total_cash + 10
# # The test for the 4th test function hasn't passed

# # 5. Gets pets sold
# # pet_shop dict --> ["admin"] key --> "pets_sold" (value is 0)
# # create get_pets_sold function
# # pass in pet_shop as a parameter
# # create a variable called all_pets_sold
# # go to dict pet_shop as that's where pet_sold key is
# # do pet_shop --> ["admin"] --> ["pets_sold"] - store this in all_pets_sold
# # return all_pets_sold var
def get_pets_sold(pet_shop):
    all_pets_sold = pet_shop["admin"]["pets_sold"]
    return all_pets_sold

# # 6. Increase pets sold
# # pet_shop dict --> ["admin"] key --> ["pets_sold"] key, contains value 0
# # create function increase_pets_sold
# # pass in pet_shop and pets_sold as parameters
# # create current_pets_sold var and store pets_sold key by following my steps above
# # create a var called updated_pets_sold
# # I can see that there have been 6 pets sold
# # print(len(pet_shop["name"]) - it didn't work but that's how I'd get the number of items in a list
# # return updated_pets_sold
# # set updated_pets_sold equal to current_pets_sold + 6
def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

# 7. Get stock count
#  pet_shop dict --> pets list - ["pets"] key for list
# create get_stock_count function
# add pet_shop as a parameter
# create total_pet_stock_count var
# assign total_get_stock_count var to pet_shop["pets"]
# use the len function on the pet_shop["pets"] key
# return total_pet_stock_count
# # use len() to get the number of pets in the pets list
def get_stock_count(pet_shop):
    total_pet_stock_count = len(pet_shop["pets"])
    return total_pet_stock_count

# 8. and 9. Get pets by breed
# pet_shop dict --> pets list --> ["breed"] key
# create get_pets_by_breed function
# add pet_shop and pet_breed as parameters
# create an empty pets list (didn't work when I set it to 0)
# do a for loop
# for pet in pet_shop ["pets"] key
# if pet ["breed"] key is the same as pet_breed 
# then add the pet to the pets list
# use insert(0, "Pikachu") - add it to the front, index 0
# return pets list

# my example:
# pokemon_pokedex_numbers = [10, 4, 25, 7, 96, 39, 26, 52] 
# even_pokedex_numbers = []

# for pokedex_number in pokemon_pokedex_numbers:
#     if pokedex_number % 2 == 0:
#         even_pokedex_numbers.append(pokedex_number)
# print(even_pokedex_numbers)

def get_pets_by_breed(pet_shop, pet_breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pets.insert(0, pet)
    return pets

# 10. Find pet by name
# create find_pet_by_name function
# pass in pet_shop and pet_name
# pet shop dict --> pets list --> ["name"] key
# create an empty pets list
# use a for loop
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# 11. Remove pet by name
# pet_shop dict --> ["pets"] list --> ["name"] key
# use find pet function and store it in a var called pet
# grab ["pets"] key then use remove() to take out pet
def remove_pet_by_name(pet_shop, pet_name):
    pet = find_pet_by_name(pet_shop, pet_name)
    pet_shop["pets"].remove(pet)

# 12. Add pet to stock
# pet_shop dict --> ["pets"] key contains list
# create add_pet_to_stock function
# pass in pet_shop and new_pet as parameters
# create var updated_pet_stock
# store pet_shop["pets"] in updated_pet_stock
# use insert(0, "Pikachu") to add to the list, index 0
def add_pet_to_stock(pet_shop, new_pet):
    updated_pet_stock = pet_shop["pets"].insert(0, new_pet)
    return updated_pet_stock

# 13. Get customer cash
# customers list --> ["cash"] key in list of dicts
# create get_customer_cash function
# pass in customer
# create customers_cash var and store customer dict and pass ["cash"] key
def get_customer_cash(customer):
    customers_cash = customer["cash"]
    return customers_cash

# 14. Remove customer cash
# I'm stuck on this question so I will ask about it and try again later.
# def remove_customer_cash(customer, cash_amount):
#     customers_cash_removed = customer["cash"]

# 15. Get customer pet count
# customers dict --> ["pets"] key
# use len function on ["pets"] key to get length of list
# create customer_pet_count function
# return total_pets
def get_customer_pet_count(customer):
    total_pets = len(customer["pets"])
    return total_pets

# 16. Add pet to customer
# customers dict --> ["pets"] key
# create add_pet_to_customer function
# pass in customer and new_pet
# create customer_new_pet var 
# grab ["pets"] key (empty [])
# then insert(0, "Pikachu") to insert new_pet
# return customer_new_pet
def add_pet_to_customer(customer, new_pet):
    customer_new_pet = customer["pets"].insert(0, new_pet)
    return customer_new_pet












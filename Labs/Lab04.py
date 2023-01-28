# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program sees if you can buy a hotel for pennsylvania avenue.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out the math for the purcase options.
# 5. How long did it take for you to complete the assignment?
#      2 hours
# Page start.
print()

# Functions and Varables.
cont = 1

def compute_price(houses, hotels):
    houses_price = houses * 200
    hotels_price = hotels * 200
    price = houses_price + hotels_price
    return price

def compute_num_houses_total(pc, nc, pa):
    total = 12
    
    if pc < 5:
        total -= pc
    else:
        total -= 4

    if nc < 5:
        total -= nc
    else:
        total -= 4

    if pa < 5:
        total -= pa
    else:
        total -= 4

    return total

def compute_num_hotels_total(pc, nc, pa):
    if pc == 5 or nc == 5 or pa == 5:
        return 0
    else:
        return 1

def opt_A(price, houses, nc, pc):
    houses_nc = 4 - nc
    houses_pc = 4 - pc
    print(f"""This will cost ${price}.
         Purchase 1 hotel and {houses} house(s).
         Put 1 hotel on Pennsylvania and return any houses to the bank.
         Put {houses_nc} house(s) on North Carolina.
         Put {houses_pc} house(s) on Pacific.""")

def opt_B(price, houses, nc):
    houses_nc = 4 - nc
    print(f"""This will cost ${price}.
         Purchase 1 hotel and {houses} house(s).
         Put 1 hotel on Pennsylvania and return any houses to the bank.
         Put {houses_nc} house(s) on North Carolina.""")

def opt_C(price, houses, pc):
    houses_pc = 4 - pc
    print(f"""This will cost ${price}.
         Purchase 1 hotel and {houses} house(s).
         Put 1 hotel on Pennsylvania and return any houses to the bank.
         Put {houses_pc} house(s) on Pacific.""")

def opt_D(price, houses):
    print(f"""This will cost ${price}.
         Purchase 1 hotel and {houses} house(s).
         Put 1 hotel on Pennsylvania and return any houses to the bank.""")

# main code
while cont == 1:
    # inputs from user
    pc_in = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    nc_in = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    pa_in = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    cash_in = int(input("How much cash do you have to spend? "))
    houses_in = int(input("How many houses are there to purchase? "))
    hotels_in = int(input("How many hotels are there to purchase? "))
    prop_yn = input("Do you own all the green properties? (y/n) ")

    # page set up
    print()

    # procedures
    house = compute_num_houses_total(pc_in, nc_in, pa_in)
    hotel = compute_num_hotels_total(pc_in, nc_in, pa_in)
    price = compute_price(house, hotel)
    if prop_yn == "y":
        if pa_in == 5:
            print("You cannot purchase a hotel if the property already has one.")
        elif pa_in == 4 and nc_in == 5:
            print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
        elif pa_in == 4 and pc_in == 5:
            print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
        else:
            if houses_in > 0:
                if hotels_in > 0:
                    if cash_in >= price:
                        if nc_in < 4 and pc_in < 4:
                            opt_A(price, house, nc_in, pc_in)
                        elif nc_in < 4:
                            opt_B(price, house, nc_in)
                        elif pc_in < 4:
                            opt_C(price, house, pc_in)
                        else:
                            opt_D(price, house)
                    else:
                        print("You do not have sufficient funds to purchase a hotel at this time.")
                else:
                    print("There are not enough hotels available for purchase at this time.")
            else:
                print("There are not enough houses available for purchase at this time.")
    else:
        print("You cannot purchase a hotel until you own all the properties of a given color group.")

    # page end
    print()
    cont = int(input("Continue: "))
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!\n")



print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10+5, 5+6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Finally, we can accept your own inputs:")
cheese_count = float(input("How many blocks cheese do you have? "))
crackers = float(input("How many crackers do you have? "))
cheese_and_crackers(cheese_count, crackers)
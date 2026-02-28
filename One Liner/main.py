

#! Conditional One Liner 
name = "Nifad"
print("It's Nifad😊") if name == "Nifad" else print("It's not Nifad 😔")


#! Loop One Liner
numbers = [10, 50, 150, 200, 75, 25]

is_less_than_100 = [1 if num < 100 else 0 for num in numbers]
print(is_less_than_100)  # Output: [1, 1, 0, 0, 1, 1]

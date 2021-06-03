def user_info(name="unknown", last_name="unknown", age="none"):
    print(f"your name is {name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
    print("\n")

user_info("Rushikesh", "Gaikwad", 69)
# user_info("Rushikesh", 69) #error
user_info("Rushikesh", "Gaikwad")
user_info("Rushikesh")
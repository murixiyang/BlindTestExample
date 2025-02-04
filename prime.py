def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def who_am_i(name: str):
    return f"Hello, I am {name}!"

# Input from the user
name = input("Enter your name: ")
print(who_am_i(name))

n = int(input("Check this number:> "))


def prime_checker(n):
    if n == 0:
        print(f"{n} is neither prime number nor composite number")
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 :
        print(f"{n} is not prime number")
    else:
        print(f"{n} is prime number")


# prime_checker(n)

# def prime_checker(n):
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} is not prime number")
#             is_prime = False
#     if is_prime:
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} is not prime number")


prime_checker(n)

def main():
    number_of_times = int(input("Choose the number of times you want to spam. "))
    message = input("What message do you want to spam? ")
    for _ in range(number_of_times):
        print(message)
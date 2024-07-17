import random
import time

def generate_random_guess():
    return ''.join([str(random.randint(0, 9)) for _ in range(7)])

def guess_number(secret_number):
    possible_numbers = [str(i).zfill(7) for i in range(10000000)]
    attempts = 0
    start_time = time.time()
    last_print_time = start_time
    
    while True:
        guess = random.choice(possible_numbers)
        attempts += 1
        current_time = time.time()
        elapsed_time = (current_time - start_time) * 1000  # Convert seconds to milliseconds
        
        if (current_time - last_print_time) >= 0.1:  # Check if 100 milliseconds have passed
            print(f"Elapsed time: {int(elapsed_time)} milliseconds, Attempts so far: {attempts}")
            last_print_time = current_time
        
        if guess == secret_number:
            print(f"Guessed correctly! The number is {guess}. It took {attempts} attempts.")
            break

if __name__ == "__main__":
    secret_number = input("Enter a 7-digit number as the secret number: ")
    while len(secret_number) != 7 or not secret_number.isdigit():
        secret_number = input("Invalid input. Please enter a valid 7-digit number: ")
    guess_number(secret_number)

# Write a code for an algorithm that counts every odd number between two given numbers and also adds them together.

# Input start and stop numbers

start = int(input(f'Input the first number: '))
stop = int(input(f'Input the last number: '))

# initialize variables

count = 0
sum = 0

# Starting a loop

for x in range(start, stop +1):
    if x % 2 !=0:      #Checking if the number is odd
        count += 1
        sum += x

# Show the results

print(f'There are {count} odd numbers and their sum is equal to {sum}.')
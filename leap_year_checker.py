# Leap Year Checker - Chapters 1-3 only
print('=' * 40)
print("     LEAP YEAR CHECKER")
print('=' * 40)
# 1. Ask user for a year (integer)
try:
   year  = int(input('Enter a year: '))
# 2. Leap year rules:
#    - Divisible by 400 → leap year
   if year % 400 == 0:
    print(f'{year} is a leap year')
#    - Divisible by 100 → not leap year
   elif year % 100 == 0:
    print(f'{year} is not a leap year')
#    - Divisible by 4 → leap year
   elif year % 4 == 0:
    print(f'{year} is a leap year')
#    - Everything else → not leap year
   else:
    print(f'{year} is not a leap year')
    
except ValueError:
    print('Invalid input. \nPlease enter an integer year.')
# 3. Use if/elif/else in the correct order
# 4. Print whether it's a leap year or not
# 5. Test with: 2000, 1900, 2024, 2023
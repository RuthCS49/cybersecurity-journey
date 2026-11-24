
"""while True :
   try:
      n = int(input("Enter your number to multiply : "))

   except ValueError:
        print("ONLY DIGITS ARE ALLOWED")
        continue
   if n <= 0:
    print("ONLY NUMBERS FROM  1 ARE ALLOWED!!!")  
    continue
   
   break

for i in range( 1, 16):
    for j in range(i):
     
        break
    print(f"{n} x {i} = {n * i}")
    # print(f" {n * i}", end="")  ( this gives the output only in horizontal way )

"""    
# shows mulitiplication in form of all tables from i to 15

TABLES_PER_ROW = 5
LAST_TABLE = 15
LAST_ROW = 15

for start in range(1, LAST_TABLE + 1, TABLES_PER_ROW):

    # Headings for this group of tables
    for t in range(start, start + TABLES_PER_ROW):
        print(f"{'TABLE OF ' + str(t):<16}", end="")
    print()

    # Each line holds one row from every table in the group
    for row in range(1, LAST_ROW + 1):
        for t in range(start, start + TABLES_PER_ROW):
            print(f"{t:>2} x {row:>2} = {t * row:>3}   ", end="")
        print()

    print()  # blank line between groups

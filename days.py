#Luai Kassem
#2/29/2024
#luai.kassem05@myhunter.cuny.edu 
# This Program implements psuedocode 

Hours = int(input("Enter the number of hours:"))

days = (Hours/24)
days = int(round(days , 0))

leftovers = Hours % 24

print(f"Days: {days}")
print(f"Hours: {leftovers}")

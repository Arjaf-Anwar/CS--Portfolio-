# ==========================================
# B201 Computer Science Lab - Unit Converter
# Student Name: Arjaf Anwar
# Date: June 2026
# ==========================================

print("--- Multi-Purpose Lab Unit Converter ---")
print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Exit")

# Get user selection
choice = input("Select an option (1-3): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    # Standard conversion formula taught in introductory math/CS
    fahrenheit = (celsius * 9/5) + 32
    print(str(celsius) + "°C is equal to " + str(fahrenheit) + "°F")

elif choice == "2":
    km = float(input("Enter distance in Kilometers: "))
    # Standard conversion factor
    miles = km * 0.621371
    print(str(km) + " km is equal to " + str(round(miles, 2)) + " miles")

elif choice == "3":
    print("Thank you for using the lab converter. Goodbye!")

else:
    print("Invalid selection. Please run the script again and choose 1, 2, or 3.")

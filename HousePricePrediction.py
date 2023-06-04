from joblib import load

# Loading the ML model
model = load("HousePriceModel.pkl")

# Infinite loop for prediction prompt
print("******************House Price Prediction***********************")

while True:
    # Taking the user input
    area = float(input("Enter the area (in square feet): "))
    rooms = int(input("Enter the number of rooms: "))
    bedrooms = int(input("Enter the number of bedrooms: "))
    bathrooms = int(input("Enter the number of bathrooms: "))
    stories = int(input("Enter the number of stories: "))
    parking = int(input("Enter the number of parking spaces: "))

    result = model.predict([[area, rooms, bedrooms, bathrooms, stories, parking]])

    # Rounding up the result to 2 decimal places
    price = round(result[0], 2)

    print("Estimated house price: ${:.2f}\n".format(price))

    choice = input("Do you want to continue [y/n]: ")

    if choice.lower() == "n":
        break
    elif choice.lower() == "y":
        print()
    else:
        break
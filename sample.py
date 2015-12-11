# Import the module
import menu3
# Create the menu
m = menu3.Menu(True)
# Set a list of food
food = ["Pizza", "Hot dog", "Salad", "Soup"]
# Ask the user for favorite food
c = m.menu("Please select a favorite food", food)
# Print the food selected
print("You selected: " + food[c-1])

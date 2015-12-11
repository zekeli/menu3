# Import the module
import menu3

# Create the menu
m = menu3.Menu(False)

# Set a list of food
food = ["Pizza", "Hot dog", "Salad", "Soup"]

# Ask the user for favorite food
c = m.menu("Please select a favorite food", food)

# Print the food selected
m.success("You selected: " + food[c-1])

# Create a dict of choices and default values
cfg = {'Your name': "John Doe", 'Your age': 24, 'Your favorite color': "blue", 'Your best friend': "Mickey Mouse"}

# Show a configuration menu, and update the choices
cfg = m.config_menu("Enter your personal details", cfg)

# Show an info message with the new values
m.info(str(cfg))


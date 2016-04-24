import menu3

# Create the menu
m = menu3.Menu(True)

# Set a list of food
food = ["Pizza", "Hot dog", "Salad", "Soup"]

gocs = ["1234", "5678", "2234", "5588"]

# Ask the user for favorite food
c = m.menu2("Please select one or more food", food)
ssc = ", ".join([food[int(i)-1] for i in c])
m.success("You selected:  " + ssc)
g = m.menu2("Please select one or more valid goc, splited by space: ", gocs)

#print(c)

# Print the food selected

ssg = ", ".join([gocs[int(i)-1] for i in g])
m.success("You selected:  " + ssg)


# Create a dict of choices and default values
cfg = {'food': ssc, 'gocs': ssg}

# Show a configuration menu, and update the choices
cfg = m.config_menu("Please review and edit(splited by comma) your choices: ", cfg)

# Show an info message with the new values
m.info(str(cfg))

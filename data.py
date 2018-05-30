# List of the chain of players
# Initial player targets the following player in the list
players = ["Jira", "Kenneth", "Sagar", "Eric", "Rodolfo", "Gio", "Amelia", "Kennedy", "Anissa", "Peter", "Drew",
  "Jessica", "Chris", "Tommy", "Carson", "Brad", "Alexa", "Anna", "Sam", "Tash", "Ryan", "Erica", "Aaron", "Sabina",
  "Derrick", "Grace", "Amanda", "Faith", "Ann Marie", "Kevin", "Maia", "Cha Cha", "Jose", "Lauren", "Gabe", "Tom",
  "Constantine", "Miles", "Sierra", "Olivia", "Mallika", "Carling", "Anh", "Sterling", "Shaggy"]

# List of the order of eliminations
eliminated = ["Erica", "Jira", "Sagar", "Alexa", "Drew", "Sabina", "Anh", "Sam", "Maia", "Mallika", "Constantine",
  "Miles", "Rodolfo", "Jessica", "Grace", "Eric", "Gio", "Amelia", "Kenneth", "Shaggy", "Tash", "Faith", "Olivia",
  "Cha Cha", "Ann Marie", "Sterling", "Carling", "Chris", "Tommy", "Carson", "Peter", "Anna", "Derrick", "Amanda",
  "Lauren", "Jose", "Gabe", "Sierra", "Kennedy", "Ryan", "Aaron", "Kevin", "Tom", "Anissa"]

# Creates a list of colors that correspond to the list of players
# All players are purple, updates the assassin and target of each round to green and red, respectively
colors = []
for i in range(len(players)):
    colors.append('#b2b2ff')

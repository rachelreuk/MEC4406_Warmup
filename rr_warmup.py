# Print name

name = "Rachel"

print(name)

# Count to favourite number squared

favourite_number = 5
squared = favourite_number**2
for i in range(1, squared+1):
  print(i)

# Create Engineers class with associated attributes

class Engineers:
  def __init__ (self, name, type, years_of_experience):
    self.skill = "problem solver"
    self.name = name
    self.type = type
    self.years_of_experience = years_of_experience

  def getSkill(self):
    return self.skill
      
  def getName(self):
    return self.name

  def getType(self):
    return self.type

  def getYears(self):
    return self.years_of_experience
      
# Create two different engineers (objects) and print their attributes

e1 = Engineers("Rachel", "Renewables Engineer", 0.5)
print("------ Engineer 1 ------")
print("Skill: " + e1.getSkill())
print("Name: " + e1.getName())
print("Type: " + e1.getType())
print("Years of experience: ", e1.getYears())

e2 = Engineers("Brett", "Software Engineer", 2.5)
print("------ Engineer 2 ------")
print("Skill: " + e2.getSkill())
print("Name: " + e2.getName())
print("Type: " + e2.getType())
print("Years of experience: ", e2.getYears())

# Change name to be reverse

length = len(name)
reversed_name = ""

for j in range(length-1, -1 , -1):
  reversed_name += name[j]

print(reversed_name)

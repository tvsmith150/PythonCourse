#The int allows conversion from string to number
age = int(input("How old are you?\n"))

#The // allows whole number division
decades = age // 10
#The % or modulus will use the remainder as the years
#Example is 5.9 decades becomes 5 decades and 9 years
years = age % 10

#Convert decades to string
print("You are " + str(decades) + " decades and " + str(years) + " years old.")

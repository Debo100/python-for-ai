# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)

first_name = "Debojit" 
last_name = "Saha"
full_name = first_name + " "+ last_name

long_dash = "-" * 10
print(full_name)
print(long_dash)
len(full_name)

age = 21
can_vote = age>=18


age = 25
has_license = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False


sentence= f"You are wining {full_name}"

temperature = 31
if temperature > 30:
    print("It's very hot")
elif temperature > 25:
    print("it's hot")
else:
    print("It's nice weather")

for i in range(5):
    print(i)

for i in range(1,6):
    print(i)
for i in range(1,10,2):
    print(i)  

#lists
my_list = ["Alice",25,age,True,has_license]
name = my_list[0]
age = my_list[1]

has_license = my_list[-3]

my_list[0]="Dave"
my_list.append("Alice")
my_list.remove("Dave")
my_list.insert(0,"Dave")

def greet():
    print("hello")
    pass

greet()

def check_eligibility(name,age):
    if age>18:
        print(f"{name} is eligible.")
    else:
        print(f"{name} is not eligible.")
    

check_eligibility("Ronty",16)
check_eligibility(name="Arko",age=25)

base = 300000
def salary(exp):
    return base*exp

result =  salary(3)

result

def  number():
    nums = [1,2,3,4,5]
    fn = nums[0]
    ln = nums[-1]
    return fn,ln

f,l = number()

import math
math.sqrt(81)

from math import sqrt,pi
import random
import os
import pandas as pd
sqrt(125)


number = random.randint(1,5000)
print(os.curdir)
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)


import requests


# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()
data["current_units"]["interval"]
print(data)


from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get('API_KEY')
debug = os.environ.get('DEBUG')
dburl=  os.environ.get('DATABASE_URL')


print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")

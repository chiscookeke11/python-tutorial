import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests as rq


# Task one
array = np.arange(1, 11)
meanValue = np.mean(array)

print(meanValue)




# Task two
students = {
    'name': ["Chinedu", "Stella", "Precious"],
    'age': [24, 23, 22]
}

df = pd.DataFrame(students)
print(df)




# Task three

# API URL
url = "https://api.agify.io?name=chinedu"


# send GET request
response = rq.get(url)

# convert the response to JSON format
fetchedData = response.json()


print("Name:", fetchedData["name"])
print("Predicted age:", fetchedData["age"])



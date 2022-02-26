import requests

token = "763a92456d4b4e1ca7ef4e4fae8b0059"

response = requests.get("https://api.spoonacular.com/recipes/complexSearch")

print(response.status_code)
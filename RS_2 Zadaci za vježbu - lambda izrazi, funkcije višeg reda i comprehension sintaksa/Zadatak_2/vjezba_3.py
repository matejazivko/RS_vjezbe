brojevi = [10, 5, 12, 15, 20]
transform = list(map(lambda brojevi: f"{brojevi}:{brojevi**2}", brojevi))
print (transform)
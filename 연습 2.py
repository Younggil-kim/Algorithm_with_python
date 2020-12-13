

string = "123456789"
result = [string[i:i+3] for i in range(0, len(string), 3)]
print(result)

import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
resultArray = []
for text_from_user in response:
    title = text_from_user["title"].capitalize()
    list_from_body = text_from_user["body"].split("\n")
    list_capitalized = []
    for sentence in list_from_body:
        list_capitalized.append(sentence.capitalize())
    body = ". ".join(list_capitalized)
    resultArray.append(title + "\n" + body + "\n")
text_final = '\n'.join(resultArray)

with open("empty_file.txt", "w") as file:
    file.write(text_final)


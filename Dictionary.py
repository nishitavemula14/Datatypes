a = {
    "name":"John",
    "Age": 25,
    "grade":"A"
}
print(a["name"])
print(a.get("Age"))
print(a.pop("grade"))
new_data=a.copy()
print(new_data)
print(a.items())
print(a.keys())
print(a.values())
value = (a.pop("Age"))
print(value)
print(a.popitem())
print(a)
a.update({"Age":25})
print(a)
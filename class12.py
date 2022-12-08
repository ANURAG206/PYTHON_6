# list1=["carry","harry","marie","larry"]
# for item in list1:
#     print(item)
items=[int,float,"harry",5,7,8,855,656,57]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)
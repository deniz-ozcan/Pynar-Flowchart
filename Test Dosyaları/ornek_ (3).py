
import json

x = {
#yorum satırı
    "name": "John",
    "age": 30,
    "city": "New York"
}
x2 = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.dumps(x)

print(y)

if(x>0):
    print("x is greater than 0")
#Yorum satırı
else:
    print("x is less than 0")

a=[1,4,6,7,
4,6,7
    ,6,6,5
    ,6,6,5
        ,64,64,
        64523
]#yorum satırı
#yorum satırı

set1 = {"apple",

     "banana", 
    "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
setx=(1,3,
#yorum satırı

4,5,

#yorum satırı
6)
sety=(1,2,3

,4,5
#yorum satırı
)#yorum satırı
setz=(1,
#yorum satırı
    2,
                    3
            ,4
,5)
print(a)
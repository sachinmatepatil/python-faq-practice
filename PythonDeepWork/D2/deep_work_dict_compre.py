# List & Dict Comprehensions — short way to build collections

#Dict Comprehensions pattern {key_expr: value_expr for item in iterable}

#Expample dict comprehension (word -> length)

texts  = ["sachin","Subhash","Mate","API","Testing"]

length_text = {text: len(text) for text in texts}
print(length_text)

# Dict comprehensions are great in SDET work when:
# Converting lists to lookup maps
# Building config maps
# Counting things, etc
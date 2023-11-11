def myfunc(text, num):
    new_text = ""
    while num > 0:
        new_text = new_text + text
    num = num - 1
    return new_text
    

print(myfunc('Hello', 4))

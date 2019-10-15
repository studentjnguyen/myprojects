tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for x in tokens:
    if x[0] == "<" and x[-1] == ">":
        count = count+1
print("count of xml in tokens is: "+ str(count))

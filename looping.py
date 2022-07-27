#python loops ada 2: while dan for
#Dengan while kita dapat mengeksekusi satu set pernyataan selama kondisinya benar

#WHILE
#i = 1

#while i < 6:
#    print (i)
#    i += 1
#else:
#    print("i is no longer less than 6")

#break statement : With the break statement we can stop the loop even if the while condition is true:
#while i < 6:
#    print(i)
#    if i == 4:
#        break
#    i += 1

#continue statement : With the continue statement we can stop the current iteration, and continue with the next:
#while i < 6:
#    i += 1
#    if i == 4:
#        continue
#    print(i)

#====================FOR======================
adj = ["red", "blue", "green"]
fruits = ["banana", "apple", "watermelon"]
#for x in fruits:
#    print(x)
#for x in "banana": #print per huruf
#    print(x)

#break
#for x in fruits:
#    print(x)
#    if x == "apple":
#        break

#for x in fruits:
#    if x == "apple":
#        break
#    print(x)

#nested loops
for x in adj:
    for y in fruits:
        print(x,y)

#for i in range(1,6):
#    print(i)
#else:
#    print("finished")

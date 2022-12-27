# items = [int, float, "suraj", 6, 7, 88, 98]
# for item in items:
#     if str(item).isnumeric() and item>6:
#         print(item)


# i = 0
# while(i<45):
#     print(i)
#     i = i + 1

# i = 0
# while(i<66):
#     print(i + 1)
#     i = i + 1


n = int(input("Enter your number"))
sum=0
for i in range(1,n+1):
    sum=sum+i

print("sum of the number", sum)

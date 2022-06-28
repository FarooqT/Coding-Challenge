import sys, csv

fileName=input("Please enter the input file name: ")

product, quantity, brand, maxArray, uniqueProducts, file1, file2 = [], [], [], [], [], [], []

#read input file
with open(fileName, 'r') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        product.append((row[2]))
        quantity.append(int((row[3])))
        brand.append((row[4]))

#data structure definitions 
numOfOrders = len(product)
productQuantity = dict()
popularBrand = dict()


#get unique products
for i in product:
    if i not in uniqueProducts:
        uniqueProducts.append(i)


#calculate the total item sold quntatity for each product
for i in range(numOfOrders):
    if product[i] in productQuantity:
        productQuantity[product[i]] = productQuantity[product[i]]+quantity[i]   
    else:
        productQuantity[product[i]] = quantity[i]

#find the most selling brand for each product
for i in uniqueProducts:
    maxArray=[]
    for o in range(numOfOrders):
        if product[o] == i:
            maxArray.append(brand[o])
    popularBrand[i]=max(set(maxArray),key=maxArray.count)

#calcualte average qunaitity sold for each product
for key, value in productQuantity.items():
    val=value/numOfOrders
    if val % 1 == 0:
        val=int(val)
    productQuantity[key]=val


#write output files
for key, value in productQuantity.items():
    file1.append(str(key+","+str(value)))
with open(r'0_'+fileName, 'w') as file:
    for item in file1:
        file.write("%s\n" % item)
for key, value in popularBrand.items():
    file2.append(str(key+","+str(value)))
with open(r'1_'+fileName, 'w') as file:
    for item in file2:
        file.write("%s\n" % item)

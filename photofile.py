fo = open('C:/Users/amaheshwar24/Pictures/DXC_BrandtoDemand_Even if You Lose.jpg', 'rb')
fo1 = open('C:/Users/amaheshwar24/Documents/pythontraining/demo.txt', 'wb')
for line in fo:

    fo1.write(line)
fo1.close()

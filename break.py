fo = open('C:/Users/amaheshwar24/Pictures/DXC_BrandtoDemand_Even if You Lose.jpg', 'rb')
i = 0
for line in fo:
    fo1 = open('C:/Users/amaheshwar24/Documents/pythontraining/chunks' + str(i) + '.jpg', 'wb')
    i += 1
    fo1.write(line)
fo.close()

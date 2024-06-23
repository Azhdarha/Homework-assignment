b =   [[9, 5, 3],[0, 7, -1],[-5, 2, 9]]
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i-1][j])
        print(b[(i+1) % len(b)][j])
        print(b[i][j-1])
        print(b[i][(j+1) % len(b[i])])
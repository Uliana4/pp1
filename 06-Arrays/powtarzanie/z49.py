arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(5):
    for j in range(5):
        arr[i][j] = (i + 1) * (j + 1)

# Display the array
for row in arr:
    for value in row:
        print(f"{value:2}", end=" ")  # Adjust formatting for alignment
    print()
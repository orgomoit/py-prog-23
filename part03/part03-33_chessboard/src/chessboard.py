# Write your solution here

def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10" * size
            # row = "1010" * size
        else:
            row = "01" * size
            # row = "0101" * size
        print(row[:size])
        i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(6)

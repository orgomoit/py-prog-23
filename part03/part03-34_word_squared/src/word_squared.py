# Write your solution here

def squared(text, size):
    text = text * (size ** 2)
    i = 0
    while i < (size * size):
        print(text[i:i+size])
        i += size

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)

def zigZag(n):
    if n == 0:
        return
    else:
        print(f"Pre: {n}")
        zigZag(n - 1)
        print(f"In: {n}")
        zigZag(n - 1)
        print(f"Post: {n}")


"""
 use euler tree to understand the flow
 find time and space complexity
"""
if __name__ == "__main__":
    zigZag(3)

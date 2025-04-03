if __name__ == "__main__":
    a = [1,2,3,4,5]
    b = [5,6,7,8,9]

    def my_sum(a1,a2):
        return a1 + a2

    c = list(map(my_sum, a, b)) # list like converting iterator that map returns to list
    print(c)

    input_list = [1,2,3,4,5]
    r1 = list(map(lambda x: x * 2, input_list))
    print(r1)

    filtered_list = list(filter(lambda x: x % 2 == 0, input_list))
    print(filtered_list)
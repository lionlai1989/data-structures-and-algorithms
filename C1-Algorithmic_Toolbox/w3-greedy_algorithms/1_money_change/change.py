def change(money):
    # write your code here
    num_ten = 0
    num_five = 0
    num_one = 0
    num_ten = money // 10 # "//"": Get quotient
    num_five = (money % 10) // 5
    num_one = (money % 10) % 5
    return int(num_ten + num_five + num_one)


if __name__ == '__main__':
    m = int(input())
    print(change(m))

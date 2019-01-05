def get_saved_number_cnt(input_num):
    saved_number_cnt = 0
    for num in range(1, input_num + 1):
        if not num % 15 or (num % 3 and num % 5):
            saved_number_cnt += 1

    return saved_number_cnt

if __name__ == "__main__":
    input_num = input("input：")
    input_num = int(input_num)

    saved_number_cnt = get_saved_number_cnt(input_num)
    print("output：", saved_number_cnt)

    # Expected True to mathematical method.
    #print(saved_number_cnt == (input_num - input_num//3 - input_num//5 + 2 * (input_num//15)))
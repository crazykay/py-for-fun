from ast import Try
import sys
def get_argv_num():
    argv_len = len(sys.argv)
    if argv_len != 2:
        print("Usage: python convert_num_to_capital.py <integer number>")
        return
    else:
        try:
            num = int(sys.argv[1])
            return num
        except ValueError:
            print("ValueError, Usage: python convert_num_to_capital.py <integer number>")
def numbers_to_strings(number, index=None):
    switcher_number = {
        0: "零",
        1: "壹",
        2: "贰",
        3: "叁",
        4: "肆",
        5: "伍",
        6: "陆",
        7: "柒",
        8: "捌",
        9: "玖",
    }
    switcher_capital = {
        0: "仟",
        1: "佰",
        2: "拾",
        3: "",
    }
    cn_str = switcher_number.get(number, "")
    if cn_str == "零":
        return cn_str
    else:
        return cn_str + switcher_capital.get(index, "")
def insert_zero(digits):
    if len(digits) == 0:
        return digits
    else:
        return [0]*(4-len(digits)) + digits
def remove_duplicate_zero(digits):
    if len(digits) == 0:
        return digits
    else:
        for d in range(len(digits) - 1, 0, -1):
            if digits[d] == "零" and digits[d] == digits[d-1]:
                del digits[d]
        return digits
def formate_to_str(digits):
    removed_duplicate_zero = remove_duplicate_zero(digits)
    return "".join(removed_duplicate_zero).strip("零")
def convert_num_to_capital():
    # get the number from argv
    num = get_argv_num()
    if num is None:
        print('-_-')
    elif num > 999999999999:
        print('Too big, please input a number less than 999999999999')
    else:
        # convert the number to digits
        digits = [int(d) for d in str(num)]

        # insert zero to the front of the digits
        single_digits = insert_zero(digits[-4:len(digits)])
        ten_thousand_digits = insert_zero(digits[-8:-4])
        hundred_million_digits = insert_zero(digits[-12:-8])

        # print(single_digits, ten_thousand_digits, hundred_million_digits)
        # convert the digits to strings
        single_digits_capital = [numbers_to_strings(d, idx) for idx, d in enumerate(single_digits)]
        ten_thousand_digits_capital = [numbers_to_strings(d, idx) for idx, d in enumerate(ten_thousand_digits)]
        hundred_million_digits_capital = [numbers_to_strings(d, idx) for idx, d in enumerate(hundred_million_digits)]
        part1 = ""
        part2 = ""
        part3 = ""
        if hundred_million_digits:
            part1 = formate_to_str(hundred_million_digits_capital) + "亿"
        # 千万位是 0 补零
        if ten_thousand_digits:
            if hundred_million_digits and ten_thousand_digits[0] == 0:
                part2 = "零" + formate_to_str(ten_thousand_digits_capital) + "万"
            else:
                part2 = formate_to_str(ten_thousand_digits_capital) + "万"
        # 千位是 0 补零
        if ten_thousand_digits and single_digits[0] == 0:
            part3 = "零" + formate_to_str(single_digits_capital)
        else:
            part3 = formate_to_str(single_digits_capital)
        print(part1 + part2 + part3 + "元整")
if __name__ == "__main__":
    # execute only if run as a script
    convert_num_to_capital()
    pass
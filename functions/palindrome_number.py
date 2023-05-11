def palindrome_number(number):
    str_num = str(number)
    end_index = len(str_num) - 1
    for i in range(len(str_num)//2):
        str_num[i] == str_num[end_index]
        end_index -= 1
        
assert palindrome_number(123321) == True
assert palindrome_number(123322) == False
number = [1, 2, 3, 5, 15, 6, 1, 6574654, 2]


def max_num(li):
    x = max(li)
    return print(x)


max_num(number)


def mult_list(li):
    x = 1
    for i in li:
        x = x * i
    return print(x)


mult_list(number)


normal = "This is a normal sentence"


def rev_string(text):
    reversed_text = text[::-1]
    return print(reversed_text)


rev_string(normal)


def num_within(num, low_end, high_end):
    if num in range(low_end, high_end + 1):
        return print("True")
    else:
        return print("False")


num_within(3, 2, 4)
num_within(10, 2, 5)


# def pascal(n):
#     pascal_li = []
#     for i in range(n):
#         if len(pascal_li) < 2:
#             pascal_li.append(1)
#             print(pascal_li)
#         else:
#             pascal_li.append(1)
#             for x in range(1,n):
#                 pascal_li[x] = pascal_li[i] + pascal_li[i - 1]
#                 print(pascal_li)


def pascal(n):
    pascal_list = []
    for i in range(n):
        pascal_list.append(1)
  
        if len(pascal_list)>2:
            for x in range(1, len(pascal_list)):
                pascal_list[x] = pascal_list[i]+ pascal_list[i-1]
            pascal_list.pop()
            pascal_list.append(1)
        print(pascal_list)

            


pascal(5)

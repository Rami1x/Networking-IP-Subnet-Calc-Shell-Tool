# <------------------------------ Imports -------------------------------->
import sys
# <------------------------------ Functions ------------------------------>

def check(ipOne, ipTwo):
    illegal = 0
    forbidden = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    i = 0
    result = True

    while i < len(ipOne):
        if ipOne[i] in forbidden:
            i += 1
        else:
            illegal += 1
            i += 1
    i = 0

    while i < len(ipTwo):
        if ipTwo[i] in forbidden:
            i += 1
        else:
            illegal += 1
            i += 1
    
    match illegal:
        case 0:
            result = True
        case _:
            result = False

    return result

def segmentation(ipOne, ipTwo):
    seg_split = ""
    segment1 = []
    segment2 = []

    for num in ipOne:
        if num != ".":
            seg_split += num
        else:
            segment1.append(seg_split)
            seg_split = ""

    segment1.append(seg_split)
    seg_split = ""

    for num in ipTwo:
        if num != ".":
            seg_split += num
        else:
            segment2.append(seg_split)
            seg_split = ""
    segment2.append(seg_split)
    
    return segment1, segment2

def Binary_Conversion(IP1, IP2):
    num_list = [128, 64, 32, 16, 8, 4, 2, 1]
    IP1_int = []
    IP2_int = []
    binary_str = ""
    binary_append = [] 
    binary_append2 = [] 


    for inst in IP1:
        IP1_int.append(int(inst))

    for inst in IP2:
        IP2_int.append(int(inst))

    for val in IP1_int:
        for number in num_list:
            if val >= number:
                binary_str += "1"
                val = val - number
            else:
                binary_str += "0"
        binary_append.append(binary_str)
        binary_str = ""

    for val1 in IP2_int:
        binary_str = ""
        for number in num_list:
            if val1 >= number:
                binary_str += "1"
                val1 = val1 - number
            else:
                binary_str += "0"
        binary_append2.append(binary_str)
                
    
    return binary_append, binary_append2

def Binary_Compare(b_one, b_two):
    same_binary = ""
    same_binary_append = []
    binary_str1 = ""
    binary_str2 = ""
    i = 0
    i2 = 0

    for num1, num2 in zip(b_one, b_two):
        binary_str1 += num1
        binary_str2 += num2

    for num1, num2 in zip(binary_str1, binary_str2):
        if num1 == num2:
            same_binary += num1
        else:
            break
    
    subnet = f"/{len(same_binary)}"

    i = 0

    while i < len(same_binary):
        chunk = same_binary[i:i+8]
        if len(chunk) < 8:
            chunk = chunk.ljust(8, "0")
        same_binary_append.append(chunk)
        i += 8

    return same_binary_append, subnet

def Conclusion(summary, sub_mask):
    num_list = [128, 64, 32, 16, 8, 4, 2, 1]
    sum = 0
    ip_append = []
    i = 0
    j = 0
    full_ip = ""

    while j < len(summary):
        for num in summary[j]:
            if num == "1":
                sum += num_list[i]
                i += 1
            else:
                i += 1
        ip_append.append(sum)
        sum = 0
        j += 1
        i = 0

    i = len(ip_append)

    while i < 4:
        ip_append.append(0)
        i += 1
    i = 0

    while i < len(ip_append):
        full_ip += f"{ip_append[i]}"
        if i == 3:  
            full_ip += f"{sub_mask}"
        else:
            full_ip += "." 
        i += 1

    return print(full_ip)
    
    
# <-------------------------------- Main -------------------------------->

x = "192.168.10.1"
y = "192.168.20.1"

checker = check(x, y) 

if checker == True:
    print("nice")
    first_ip, second_ip = segmentation(x, y)
    x_binary, y_binary = Binary_Conversion(first_ip, second_ip)
    same_binary, subnet = Binary_Compare(x_binary, y_binary)
    Conclusion(same_binary, subnet)

else:
    print("L")
    
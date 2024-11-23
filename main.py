import sys

x = '192.168.10.1'
y = '192.168.20.1'

def check(ipOne, ipTwo):
    legal = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9", "0", "."]

    for num1, num2 in zip(ipOne, ipTwo):    # this for loop checks if its in IPV4 format.
        if num1 in legal and num2 in legal:
            result = True
        else:
            result = False
            break
    
    return result

def segmentation(ipOne, ipTwo):
    dot = "."
    sim_ip = ""
    sim_ip_append = []
    wrong_ip_line = 0
    not_ip1 = ""
    not_ip2 = ""
    not_ip1_append = []
    not_ip2_append = []

    for num1, num2 in zip(ipOne, ipTwo): # this is the for loop which finds similar ip addresses but checks if its full segment similarity first
        if num1 != dot and num2 != dot:
            if num1 == num2:
                sim_ip += num1
                wrong_ip_line += 1
            else:
                break
        elif num2 == dot and num2 == dot:
            sim_ip_append.append(sim_ip)
            wrong_ip_line += 1
            sim_ip = ""
        else:
            break

    for i in range(wrong_ip_line, len(ipOne)):
        num1 = ipOne[i]
        num2 = ipTwo[i]
        if num1 != dot and num2 != dot:
            not_ip1 += num1
            not_ip2 += num2
        elif num1 == dot and num2 == dot:
            not_ip1_append.append(not_ip1)
            not_ip2_append.append(not_ip2)
            not_ip1 = ""
            not_ip2 = ""
        else:
            break

    if not_ip1 or not_ip2:
        not_ip1_append.append(not_ip1)
        not_ip2_append.append(not_ip2)


    return sim_ip_append, not_ip1_append, not_ip2_append

def binary(diffOne, diffTwo):
    diffOne_int = []
    diffTwo_int = []
    num_list = [128, 64, 32, 16, 8, 4, 2, 1]
    binary_diffOne = ""
    binary_diffTwo = ""
    binary_one_append = []
    binary_two_append = []

    for val in diffOne:
        diffOne_int.append(int(val))
    for val in diffTwo:
        diffTwo_int.append(int(val))

    for num in diffOne_int:
        binary_diffOne = ""
        for bit in num_list:
            if num >= bit:
                binary_diffOne += "1"
                num -= bit
            else:
                binary_diffOne += "0"
        binary_one_append.append(binary_diffOne)

    for numb in diffTwo_int:
        binary_diffTwo = ""
        for bitt in num_list:
            if numb >= bitt:
                binary_diffTwo += "1"
                numb -= bitt
            else:
                binary_diffTwo += "0"

        binary_two_append.append(binary_diffTwo)

    return binary_one_append, binary_two_append

def getSummarized(One, Two):
    sum_append = []
    rowOne = []
    rowTwo = []
    summarized = ""

    rowOne.append(One[0])
    rowOne.append(Two[0])
    rowTwo.append(One[1])
    rowTwo.append(Two[1])

    for num1, num2 in zip(rowOne[0], rowOne[1]):
        if num1 != num2:
            summarized += "1"
        else:
            if num1 == "0":
                summarized += "0"
            else:
                summarized = summarized[:-1]
                summarized += "10"

    sum_append.append(summarized)
    summarized = ""

    for num1, num2 in zip(rowTwo[0], rowTwo[1]):
        if num1 != num2:
            summarized += "1"
        else:
            if num1 == "0":
                summarized += "0"
            else:
                summarized = summarized[:-1]
                summarized += "10"
    
    sum_append.append(summarized)

    return sum_append

checker = check(x, y) 

if checker == True:
    same_addr, diff_addr1, diff_addr2 = segmentation(x, y)
    binary_convert_one, binary_convert_two = binary(diff_addr1, diff_addr2)
    summarized = getSummarized(binary_convert_one, binary_convert_two)

    print(f"Identical segments of first and second IP: {same_addr}\nDifferent segments for first IP: {diff_addr1}\nDifferent segments for second IP: {diff_addr2}\n")
    
    
    
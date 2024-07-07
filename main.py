
def AND(A,B):
    result = ["F" for i in range(len(A))]
    for i in range(len(A)):
        if((A[i])=="T" and (B[i])=="T"):
            result[i] = "T"
    return result

def implication(A,B):
    result = ["T" for i in range(len(A))]
    for i in range(len(A)):
        if((A[i])=="T" and (B[i])=="F"):
            result[i] = "F"
    return result

def OR(A,B):
    result = ["T" for i in range(len(A))]
    for i in range(len(A)):
        if((A[i])=="F" and (B[i])=="F"):
            result[i] = "F"
    return result

def XOR(A,B):
    result = ["F" for i in range(len(A))]
    for i in range(len(A)):
        if((A[i])!=(B[i])):
            result[i] = "T"
    return result

def XNOR(A,B):
    result = ["F" for i in range(len(A))]
    for i in range(len(A)):
        if((A[i])==(B[i])):
            result[i] = "T"
    return result

def NOT(A):
    for i in range(len(A)):
        if((A[i])=="F"):
            A[i] = "T"
        else:
            A[i] = "F"
    return A

def Num2(exp, num):
    stack_1 = []
    stack_2 = []
    index_1 = -1
    index_2 = -1

    A = ["F" for i in range(2 ** num)]
    B = ["F" for i in range(2 ** num)]
    for i in range(num):
        if i == 0:
            for j in range(int((2 ** num) / 2)):
                A[(2 ** num) - (j + 1)] = "T"
        else:
            for j in range(2 ** num):
                if (j % 2) != 0:
                    B[j] = "T"

    print("A =",A)
    print("B =",B)
    exp_list = list(exp)
    for i in range(len(exp_list)):
        if (ord(exp_list[i])) == 65:
            stack_1.append(A)
            index_1 += 1
        elif (ord(exp_list[i])) == 66:
            stack_1.append(B)
            index_1 += 1
        elif exp_list[i] == ")":
            while stack_2[index_2] != "(":
                if stack_2[index_2] == "^":
                    stack_1.append(AND(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "V":
                    stack_1.append(OR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1

                elif stack_2[index_2] == "O":
                    stack_1.append(XOR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1

                elif stack_2[index_2] == "+":
                    stack_1.append(XOR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == ">":
                    col = stack_1.pop()
                    index_1 -= 1
                    stack_1.append(implication(stack_1.pop(), col))
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "-":
                    stack_1.append(NOT(stack_1.pop()))
                    stack_2.pop()
                    index_2 -= 1
            stack_2.pop()
            index_2 -= 1
        else:
            stack_2.append(exp_list[i])
            index_2 += 1
    print("X =",stack_1.pop())

def Num3(exp, num):
    stack_1 = []
    stack_2 = []
    index_1 = -1
    index_2 = -1
    A = ["F" for i in range(2 ** num)]
    B = ["F" for i in range(2 ** num)]
    C = ["F" for i in range(2 ** num)]
    for i in range(num):
        if i == 0:
            for j in range(int((2 ** num) / 2)):
                A[(2 ** num) - (j + 1)] = "T"
        if i == 1:
            count = 2
            for j in range(int((2 ** num) / 4)):
                for k in range(2):
                    B[count + j + k] = "T"
                count += 3
        else:
            for i in range(2 ** num):
                if (i % 2) != 0:
                    C[i] = "T"
    print("A =",A)
    print("B =",B)
    print("C =",C)
    exp_list = list(exp)
    for i in range(len(exp_list)):
        if (ord(exp_list[i])) == 65:
            stack_1.append(A)
            index_1 += 1
        elif (ord(exp_list[i])) == 66:
            stack_1.append(B)
            index_1 += 1
        elif (ord(exp_list[i])) == 67:
            stack_1.append(C)
            index_1 += 1
        elif exp_list[i] == ")":
            while stack_2[index_2] != "(":
                if stack_2[index_2] == "^":
                    stack_1.append(AND(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == ">":
                    col = stack_1.pop()
                    index_1 -= 1
                    stack_1.append(implication(stack_1.pop(), col))
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "V":
                    stack_1.append(OR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "O":
                    stack_1.append(XOR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "+":
                    stack_1.append(XNOR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "-":
                    stack_1.append(NOT(stack_1.pop()))
                    stack_2.pop()
                    index_2 -= 1
            stack_2.pop()
            index_2 -= 1
        else:
            stack_2.append(exp_list[i])
            index_2 += 1
    print("X =",stack_1.pop())

def Num4(exp,num):
    stack_1 = []
    stack_2 = []
    index_1 = -1
    index_2 = -1
    A = ["F" for i in range(2 ** num)]
    B = ["F" for i in range(2 ** num)]
    C = ["F" for i in range(2 ** num)]
    D = ["F" for i in range(2 ** num)]
    for i in range(num):
        if i == 0:
            for j in range(int((2 ** num) / 2)):
                A[(2 ** num) - (j + 1)] = "T"
        if i == 1:
            count = 4
            for j in range(int((2 ** num) / 8)):
                for k in range(4):
                    B[count + j + k] = "T"
                count += 7
        if i == 2:
            count = 2
            for j in range(int((2 ** num) / 4)):
                for k in range(2):
                    C[count + j + k] = "T"
                count += 3
        else:
            for j in range(2 ** num):
                if (j % 2) != 0:
                    D[j] = "T"
    print("A =",A)
    print("B =",B)
    print("C =",C)
    print("D =",D)
    exp_list = list(exp)
    for i in range(len(exp_list)):
        if (ord(exp_list[i])) == 65:
            stack_1.append(A)
            index_1 += 1
        elif (ord(exp_list[i])) == 66:
            stack_1.append(B)
            index_1 += 1
        elif (ord(exp_list[i])) == 67:
            stack_1.append(C)
            index_1 += 1
        elif (ord(exp_list[i])) == 68:
            stack_1.append(D)
            index_1 += 1
        elif exp_list[i] == ")":
            while stack_2[index_2] != "(":
                if stack_2[index_2] == "^":
                    stack_1.append(AND(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == ">":
                    col = stack_1.pop()
                    index_1 -= 1
                    stack_1.append(implication(stack_1.pop(), col))
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "V":
                    stack_1.append(OR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "O":
                    stack_1.append(XOR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "+":
                    stack_1.append(XNOR(stack_1.pop(), stack_1.pop()))
                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "-":
                    stack_1.append(NOT(stack_1.pop()))
                    stack_2.pop()
                    index_2 -= 1
            stack_2.pop()
            index_2 -= 1
        else:
            stack_2.append(exp_list[i])
            index_2 += 1
    print("X =",stack_1.pop())


def Num5(exp, num):
    stack_1 = []
    stack_2 = []
    index_1 = -1
    index_2 = -1
    A = ["F" for i in range(2 ** num)]
    B = ["F" for i in range(2 ** num)]
    C = ["F" for i in range(2 ** num)]
    D = ["F" for i in range(2 ** num)]
    E = ["F" for i in range(2 ** num)]
    for i in range(num):
        if i == 0:
            for j in range(int((2 ** num) / 2)):
                A[(2 ** num) - (j + 1)] = "T"
        if i == 1:
            count = 8
            for j in range(int((2 ** num) / 16)):
                for k in range(8):
                    B[count + j + k] = "T"
                count += 15
        if i == 2:
            count = 4
            for j in range(int((2 ** num) / 8)):
                for k in range(4):
                    C[count + j + k] = "T"
                count += 7
        if i == 3:
            count = 2
            for j in range(int((2 ** num) / 4)):
                for k in range(2):
                    D[count + j + k] = "T"
                count += 3
        else:
            for j in range(2 ** num):
                if (j % 2) != 0:
                    E[j] = "T"
    print("A =",A)
    print("B =",B)
    print("C =",C)
    print("D =",D)
    print("E =",E)
    exp_list = list(exp)
    for i in range(len(exp_list)):
        if (ord(exp_list[i])) == 65:
            stack_1.append(A)
            index_1 += 1
        elif (ord(exp_list[i])) == 66:
            stack_1.append(B)
            index_1 += 1
        elif (ord(exp_list[i])) == 67:
            stack_1.append(C)
            index_1 += 1
        elif (ord(exp_list[i])) == 68:
            stack_1.append(D)
            index_1 += 1
        elif (ord(exp_list[i])) == 69:
            stack_1.append(E)
            index_1 += 1
        elif exp_list[i] == ")":
            while stack_2[index_2] != "(":
                if stack_2[index_2] == "^":
                    stack_1.append(AND(stack_1.pop(), stack_1.pop()))

                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == ">":
                    col = stack_1.pop()
                    index_1 -= 1
                    stack_1.append(implication(stack_1.pop(), col))
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "V":
                    stack_1.append(OR(stack_1.pop(), stack_1.pop()))

                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1

                elif stack_2[index_2] == "O":
                    stack_1.append(XOR(stack_1.pop(), stack_1.pop()))

                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "+":
                    stack_1.append(XNOR(stack_1.pop(), stack_1.pop()))

                    index_1 -= 1
                    stack_2.pop()
                    index_2 -= 1
                elif stack_2[index_2] == "-":
                    stack_1.append(NOT(stack_1.pop()))

                    stack_2.pop()
                    index_2 -= 1
            stack_2.pop()
            index_2 -= 1
        else:
            stack_2.append(exp_list[i])
            index_2 += 1
    print("X =",stack_1.pop())

num = int(input("Enter Number Of Variables: "))
exp = input("Enter Expression: ")
if num == 2:
    Num2(exp, num)
elif num == 3:
    Num3(exp, num)
elif num == 4:
    Num4(exp, num)
elif num == 5:
    Num5(exp, num)
else:
    print("Wrong Input")

'''
Here we are using euclidean algorithm lets understand and see the algorithm
'''

# def gcd_of_numbers(num1,num2):
#     div1,div2,c=[],[],0
#     for i in range(1,num1+1):
#         if num1%i==0:
#             div1.append(i)
#     for i in range(1,num2+1):
#         if num2%i==0:
#             div2.append(i)
#     result=set(div1).intersection(set(div2))
#     return div1,div2,result

# def gcd_of_numbers(num1,num2):

#     k=max(num1,num2)
#     y=min(num1,num2)
#     r,q=1,1
#     for i in range(1,k+1):
        
#         q=k/y
#         r=k%y
#         k=y
#         y=r
#         if y==0:
#             return k # Method1

def gcd_of_two_numbers(num1,num2):
    if num2>num1:
        num1,num2=num2,num1 #prerequesite that num1 should be greater than num1
    
    if num2==0:
        return num1 
    else:
        return gcd_of_two_numbers(num2,num1%num2)
    
    
    

    



def gcd_of_strings(str1,str2):
    len_gcd=gcd_of_two_numbers(len(str1),len(str2))
    #Extract length o
    substring=str1[:len_gcd]

    #check if substring is common divisor for both the strings
    #"ABC" * (len("ABCABC") // 3) == "ABCABC"  # True
    is_divisor_for_str1=substring*(len(str1)//len_gcd)==str1
    is_divisor_for_str2=substring*(len(str2)//len_gcd)==str2

    if is_divisor_for_str1 and is_divisor_for_str2:
        return substring
    else:
        return ""

    



if __name__=="__main__":
    print(gcd_of_strings("ABCABC","ABC"))
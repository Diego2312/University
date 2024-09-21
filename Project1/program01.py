# -*- coding: utf-8 -*-

'''
Let int_seq be a string that contains a sequence of non-negative
    integers separated by commas and subtotal a non-negative integer.

Design a function ex1(int_seq, subtotal) that:
    – takes as parameters 
      a string (int_seq) and a positive integer (subtotal >= 0), and 
    – returns the number of substrings of int_seq such that 
      the sum of their values is equal to subtotal.

Hint: you can obtain a substring by picking any consecutive
    elements in the original string.

For example, given int_seq = '3,0,4,0,3,1,0,1,0,0,5,0,4,2' and subtotal = 9, 
    the function should return 7. The following substrings, indeed, consist of
    values whose sum is equal to 9:
    int_seq = '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
            => _'0,4,0,3,1,0,1,0'_____________
               _'0,4,0,3,1,0,1'_______________
               ___'4,0,3,1,0,1,0'_____________
               ___'4,0,3,1,0,1'_______________
               ___________________'0,0,5,0,4'_
             _____________________'0,5,0,4'_
                 _______________________'5,0,4'_

NOTE: it is FORBIDDEN to use/import any libraries

NOTE: Each test must terminate on the VM before the timeout of
    1 second expires.

WARNING: Make sure that the uploaded file is UTF8-encoded
    (to that end, we recommend you edit the file with Spyder)
'''

def ex1(int_seq, subtotal):

    int_list = []
    count = 0 #number of subsequnces

    spl = int_seq.split(',')

    for n in spl:
        int_list.append(int(n))

    #Loop

    #Start a subsequence from every value on the list
    for j in range(len(int_list)):
        sum_values = 0

        print('number of loops ', j)

        #Check the sums of subsequences
        for i in range(len(int_list)):
            print('index ', i)
            print(sum_values, '+', int_list[i])

            #Add value of list to variable sum_values
            sum_values += int_list[i]

            #Count how many times you get a sum exactly equal to the subtotal (sequence found)
            if sum_values == subtotal:
                count += 1
                try:
                    if int_list[i+1] == 0:
                        print('it happened')
                        print('sliced list ', int_list[i:])

                        #The number of consecutive zeroes after the sum adds to count
                        for k in range(len(int_list[i:]) - 1):
                            print('this is the value of the list', int_list[k], 'this is the index of the value', k)
                            print('this is the sliced list ', int_list[i:])
                            print('this is the len of the list ', len(int_list))
                            if int_list[k] == 0:
                                print(k)
                                count += 1
                                print('added')
                            elif int_list[k+1] != 0:
                                break
                            else:
                                continue
                        pass
                except IndexError:
                    continue

            #Stop the loop if the sum of the subsequence exceeds the subtotal or if it's equal (no reason to continue)
            if sum_values >= subtotal:
                break
            print('sum of the values is ', sum_values)

        #Shorten the list every time, so the begining value changes (so the subsequence changes)
        int_list.pop(0)

        print(count)
    return count

test_seq_len  = 10
half          = test_seq_len // 2
zeros         = ['0'] * (half-1)
test_int_seq  = ",".join(zeros + ['1']*2 + zeros)
print(test_int_seq)
test_subtotal = 2
expected      = half ** 2

if __name__ == '__main__':
    ex1(test_int_seq, 2)
    pass




test_lis = '12, 32, 43, 54, 123, 532'
spli = test_lis.split(',')
emp = []
for i in spli:
    emp.append(int(i))

#print(emp)


print(expected)

#return self.do_test(test_int_seq, test_subtotal, expected)


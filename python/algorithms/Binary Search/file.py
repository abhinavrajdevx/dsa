def binary_search(lo, hi, condition):
    while (lo <= hi):
        mid= (lo + hi ) // 2
  #      print ('mid: ', mid, " lo: ", lo, ' high ', hi)
   #     print(condition(mid) )
        if (condition(mid) == "equal"):
            return mid
        elif (condition(mid) == "left"):
            hi= mid -1
        elif (condition(mid) == "right"):
            lo= mid +1
    return -1

def solution (nums, value):
    def condition(mid):
     #   print ('mid:  ', mid)
        if (nums[mid] == value):
            return "equal"
        elif (nums[mid] > value):
            return "left"
        elif (nums[mid] < value):
            return "right"
    return binary_search(0, len(nums), condition )


def test (testcases, solution):
    index= 0
    while (index < len(testcases)):
    #    print ('Test Case: ', index+1, '\n\n' ,testcases[index])
        if (testcases[index]['output'] == solution(testcases[index]['input']['nums'],  testcases[index]['input']['value'] )):
            print ("PASSED", )
        else:
            print ("FAILED")
        print ('OUTPUT: ', solution(testcases[index]['input']['nums'],  testcases[index]['input']['value'] ))
        index= index+1
        print ('\n\n')

def main ():
    testcases= [
        {
            # Normal Case
            'input' : {
                'nums': [1, 2, 3, 4, 5],
                'value': 4
            },
            'output': 3
        },
                {
            # Normal Case
            'input' : {
                'nums': [1, 2, 3, 4, 5],
                'value': 5
            },
            'output': 4
        }
    ]
    test(testcases, solution)



main()



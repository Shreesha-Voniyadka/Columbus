def removeDuplicates(self, arr):
        # code here
        # stack = []
        # for x in arr:
        #     if x not in stack:
        #         stack.append(x)
        # return stack
        # problem in this got time complexity issue run time error
        
        a=[ ]
        d=dict()
        for i in arr:
            if i not in d:
                a.append(i)
                d[i]=1
        return a
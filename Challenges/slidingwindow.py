#Sliding window
# Input  : arr[] = {100, 200, 300, 400}, k = 2
# Output : 700

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

# Input  : arr[] = {2, 3}, k = 3
# Output : Invalid
# There is no subarray of size 3 as size of whole array is 2.

# start & end of sliding window: |start-> ... end->|
# short version of sliding window, focus on two pointers
def start_end_sliding_window(self, seq):
    start, end = 0, 0
    while end < len(seq):
        # end pointer grows in the outer loop
        end += 1
        
        # start pointer grows with some restrict
        while self.start_condition(start):
            # process logic before pointers movement
            self.process_logic1(start, end)
            # start grows in the inner loop
            start += 1
            
        # or process logic after pointers movement
        self.process_logic2(start, end)
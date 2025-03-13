from typing import List

class SegmentTree:
    def __init__(self, data):  # ✅ Fix: Correct the constructor name
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.min_tree = [float('inf')] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        
        # Initialize the tree
        for i in range(self.n):
            self.min_tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.min_tree[i] = min(self.min_tree[2 * i], self.min_tree[2 * i + 1])
    
    def push(self, node, l, r):
        """ Push the lazy updates down the tree. """
        if self.lazy[node] != 0:
            self.min_tree[node] += self.lazy[node]
            if l != r:  # If not a leaf node
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0
    
    def range_add(self, a, b, val, node=1, l=0, r=None):
        """ Add `val` to all elements in range [a, b]. """
        if r is None:
            r = self.size - 1
        self.push(node, l, r)
        if a > r or b < l:
            return
        if a <= l and r <= b:
            self.lazy[node] += val
            self.push(node, l, r)
            return
        mid = (l + r) // 2
        self.range_add(a, b, val, 2 * node, l, mid)
        self.range_add(a, b, val, 2 * node + 1, mid + 1, r)
        self.min_tree[node] = min(self.min_tree[2 * node], self.min_tree[2 * node + 1])
    
    def query_min(self, a=0, b=None, node=1, l=0, r=None):
        """ Get the minimum value in range [a, b]. """
        if b is None:
            b = self.size - 1
        if r is None:
            r = self.size - 1
        self.push(node, l, r)
        if a > r or b < l:
            return float('inf')
        if a <= l and r <= b:
            return self.min_tree[node]
        mid = (l + r) // 2
        left = self.query_min(a, b, 2 * node, l, mid)
        right = self.query_min(a, b, 2 * node + 1, mid + 1, r)
        return min(left, right)

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if not nums:
            return 0
        delta = [-x for x in nums]
        st = SegmentTree(delta)
        
        # Check if the initial array is already zero
        if st.query_min() >= 0:
            return 0
        
        for k, (l, r, val) in enumerate(queries):
            st.range_add(l, r, val)
            if st.query_min() >= 0:
                return k + 1  # Return the 1-based index of the successful query
        
        return -1  # If no query made the array zero, return -1

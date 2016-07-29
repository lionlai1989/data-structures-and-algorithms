#Greedy Algorithm<br>
1. Reduction to subproblem<br>
2. safe move, if there is an optimal solution consistent with this first move (Not all first moves are safe).<br>
General Strategy:<br>
problem --> safe move<br>
   1. make a safe move.<br>
   2. PROVE that it is a safe move.<br>
   3. reduce to subproblem.<br>
   4. solve the subproblem.<br>

It's really important to PROVE your solutions before implementing them.<br>
#Divide and Conquer<br>
   1. break the problem into non-overlapping subproblems of the same type.<br>
   2. recursively solve these problems.<br>
   3. combine results of subproblems.<br>

##Binary Search<br>
```python
def binarySearch(array, low, high, key):
  if high < low:
    return -1
  mid = floor(mid+(high-low)/2)
  if key == array[mid]:
    return key
  elif key < array[mid]:
    binarySearch(array, low, mid-1, key)
  else:
    binarySearch(array, mid+1, high, key)
```
###Note: Using "Unicode Entity Codes for Math" to express math equation.<br>
##Polynomial Multiplication<br>
two n-1 degree polys:<br>
(a<sub>n-1</sub>X<sup>n-1</sup> + a<sub>n-2</sub>X<sup>n-2</sup> + ... + a<sub>1</sub>X + a<sub>0</sub>) &times; (b<sub>n-1</sub>X<sup>n-1</sup> + b<sub>n-2</sub>X<sup>n-2</sup> + ... + b<sub>1</sub>X + b<sub>0</sub>) = (c<sub>2n-2</sub>X<sup>2n-2</sup> + c<sub>2n-3</sub>X<sup>2n-3</sup> + ... + c<sub>1</sub>X + c<sub>0</sub>)

A(X) = D<sub>1</sub>(X)X<sup>n/2</sup> + D<sub>0</sub>(X)<br>
D<sub>1</sub>(X) = a<sub>n-1</sub>X<sup>n/2-1</sup> + a<sub>n-2</sub>X<sup>n/2-2</sup> + ... + a<sub>n/2</sub><br>
D<sub>0</sub>(X) = a<sub>n/2-1</sub>X<sup>n/2-1</sup> + a<sub>n/2-2</sub>X<sup>n/2-2</sup> + ... + a<sub>0</sub><br>
B(X) = E<sub>1</sub>(X)X<sup>n/2</sup> + E<sub>0</sub>(X)<br>
E<sub>1</sub>(X) = b<sub>n-1</sub>X<sup>n/2-1</sup> + b<sub>n-2</sub>X<sup>n/2-2</sup> + ... + b<sub>n/2</sub><br>
E<sub>0</sub>(X) = b<sub>n/2-1</sub>X<sup>n/2-1</sup> + b<sub>n/2-2</sub>X<sup>n/2-2</sup> + ... + b<sub>0&#189;</sub><br>
AB = (D<sub>1</sub>E<sub>1</sub>)X<sup>n</sup> + (D<sub>1</sub>E<sub>0</sub> + D<sub>0</sub>E<sub>1</sub>)X<sup>n/2</sup> + D<sub>0</sub>E<sub>0</sub><br>
i = 0 to log<sub>2</sub>n, &#8721;4<sup>i</sup> &times; k &times; n &frasl; 2<sup>i</sup> = O(n<sup>2</sup>)




I finished most of assignments except  
'03_inversions.py',  
'03_points_and_segments.py',  
'03_sorting.py',  
'04_knapsack.py'  
'04_lcs3.py',  
'04_placing_parentheses.py'  

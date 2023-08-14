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
##Polynomial Multiplication<br>
two n-1 degree polys:<br>
(a<sub>n-1</sub>x<sup>n-1</sup> + a<sub>n-2</sub>x<sup>n-2</sup> + ... + a<sub>1</sub>x + a<sub>0</sub>) &times; (b<sub>n-1</sub>x<sup>n-1</sup> + b<sub>n-2</sub>x<sup>n-2</sup> + ... + b<sub>1</sub>x + b<sub>0</sub>) = (c<sub>2n-2</sub>x<sup>2n-2</sup> + c<sub>2n-3</sub>x<sup>2n-3</sup> + ... + c<sub>1</sub>x + c<sub>0</sub>)<br>
### naive<br>
```python
product = [0]
for i in range(n):
   for j in range(n):
      product[i+j] = product[i+j] + A[i]*B[j]
```
runtime: O(n<sup>2</sup>)<br>
###naive Divide and Conquer<br>
A(x) = D<sub>1</sub>(x)x<sup>n/2</sup> + D<sub>0</sub>(x)<br>
D<sub>1</sub>(x) = a<sub>n-1</sub>x<sup>n/2-1</sup> + a<sub>n-2</sub>x<sup>n/2-2</sup> + ... + a<sub>n/2</sub><br>
D<sub>0</sub>(x) = a<sub>n/2-1</sub>x<sup>n/2-1</sup> + a<sub>n/2-2</sub>x<sup>n/2-2</sup> + ... + a<sub>0</sub><br>
B(x) = E<sub>1</sub>(x)x<sup>n/2</sup> + E<sub>0</sub>(x)<br>
E<sub>1</sub>(x) = b<sub>n-1</sub>x<sup>n/2-1</sup> + b<sub>n-2</sub>x<sup>n/2-2</sup> + ... + b<sub>n/2</sub><br>
E<sub>0</sub>(x) = b<sub>n/2-1</sub>x<sup>n/2-1</sup> + b<sub>n/2-2</sub>x<sup>n/2-2</sup> + ... + b<sub>0</sub><br>
AB = (D<sub>1</sub>E<sub>1</sub>)x<sup>n</sup> + (**D<sub>1</sub>E<sub>0</sub> + D<sub>0</sub>E<sub>1</sub>**)x<sup>n/2</sup> + D<sub>0</sub>E<sub>0</sub><br>
runtime: i = 0 to log<sub>2</sub>n, &#8721;4<sup>i</sup> &times; k &times; n &frasl; 2<sup>i</sup> = O(n<sup>2</sup>)<br>
###faster Divide and Conquer by Karatsuba<br>
A(x) = a<sub>1</sub>x + a<sub>0</sub><br>
B(x) = b<sub>1</sub>x + b<sub>0</sub><br>
C(x) = A(x)B(x) = a<sub>1</sub>b<sub>1</sub>x<sup>2</sup> + (**a<sub>1</sub>b<sub>0</sub> + a<sub>0</sub>b<sub>1</sub>**)x + a<sub>0</sub>b<sub>0</sub><br>
It doesn't need to calculate **a<sub>1</sub>b<sub>0</sub> + a<sub>0</sub>b<sub>1</sub>** respectively, just using<br>
a<sub>1</sub>b<sub>0</sub> + a<sub>0</sub>b<sub>1</sub> = (a<sub>1</sub> + a<sub>0</sub>)(b<sub>1</sub> + b<sub>0</sub>) - a<sub>1</sub>b<sub>1</sub> - a<sub>0</sub>b<sub>0</sub><br>
to calculate the sum of them.<br>
It can reduce times of calculation: 4 --> 3<br>
runtime: i = 0 to log<sub>2</sub>n, &#8721;3<sup>i</sup> &times; k &times; n &frasl; 2<sup>i</sup> = O(n<sup>log<sub>2</sub></sup><sup>3</sup>)= O(n<sup>1.58</sup>)<br>
##Master Theorem<br>
if T(n) = aT(&lceil;n/b&rceil;) + O(n<sup>d</sup>), (for constants, a > 0, b > 1, d &ge; 0)<br>
T(n) &isin; O(n<sup>d</sup>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;, if d > log<sub>b</sub>a, 2<sup>nd</sup> > 1<sup>st</sup><br>
T(n) &isin; O(n<sup>d</sup>log(n))         , if d = log<sub>b</sub>a, 2<sup>nd</sup> = 1<sup>st</sup><br>
T(n) &isin; O(n<sup>log<sub>b</sub>a</sup>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;, if d < log<sub>b</sub>a, 2<sup>nd</sup> < 1<sup>st</sup><br>
##Fibonacci<br>
###Naive Solution:<br>
```python
def f(n):
   if n <= 1:
      return n
   else:
      f(n-1) + f(n)
```
###Smart Solution
```python
def f(n):
   F = [0] * n
   F[0] = 0
   F[1] = 1
   for i in range(2, n+1):
      F[i] = F[i-1] + F[i-2]
   return F(n)
```
##Greatest Common Divisor
###Naive Solution
```python
def gcd(a, b):
   best = 0
   for d in range(1, a+b):
      if a%d == 0 and b%d == 0:
         best = d
   return best
```
###Smart Solution: Euclidean Algorithm
**lemma**: a' = a % b, gcd(a, b) = gcd(a', b) = gcd(b, a')<br>
```python
def gcd(a, b):
   if b == 0:
      return a
   else:
      a' = a % b
   return gcd(b, a')
```
#Computing Runtime:
Consider **asymptotic** runtimes. How does runtime scale with INPUT size?<br>
log(n) ≪ &radic;n ≪ n ≪ nlog(n) ≪  n<sup>2</sup>  ≪  2<sup>n</sup><br>
n<sup>a</sup> ≪ n<sup>b</sup> for 0 < a < b<br>
n<sup>a</sup> ≪ b<sup>n</sup> for a > 0, b > 1<br>
log<sub>b</sub>x<sup>p</sup> = p&sdot;log<sub>b</sub>x<br>
f(n) = O(g(n)), f(n) grows **no more faster** than g(n).
#Sorting Problem
Tree property: 2<sup>d</sup> &ge; l, d &ge; log<sub>2</sub>l<br> 
Selection Sort, Merge Sort, Bubble Sort, Insertion Sort<br>
**quick sort:** 
Mathematical analysis of quicksort shows that, on average, the algorithm takes O(n&sdot;log(n)) comparisons to sort n items. In the worst case, it makes O(n<sup>2</sup>) comparisons, though this behavior is rare.<br>
##Editing Distance<br>
**M**atch<br>
**R**eplace<br>
**I**nsert into x<br>
**D**elete from x<br>

||1|2|3|4|5|6|7|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|X|E|D|I|T|I|N|G||
|Y|D|I|S|T|A|N|C|E|

```c
Let D[0, j] = 0, D[i, 0] = i, other wise
D[i, j] = min( D[i-1, j] + 1, 
               D[i, j-1] + 1, 
               D[i-1, j-1] + δ(x[i], y[j]))
if x[i] = y[j]
   δ = 0;
else
   δ = 1;
```
||||D|I|S|T|A|N|C|E|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| | |0|1|2|3|4|5|6|7|8|
| |0|0|1|2|3|4|5|6|7|8|
|E|1|1|1|2|3|4|5|6|7|7|
|D|2|2|1|2|3|4|5|6|7|8|
|I|3|3|2|1|2|3|4|5|6|7|
|T|4|4|3|2|2|2|3|4|5|6|
|I|5|5|4|3|3|3|3|4|5|6|
|N|6|6|5|4|4|4|4|3|4|5|
|G|7|7|6|5|5|5|5|4|4|5|
**eg.**<br>
D[1, 1] = min( D[1, 0] + 1 --> 2, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D[0, 1] + 1 --> 2, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D[0, 0] + δ(x[1], y[1]) --> 1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>
D[2, 1] = min( D[2, 0] + 1 --> 3, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D[1, 1] + 1 --> 2, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D[1, 0] + δ(x[2], y[1]) --> 1, &#8757;x[2] = D =y[1], &#8756;δ = 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>
Use backtrack pointer to reconstruct path.<br>
```python
def edit_distance(x, y):
	m = len(x)
	n = len(y)
	arr = np.zeros(shape=(m+1, n+1))
	for i in range(m+1):
	   arr[i, 0] = i
	for i in range(n+1):
		arr[0, i] = i
	for i in range(1, m+1):
		for j in range(1, n+1):
			insertion = arr[i, j-1] + 1
			deletion = arr[i-1, j] + 1
			match = arr[i-1, j-1]
			mismatch = arr[i-1, j-1] + 1
			if x[i-1] == y[j-1]:
				arr[i, j] = min(insertion, deletion, match)
			else:
				arr[i, j] = min(insertion, deletion, mismatch)
   return int(arr[m, n])
```
#Dynamic Array<br>
len(array) = **2**<br>
len(array) = **4**<br>
len(array) = **8**<br>
len(array) = **16**<br>
len(array) = **32**<br>

**Aggregate Method (or brute force)**<br>
**Accounting Method (or the banker's method)**<br>
**Potential Method (or the physicist's method)**<br>

I finished most of assignments except  
'03_inversions.py',  
'03_points_and_segments.py',  
'03_sorting.py',  
'04_knapsack.py'  
'04_lcs3.py',  
'04_placing_parentheses.py'  

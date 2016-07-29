#Hash Tables<br>
##Direct Addressing<br>
Input: 0 <= n <= 999<br>
create an array[1000]<br>

|array|
|:---:|
|0|
|1|
|...|
|998|
|999|
##Hash Function<br>
For any set of objects S and any integer m > 0, a function h: S-->{0, 1, ..., m-1} is called a hash function.<br>
m is called the cardinality of hash function h.<br>
Properties:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. direct addressing with O(m) memory.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. we want small cardinality m.<br>
Collision: h(O1) == h(O2), O1 != O2<br>
###Chaining<br>
|array|
|:---:|
|0|
|1 --> c --> d|
|2|
|3 --> a --> b|
|4 --> e --> f --> g|
Properties:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. memory: O(m+n).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. time: O(c+1), c is the length of the longest chain.<br>


I finished most of exams except<br>
'00_process_packages.py'<br>
'01_merging_tables.py'<br>
'02_hash_substring.py'<br>
'03_rope.py'<br>
<br>
#**Important Note:**<br>
In 01_job_queue.py, time exceeds limit when using my heap function, so I turned to using python module heapq. But heapq module looks no better than my code. It also uses sift_down and sift_up function.<br> 
In 03_set_range_sum.py, I implement insert, erase and search by myself. Wateching splay tree visualization helps to solve this problem.<br>
https://www.cs.usfca.edu/~galles/visualization/SplayTree.html<br>
Strange thing is that the logic between online visualization and lecture is not really the same, and online visulization seems to more makes sense to me.

# Algorithmic Toolbox

Algorithmic Toolbox covers basic algorithmic techniques and ideas for computational problems arising frequently in practical applications: sorting and searching, divide and conquer, greedy algorithms, dynamic programming. I learn a lot of theory: how to sort data and how it helps for searching; how to break a large problem into pieces and solve them recursively; when it makes sense to proceed greedily; how dynamic programming is used in genomic studies.

## Description

This section provides a brief overview of the course content for each week.

- Week 1: Programming Challenges  
  Finish all problems.

- Week 2: Algorithmic Warm-Up  
  Finished the problems 1 to 6. The problems 7 to 8 is too hard.  

- Week 3: Greedy Algorithms  
  Not all problems can be solved by greedy algorithms. So, make sure the first safe choice is optimal choice. Then you can continue. If not, then greedy algorithm is probably not the way to go.  
  Finished the problems 1 to 3. The problems 4 to 7 is too hard.

- Week 4: Divide-and-Conquer  
  binary search, selection sort, merge sort, non-counting sort, quick sort. Finsih the problems from 1 to 3. The problems 4 to 7 is too hard.

- Week 5: Dynamic Programming 1  
  Finish problems 1 to 3. 

  - An advaned question:
    We want to compute not only the edit distance $d$ between two words, but also the number of ways to edit the first
    word to get the second word using the minimum number $d$ of edits. Two ways are considered different if there is
    such $i$, $1 < 4 < d$  that on the $i$-th step the edits in these ways are different.
    
    To solve this problem, in addition to computing array $T$ with edit distances between prefixes of the first and
    second word, we compute array $ways$, such that:
    $$
    ways[i, j] = \text{the number of ways to edit the prefix of length i of the first word to get the prefix of length j of the second word using the minimum possible number of edits}.
    $$

    The following is the correct way to compute $ways[i, j]$ based on the previously computed values:
    ```
    ways[i, j] = 0
    if T[i, j] == T[i - 1, j] + 1:
        ways[i, j] += ways[i - 1, j]
    if T[i, j] == T[i, j - 1] + 1:
        ways[i, j] += ways[i, j - 1]
    if word1[i] == word2[j] and T[i, j] == T[i - 1, j - 1]:
        ways[i, j] += ways[i - 1, j - 1]
    if T[i, j] == T[i - 1, j - 1] + 1:
        ways[i, j] += ways[i - 1, j - 1]
    ```
    $T[i, j]$ is computed based on $T[i-1, j]$, $T[i, j-1]$ and $T[i-1, j-1]: we decide what will be
    the last edit and then try to use the minimum number of edits needed before that, which is already stored
    in the table $T$ for all the variants of the last editing action. If the minimum number of edits $T[i, j]$ can be
    obtained via different last editing actions, we should sum all the ways that exactly $T[i, j]$ edits can be
    made to change the $i$-th prefix of the first word into the $j$-th prefix of the second word.
    First $\text{\textit{if}}$ checks all the ways when the last action is to delete the last symbol. Second $\text{\textit{if}}$ checks all the ways
    when the last action is to insert the necessary symbol. Third $\text{\textit{if}}$ checks all the ways to match last symbols of
    the prefixes. Last $\text{\textit{if}}$ checks all the ways to replace the last symbol of the $i$-th prefix of the first word by the
    last symbol of the $j$-th prefix of the second word.

- Week 6: Dynamic Programming 2  
  Finish problems 1 and 3.


## Reference:

- Week 1:

- Week 2:

- Week 3:

- Week 4:
  - [Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms)

- Week 5:
  - [Making Change Animation](https://www.cs.usfca.edu/~galles/visualization/DPChange.html)
  - [Edit Distance Calculator](http://www.let.rug.nl/kleiweg/lev/)
  - [Longest Common Subsequence](https://www.cs.usfca.edu/~galles/visualization/DPLCS.html): the longest common subsequence problem is a special case of the edit distance problem where we allow insertions and deletions only
  - Chapter 5 "How Do We Compare Biological Sequences" of [CP]
  - [Additional Slides](https://www.dropbox.com/s/qxzh146jd72188d/dynprog.pdf?dl=0)

- Week 6:
  - [Polynomial vs Pseudopolynomial](https://stackoverflow.com/questions/4538581/why-is-the-knapsack-problem-pseudo-polynomial#answer-4538668)
  - Knapsack: Section 6.4 of [DPV]

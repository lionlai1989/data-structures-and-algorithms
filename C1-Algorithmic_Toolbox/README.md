# Algorithmic Toolbox

## Description

This section provides a brief overview of the course content for each week.

### Week 1: Programming Challenges

The first week of this specialization emphasizes that identifying smarter
problem-solving approaches can significantly reduce processing compared to naive
algorithms.

### Week 2: Algorithmic Warm-Up

This week's objective is to demonstrate how a clever insight can make an algorithm for a
problem significantly faster, potentially achieving a billion-fold improvement. This
concept is illustrated through classical problems involving Fibonacci numbers, greatest
common divisors, and least common multiples.

### Week 3: Greedy Algorithms

Not all problems are suited for greedy algorithms. However, if a problem can be tackled
using a greedy approach, it generally adheres to the following pattern: make the first
safe choice the optimal choice and continue by consistently selecting that choice for
subsequent steps. If the initial safe choice isn't the optimal one, then a greedy
algorithm is probably not appropriate for solving that specific problem.

### Week 4: Divide-and-Conquer

Divide and conquer is a classical strategy applicable to various algorithms, including
binary search, polynomial multiplication, selection sort, merge sort, counting sort, and
quick sort.

### Week 5: Dynamic Programming 1

Dynamic programming is a problem-solving technique that involves breaking down a complex
problem into a sequence of simpler subproblems, solving each subproblem only once, and
storing the results in a table to avoid redundant computations. The central idea is to
build solutions to larger problems by using solutions to smaller problems. This approach
begins by solving the smallest subproblem and incrementally progressing towards the
desired problem size, with each step relying on the solutions to previous, smaller
subproblems. Such a process minimizes redundant work and significantly enhances the
overall efficiency of problem-solving.

It often works well for problems with overlapping subproblems and optimal substructure.
It can be applied to solve common problems such as the money change problem and
calculating the edit distance between two strings.

### Week 6: Dynamic Programming 2

A typical problem which can be solved with dynamic programming is Maximum Amount of
Gold.

## Reference:

-   Week 1:

-   Week 2:

    -   [Big-O Visualization](https://htmlpreview.github.io/?https://github.com/lionlai1989/data-structures-and-algorithms/blob/master/C1-Algorithmic_Toolbox/bigo.html)

-   Week 3:

-   Week 4:

    -   [Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms)

-   Week 5:

    -   [Making Change Animation](https://www.cs.usfca.edu/~galles/visualization/DPChange.html)
    -   [Edit Distance Calculator](http://www.let.rug.nl/kleiweg/lev/)
    -   [Longest Common Subsequence](https://www.cs.usfca.edu/~galles/visualization/DPLCS.html):
        the longest common subsequence problem is a special case of the edit distance
        problem where we allow insertions and deletions only
    -   Chapter 5 "How Do We Compare Biological Sequences" of [CP]
    -   [Additional Slides](https://www.dropbox.com/s/qxzh146jd72188d/dynprog.pdf?dl=0)

-   Week 6:

    -   [Polynomial vs Pseudopolynomial](https://stackoverflow.com/questions/4538581/why-is-the-knapsack-problem-pseudo-polynomial#answer-4538668)
    -   Knapsack: Section 6.4 of [DPV]

    <!-- -   An advaned question: We want to compute not only the edit distance $d$ between
        two words, but also the number of ways to edit the first word to get the second
        word using the minimum number $d$ of edits. Two ways are considered different if
        there is such $i$, $1 \leq i \leq d$ that on the $i$-th step the edits in these
        ways are different.

            To solve this problem, in addition to computing array $T$ with edit distances
            between prefixes of the first and second word, we compute array $ways$, such
            that:

            $$
            ways[i, j] = \text{the number of ways to edit the prefix of length i of the first word to get the prefix of length j of the second word using the minimum possible number of edits}.
            $$

            The following is the correct way to compute $ways[i, j]$ based on the previously
            computed values:

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

            $T[i, j]$ is computed based on $T[i-1, j]$, $T[i, j-1]$ and
            $T[i-1, j-1]: we decide what will be

        the last edit and then try to use the minimum number of edits needed before
        that, which is already stored in the table $T$ for all the variants of the last
        editing action. If the minimum number of edits $T[i, j]$ can be obtained via
        different last editing actions, we should sum all the ways that exactly
        $T[i, j]$ edits can be made to change the $i$-th prefix of the first word into
        the $j$-th prefix of the second word. First $\text{\textit{if}}$ checks all the
        ways when the last action is to delete the last symbol. Second
        $\text{\textit{if}}$ checks all the ways when the last action is to insert the
        necessary symbol. Third $\text{\textit{if}}$ checks all the ways to match last
        symbols of the prefixes. Last $\text{\textit{if}}$ checks all the ways to
        replace the last symbol of the $i$-th prefix of the first word by the last
        symbol of the $j$-th prefix of the second word. -->

# Data Structures and Algorithms

This repository hosts materials for the course,
[Data Structures and Algorithms Specialization](https://www.coursera.org/specializations/data-structures-algorithms),
offered by Coursera and UC San Diego, including my own solutions to the problems.

## Description

This specialization explores fundamental in data structures and algorithms and is
divided into six series courses, each offering thorough explanation and unique insights
into this field.

-   [Algorithmic Toolbox](https://github.com/lionlai1989/data-structures-and-algorithms/tree/master/C1-Algorithmic_Toolbox):  
    The initial course covers algorithmic strategies, including greedy algorithms,
    divide-and-conquer algorithms, and dynamic programming. These three techniques are
    better described as strategic approaches rather than specific algorithms. The
    principles underlying these strategies are readily observable in more specialized
    algorithms. For instance, merge sort exemplifies the divide-and-conquer algorithm,
    and dynamic programming can be applied to solve problems like finding the shortest
    path in an undirected graph.

-   [Data Structures](https://github.com/lionlai1989/data-structures-and-algorithms/tree/master/C2-Data_Structures):  
    To maximize the potential of good algorithms, it's essential to have efficient data
    structures for data manipulation. In this course, I delve into various data
    structures, including arrays, linked lists, and hash tables, gaining a comprehensive
    understanding of their strengths and weaknesses and when to employ each of them.

-   [Algorithms on Graphs](https://github.com/lionlai1989/data-structures-and-algorithms/tree/master/C3-Algorithms_on_Graphs):


-   [Algorithms on Strings](https://github.com/lionlai1989/data-structures-and-algorithms/tree/master/C4-Algorithms_on_Strings):
    

## Getting Started

All the results in this repository can be reproduced by following the instructions
below.

### System Dependencies

Before you start, you need to make sure you have the following dependencies installed:

-   **Python-3.10**:
-   **C++**:

### Downloading

-   To download this repository, run the following command:

```shell
git clone https://github.com/lionlai1989/data-structures-and-algorithms.git
```

### Install Dependencies

#### Python

-   Create and activate a Python virtual environment

```
python3.10 -m venv venv_algorithms && source venv_algorithms/bin/activate
```

-   Update `pip` and `setuptools`:

```
python3 -m pip install --upgrade pip setuptools
```

-   Install required Python packages in `requirements.txt`.

```
python3 -m pip install -r requirements.txt
```

#### C++

### Running Code

Now you are ready to run the code of each programming language.

#### Python

Please remember to select the kernel you just created in your virtual environment
`venv_algorithms`.

```python
python3
```

#### C++

```cpp
g++ -pipe -O2 -std=c++11
```

### Document

The table of contents of this file can be regenerated with the following steps.

-   Create a `temp` folder and copy/paste this `README.md` file into `temp`.
-   `cd` to `temp` and run `docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc`
-   Copy/paste `README.md` to the original location and delete `temp`.

## Help

Any feedback, comments, and questions are welcome.

## Authors

[@lionlai](https://github.com/lionlai1989)

## Version History

-   2.0.0
    -   Continue this course in 2023 and aim to understand EVERYTHING.
-   1.0.0
    -   Finish first three courses in 2016, but didn't continue till the end.

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for
details

## Acknowledgments

Explore the inspiration and references listed here to further expand your knowledge and
sharpen your skills.

-   [Ace Your Next Coding Interview by Learning Algorithms](https://stepik.org/course/102772/promo?utm_source=bookwebpage&utm_medium=intro)
-   [DISCRETE MATHEMATICS for Computer Science](http://discrete-math.tilda.ws/?utm_source=coursera&utm_medium=reading&utm_campaign=toolbox)
-   [DPV] Sanjoy Dasgupta, Christos Papadimitriou, and Umesh Vazirani. Algorithms (1st
    Edition). McGraw-Hill Higher Education. 2008.
-   [CP] Phillip Compeau, Pavel Pevzner. Bioinformatics Algorithms: An Active Learning
    Approach. Active Learning Publishers. 2014.
-   [Bioinformatics Algorithms: An Active Learning Approach](): it talks a lot of things
    about string pattern matching.

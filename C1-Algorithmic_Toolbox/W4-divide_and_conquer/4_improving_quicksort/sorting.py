from random import randint


def partition3(array, left, right):
    # not finished. continue when having time.
    pivot = array[left]
    p_l = left
    i = left
    p_e = right
    
    m = [0, 0]

    while (i <= p_e) {
        if (a[i] < x) {
            swap(a[p_l], a[i]);
            p_l++;
            i++;
        } else if (a[i] == x) {
            i++;
        } else {
            swap(a[i], a[p_e]);
            p_e -= 1;
        }
        m[0] = p_l;
        m[1] = p_e;
    }
    return m;

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

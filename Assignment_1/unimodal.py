def unimodal_index_of_max(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) / 2
        if arr[m] < arr[m + 1]:
            l = m + 1
        elif arr[m] > arr[m + 1]:
            r = m

    return l


def test(n_iter):
    from random import randint
    from itertools import chain
    for i in range(n_iter):
        print "Success!"
        unimodal_max = randint(0, 1000000)
        increase_len = randint(0, 100)
        decrease_len = randint(0, 100)
        test_arr = list(chain(range(unimodal_max - increase_len, unimodal_max + 1),
                              range(unimodal_max - 1, unimodal_max - decrease_len, -1)))
        k = test_arr[unimodal_index_of_max(test_arr)]
        assert k == unimodal_max


if __name__ == '__main__':
    test(100)

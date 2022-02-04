import copy


class BubbleSort:
    @staticmethod
    def apply(array):
        arr = copy.copy(array)
        for i in range(len(arr) - 1):
            swapped = False
            for k in range(len(arr) - i - 1):
                if arr[k] > arr[k + 1]:
                    buff = arr[k]
                    arr[k] = arr[k + 1]
                    arr[k + 1] = buff
                    swapped = True
            if not swapped:
                break
        return arr


class ShakerSort:
    @staticmethod
    def apply(array):
        arr = copy.copy(array)
        begin = 0
        end = len(arr) - 1
        swapped = True
        while swapped:
            swapped = False
            for k in range(begin, end):
                if arr[k] > arr[k + 1]:
                    buff = arr[k]
                    arr[k] = arr[k + 1]
                    arr[k + 1] = buff
                    swapped = True
            end -= 1
            for k in range(end, begin, -1):
                if arr[k] < arr[k - 1]:
                    buff = arr[k]
                    arr[k] = arr[k - 1]
                    arr[k - 1] = buff
                    swapped = True
            begin += 1
        return arr


class CombSort:
    @staticmethod
    def apply(array):
        arr = copy.copy(array)
        gap = len(arr)
        swapped = True
        while gap > 1 or swapped:
            swapped = False
            gap = max(int(gap / 1.247), 1)
            for k in range(len(arr) - gap):
                if arr[k] > arr[k + gap]:
                    buff = arr[k]
                    arr[k] = arr[k + gap]
                    arr[k + gap] = buff
                    swapped = True
        return arr

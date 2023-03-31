from math import sqrt, erfc
from scipy.special import gammainc


def frequency_test(subsequence: str) -> float:
    n = len(subsequence)
    summ = 0
    for i in subsequence:
        if i == '1':
            summ += 1
        else:
            summ -= 1
    return erfc(1 / sqrt(2 * n) * summ)


def identical_consecutive_bit_test(subsequence: str) -> float:
    n = len(subsequence)
    s = 0
    for i in subsequence:
        s += 1 if i == '1' else 0
    s = s / n
    p_value = 0
    if abs(s - 0.5) < 1 / sqrt(n):
        v_n = 0
        for i in range(n - 1):
            if subsequence[i] != subsequence[i + 1]:
                v_n += 1
        p_value = erfc(abs(v_n - 2*n*s*(1 - s)) / (sqrt(8 * n) * s * (1 - s)))
    return p_value


def longest_sequence_of_ones_test(subsequence: str) -> float:
    n = len(subsequence)
    units = [0] * (n // 8)
    for i in range(len(units)):
        cur_one_sequence = 0
        for j in range(8):
            if subsequence[i * 8 + j] == '1':
                cur_one_sequence += 1
            else:
                if units[i] < cur_one_sequence:
                    units[i] = cur_one_sequence
                cur_one_sequence = 0
        if units[i] < cur_one_sequence:
            units[i] = cur_one_sequence
    v = [units.count(0) + units.count(1), units.count(2), units.count(3),
         len(units) - units.count(0) - units.count(1) - units.count(2) - units.count(3)]
    pi = [0.2148, 0.3672, 0.2305, 0.1875]
    x_2 = 0
    for i in range(4):
        x_2 += ((v[i] - 16 * pi[i]) ** 2) / (16 * pi[i])
    p_value = gammainc(1.5, x_2 / 2)
    return p_value


if __name__ == '__main__':
    bit_sequence = "11100010010111010010101001010000110011110100100110011010000100101101011110001101100111010000010111101111011110100010010000110101"
    print(f'\nЧастотный побитовый тест: {frequency_test(bit_sequence)}')
    print(f'Тест на одинаковые подряд идущие биты: {identical_consecutive_bit_test(bit_sequence)}')
    print(f'Тест на самую длинную последовательность единиц в блоке: {longest_sequence_of_ones_test(bit_sequence)}')

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            arr_index = ord(char) - ord("a")
            alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(
    "정답 = [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
    find_alphabet_occurrence_array("hello my name is dingcodingco"),
)
print(
    "정답 = [1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0] \n현재 풀이 값 =",
    find_alphabet_occurrence_array("we love algorithm"),
)
print(
    "정답 = [0, 3, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
    find_alphabet_occurrence_array("best of best youtube"),
)

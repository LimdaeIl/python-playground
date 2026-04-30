def find_alphabet_occurrence_array(string):
  alphabet_occurrence_array = [0] * 26

  for char in string:
    if char.isalpha():
      arr_index = ord(char) - ord("a")
      alphabet_occurrence_array[arr_index] += 1

  return alphabet_occurrence_array

input = "abadabac"

# 0(N)
def find_not_repeating_first_character(string):
    # string 에서 알파벳의 빈도수를 찾는다.
    # 그리고 빈도수가 1인 알파벳 중에서 string 에서 뭐가 먼저 나왔는지를 찾아본다.
    occurrence_array = find_alphabet_occurrence_array(string)

    not_repeating_character_array = []

    for index in range(len(occurrence_array)):
      alphabet_occurrence = occurrence_array[index]
      if alphabet_occurrence == 1:
        not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
      if char in not_repeating_character_array:
        return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

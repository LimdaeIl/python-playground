def sieve_of_eratosthenes(n):
  # 0 ~ n까지 True로 초기화 (소수 후보)
  is_prime = [True] * (n + 1)

  # 0과 1은 소수가 아님
  is_prime[0] = False
  is_prime[1] = False

  # 2부터 √n까지 반복
  for i in range(2, int(n ** 0.5) + 1):
    # 아직 소수라면
    if is_prime[i]:
      # i의 배수 제거 (i*i부터 시작)
      for j in range(i * i, n + 1, i):
        is_prime[j] = False

  # 소수만 추출
  primes = []
  for i in range(2, n + 1):
    if is_prime[i]:
      primes.append(i)

  return primes


# 테스트
print(sieve_of_eratosthenes(30))
# 결과: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
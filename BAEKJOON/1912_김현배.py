# n개의 정수로 이루어진 임의의 수열이 주어진다.
# 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
# 단, 수는 한 개 이상 선택해야 한다.
# 예를 들어서 10,-4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어져싸고 하자.
# 여기서 정답은 12+21 인 33이 정답이 된다.

# 1912 연속합
n = int(input())  # n개의 수열 설정
a = list(map(int, input().split()))  # n개 수열 입력
sum = [a[0]]  # sum[0]을 a[0]으로 비교를 위해 설정
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
# sum의 i번째 인덱스와 a의 i+1번째 인덱스의 숫자를 더한 값과 a의 i+1번째 숫자 비교
print(max(sum))

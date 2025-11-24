# 입력 : 첫째 줄에 파일 이름의 개수 n이 주어진다. 둘째 줄부터 n개의 줄에는 파일 이름이 주어진다. n은 50보다 작거나 같은 자연수 이고, 파일 이름의 길이는 모두 같고 길이는 최대 50이다. 파일이름은 알파벳 소문지와 '.' 로만 이루어져 있다.
# 출력 : 첫째 줄에 패턴을 출력하면 된다.

num = int(input())
word = list(input())

for _ in range(num-1):
    word_2 = input()
    for n in range(len(word)):
        if word[n] == word_2[n]:
            continue
        else:
            word[n] = "?"
print(*word, sep = "")

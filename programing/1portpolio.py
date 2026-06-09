# 예외 처리 기법
try:
    print(sad)
except:
    print("오류 발생")

# 오류 내용까지 알아보자
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# try finally 문
try:
    f = open("foo.txt", "w")

finally:
    f.close() # 중간에 오류가 발생하더라도 무조건 실행

# 0으로 나누는 오류와 인덱싱 오류 처리
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다")

# 또는

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# try-else 문
try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")
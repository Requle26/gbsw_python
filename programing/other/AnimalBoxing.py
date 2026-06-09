import requests

MODEL_NAME = "qwen2.5:14b"

messages = [
    {
        "role": "system",
        "content": "너는 항상 한국어로만 대답해야 해. 한자나 다른 언어는 사용하면 안 돼. 문법이 자연스럽고 정확해야 해. 답변은 논리적이고 자세하게 해."
    }
]

def ask_ai(prompt):
    messages.append({"role": "user", "content": prompt})

    response = requests.post("http://localhost:11434/api/chat", json={
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.7
        }
    })

    reply = response.json()["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply


print("--- 우리랑 맞짱 뜰 사람? ---")

field = input("전장 입력 : ")

print("--- 첫번째 상대 ---")
creature_type1 = input("첫번째 상대 종족타입 : ")
creature_name1 = input("첫번째 상대 이름 선택 : ")
sd1 = input("첫번째 상대 특수 능력(없으면 '없음' 기입) : ")

print("--- 두번째 상대 ---")
creature_type2 = input("두번째 상대 종족타입 : ")
creature_name2 = input("두번째 상대 이름 선택 : ")
sd2 = input("두번째 상대 특수 능력(없으면 '없음' 기입) : ")


prompt = f"""
두 명의 생명체가 싸울 거야.

전투 조건:
- 둘 다 사력을 다함
- 둘 다 죽음을 두려워하지 않음
- 싸움 장소: {field}

첫번째 상대:
- 종족: {creature_type1}
- 이름: {creature_name1}
- 특수 능력: {sd1}

두번째 상대:
- 종족: {creature_type2}
- 이름: {creature_name2}
- 특수 능력: {sd2}

아래 내용을 자세하게 분석해줘.

1. 전체 전투 흐름
2. 첫번째 상대 승률
3. 두번째 상대 승률
4. 승리 가능성이 높은 쪽
5. 승리 이유
6. 진 쪽의 패배 원인
7. 진 쪽에게 줄 피드백
8. 다음 추천 상대

"""

print("답변 생성중입니다. 잠시만 기다려주세요...")

reply = ask_ai(prompt)
print(f"AI: {reply}\n")
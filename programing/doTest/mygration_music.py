import random

musicList = (("Sunflower - Post Malone & Swae Lee", "Pink + White - Frank Ocean", "Oui - Jeremih"),
("4EVA - KAYTRAMINE, Amine, KAYTRANDA & Pharrell Williams", "Blue - PinkPantheress", "Another Dimension - Pop Money"),
("Hotline Bling - Drake", "The Way Life Goes - Lil Uzi Vert", "20 Min - Lil Uzi Vert"))

customMusic = []
select = False

def musicChoicer(weather, feels):
    result = f"오늘 {musicList[weather][feels]}, 들어보시는건 어떤가요?"
    return result

def addMusic():
    admusic = ""
    while True:
        admusic = input("음악 입력: ")
        if admusic == "0":
            break
        customMusic.append(admusic)
    return

def cMusicChoicer():
    global customMusic
    cMusicLen = len(customMusic)
    randomNum = f"{random.random()*cMusicLen:.0f}"
    randomNum = int(randomNum)

    if len(customMusic) > 1:
        randomNum = random.randrange(0, cMusicLen)
        answer = f"오늘 {customMusic[randomNum]}, 들어보시는건 어떤가요?"
        return answer
    else:
        answer = "두개 이상의 음악을 추가해주세요!"
        return answer



print("""----------------
1. 커스텀 뮤직
2. 기본 음악 추천""")
defalt = int(input("정수를 입력해주세요: "))

if defalt == 2:
    select = True
    print("-------- 오늘의 날씨를 입력하세요! --------")
    print("""|  1. 맑음
|  2. 흐림
|  3. 비옴""")
    weather = int(input("정수를 입력해주세요: "))-1

    print("--------- 현재 시간을 입력하세요! ---------")
    print("""|  1. 아침
|  2. 점심
|  3. 저녁""")
    feels = int(input("정수를 입력해주세요: "))-1
    print()
    print(musicChoicer(weather, feels))

elif select == False:
    print("-------- 추가할 음악을 입력해주세요 (0을 입력해 추가 종료 및 추천받기) --------")
    addMusic()
    cMusicChoicer()


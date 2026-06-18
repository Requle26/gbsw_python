        if len(customMusic) > 1:
            cMusicLen = len(customMusic)
            randomNum = f"{random.random()*cMusicLen:.0f}"
            print(f"오늘 {customMusic[randomNum]}, 들어보시는건 어떤가요?")
        else:
            print("두개 이상의 음악을 추가해주세요!")
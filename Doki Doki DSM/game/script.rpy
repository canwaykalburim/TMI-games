define ch_TaeHyeon = Character("태현", color = "#0000ff")

image TaeHyeon:
    im.FactorScale ("ch/TaeHyeon.png", 2.8)
    yalign 0.0

image School:
    im.FactorScale ("bg/DSM.png", 2.2)

define center = Position(xalign = 0.5)
define left = Position(xalign = 0.2)
define right = Position(xalign = 0.8)

label start:

    play music "BGM/Doki Doki Literature Club_Ohayou Sayori.wav"

    scene School with fade

    "20XX년 3월 2일"

    "오늘은 태현이의 두근두근 첫 등교일이다."

    "태현이가 입학한 학교는 대한민국 최고의 명문고 DSM"

    "DSM은 세계적으로도 유명한 학교이며 누구나 이 학교에 다니고 싶어한다."

    "태현이는 새 친구들과 선생님을 만날 생각에 들뜬 마음으로 학교에 들어섰다."

    show TaeHyeon

    ch_TaeHyeon "여기가 대한 스페셜 마이스터(Daehan Special Meister) 고등학교인가?"

    hide TaeHyeon

    "이 학교는 아마 태현이의 밝은 미래를 위한 출발선이 될 것이다."

    "적어도 태현이는 그렇게 생각하고 있다."

    "아니 적어도 태현이는 그렇게 생각하고 있었다."

    "태현이는 두근거리는 긴장감을 갖고 교실로 들어가려고 했다."

    return

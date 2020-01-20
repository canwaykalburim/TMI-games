define ch_SangHai = Character("상하이 조", color = "#600080")
define ch_TaeHyeon = Character("태현", color = "#0000ff")
define ch_YoonSu = Character("윤수", color = "#f7d600")
define ch_YoonJu = Character("윤주", color = "#ff8800")
define ch_HoSeung = Character("호승", color = "##00cc00")
define q = Character("???", color = "#000000")

image AngrySH:
    im.FactorScale ("ch/AngrySH.png", 2.88)
    yalign 0.0, xalign 0.0

image BackSH:
    im.FactorScale("ch/BackSH.png", 0.9)
    yalign 0.3

image BlackHS:
    im.FactorScale("ch/BlackHS.png", 0.65)
    yalign 0.5, xalign 1.0

image BossHS:
    im.FactorScale("ch/BossHS.png", 0.65)
    yalign 0.5, xalign 1.0

image BraveHS:
    im.FactorScale("ch/BraveHS.png", 2.0)
    yalign 1.0

image BraveTH:
    im.FactorScale ("ch/BraveTH.png", 0.7)
    yalign 0.05

image GreatTH:
    im.FactorScale ("ch/GreatTH.png", 1.35)
    yalign 0.0

image KillerSH:
    im.FactorScale ("ch/KillerSH.png", 2.73)
    yalign 0.0, xalign 1.0

image SangHai:
    im.FactorScale ("ch/SangHai.png", 2.2)
    yalign 0.35, xalign 0.0

image SmileSH:
    im.FactorScale ("ch/SmileSH.png", 1.8)
    yalign 0.2, xalign 0.0

image SurpSH:
    im.FactorScale("ch/SurpSH.png", 1.18)
    yalign -1, xalign 1.0

image SurpYoonSu:
    im.FactorScale ("ch/SurpYoonSu.png", 2.5)
    yalign 0.2

image TaeHyeon:
    im.FactorScale ("ch/TaeHyeon.png", 3)
    yalign 0.0

image TalkingSH:
    im.FactorScale("ch/TalkingSH.png", 0.993)
    xalign 1.0, yalign 0.0

image YoonJu:
    im.FactorScale ("ch/YoonJu.png", 1.5)
    yalign 0.25, xalign 1.0

image YoonSu:
    im.FactorScale ("ch/YoonSu.png", 0.95)
    yalign 0.2
image SmileHS:
    im.FactorScale ("ch/SmileHS.png", 1.0)
    yalign 0.5
image Street = "bg/street.png"

#define narrator = Character(None, kind = nvl)
#define ch_narrator = Character(None)
define center = Position(xalign = 0.5)
define left = Position(xalign = 0.0)
define right = Position(xalign = 1.0)

transform movetoright:
    linear 0.5 xalign 1.0
transform movetoleft:
    linear 0.5 xalign 0.0

# 스토리

label start: # part1

    $Interchange = 0

    play music "BGM/Doki Doki Literature Club_Ohayou Sayori.wav"

    scene Street with fade

    "화창하고 평범한 어느 아침"
    "따사로운 햇살이 태현이를 간질인다"
    "눈부신 햇살이 기분 좋은날"
    "태현이는 이 기분 좋은 하루가 계속 되기를 기대하며 오늘도 학교에 가기 위해 길을 걷고 있다"
    "그러던 중 저 멀리서 태현이의 같은 반 친구들이 보인다"

    show TaeHyeon at center with dissolve

    ch_TaeHyeon "안녕 얘들아"

    "태현이가 반갑게 인사한다"

    hide TaeHyeon
    show SangHai

    ch_SangHai "안녕하시오"

    "상하이 조가 반갑게 인사한다"

    hide SangHai
    show YoonSu at center

    ch_YoonSu "그래 안녕"
    
    "윤수는 부끄러운지 얼굴을 가리고 인사를 한다"

    hide YoonSu with moveoutleft
    show YoonJu with moveinright

    ch_YoonSu "???"
    ch_YoonJu "하이!"

    "가만히 있는 윤수를 굳이 밀어내고 끼어들어 인사하는 윤주"

    show TaeHyeon at left with moveinleft

    ch_TaeHyeon "하 하 하"
    ch_YoonJu "하 하 하"
    ch_TaeHyeon "너한테는 안 했어!"
    ch_YoonJu "아니이..."
    ch_YoonJu "하... 서러워서 진짜..."

    "갑자기 끼어든 윤주에게도 태현이는 친절히 인사해 주었다"

    hide YoonJu
    hide TaeHyeon

    "갑자기 끼어든 윤주에게 태현이는 친절하게 인사해 주었고"
    "윤주는 언제나 그렇듯 갑자기 서러워하고"
    "그렇게 태현이와 친구들은 평소와 다를 것 없이 서로 반갑게 인사를 나누며 학교에 가는 중이다"
    "그러던 그 때"
    "태현이는 문득 이상한 기분이 들었다"

    show TaeHyeon at center

    ch_TaeHyeon "잠깐...!"
    ch_TaeHyeon "근데 얘들아... 우리 중에 누구 이상한 사람 있지 않았니??"

    hide TaeHyeon
    play music "BGM/Doki Doki Literature Club_Sayo Nara.wav"

    "아무래도 태현이의 기분 좋은 하루는 벌써 끝이 난 것 같다"

    show YoonSu at center

    ch_YoonSu "....."
    ch_YoonSu "흠..."
    ch_YoonSu "그랬나...?"
    ch_YoonSu "그런것 같기도 하고..."
    ch_YoonSu "혹시 장난 치는 건 아니지??"

    hide YoonSu

    "무서운지 약간 떨고 있는 듯한 윤수"
    "장난이라고 말해줄 수는 있었지만"
    "진실을 숨길 수는 없는 법"

    show TaeHyeon at center

    ch_TaeHyeon "흠..."
    ch_TaeHyeon "진짜인것 같은데?"

    hide TaeHyeon
    show YoonSu

    ch_YoonSu "....."

    hide YoonSu
    show TaeHyeon

    ch_TaeHyeon "?"

    hide TaeHyeon
    show YoonSu

    ch_YoonSu "....."

    hide YoonSu
    show TaeHyeon

    ch_TaeHyeon "??"

    hide TaeHyeon
    show YoonSu

    ch_YoonSu "!!!!!"

    hide YoonSu
    show TaeHyeon

    ch_TaeHyeon "?????"

    hide YoonSu
    hide TaeHyeon

    show SurpYoonSu

    ch_YoonSu "으아아아아아아악!"

    hide SurpYoonSu

    ch_SangHai "하... 이런..."
    ch_SangHai "자연스럽다고 생각했는데"
    ch_SangHai "결국 들켰구만?"

    show AngrySH with dissolve

    ch_SangHai "하... 어쩌지?"
    ch_SangHai "귀찮게 됐네..."
    ch_SangHai "생각보다 눈치가 빠른 놈들이구만"
    ch_SangHai "일단은 들켰으니까..."
    ch_SangHai "싸워야 겠지?"

    hide AngrySH

    "갑작스럽게 나타나 태현이 일행에게 모습을 드러낸 상하이 조"
    "상하이 조는 조금씩 태현이 일행에게 다가오고 있다"

    menu:
        "어떻게 해야할까"
        "쓰러트린다":
            $Interchange -= 1
            call Fight_Ending
        "도망간다":
            $Interchange += 1
            call Run_Ending

    jump part_two

    return


label part_two: #part2

    "상하이 조는 총을 꺼내들었다"

    show BraveTH at center

    ch_TaeHyeon "!!!"
    ch_TaeHyeon "생각 보다 더 위험한 놈이었군..."

    hide KillerSH
    hide BraveTH

    "태현이는 잠시 당황 했지만 이내 침착을 되찾았다"

    show KillerSH

    ch_SangHai "호오 총을 보고도 놀라지 않다니..."
    ch_SangHai "생각보다 더 용감한 놈이구만"
    ch_SangHai "이거 진짜 총이라구?"

    hide KillerSH

    "태현이는 아무말도 하지 않았다"
    "대신 태현이는 살며시 미소를 지었다"

    show KillerSH

    ch_SangHai "뭐야 지금 웃는거야?"
    ch_SangHai "막상 죽을 생각을 하니 무서워서 미친거구만?"

    hide KillerSH

    "태현은 미소를 유지하며 조금씩 입을 열기 시작했다"

    show GreatTH
    
    ch_TaeHyeon "아니... 그냥..."
    ch_TaeHyeon "다행이라 생각해서..."

    hide GreatTH

    "상하이 조는 의아해하며 고개를 갸웃했다"

    show GreatTH

    ch_TaeHyeon "너와 얘기하는 동안 친구들이 모두 도망갔거든"
    ch_TaeHyeon "설령 여기서 너와 싸워서 진다고 해도..."
    ch_TaeHyeon "친구들은 무사하겠지"
    ch_TaeHyeon "난 그걸로 만족해"

    hide GreatTH

    "태현의 눈에는 조금의 후회도 없었다"

    show BraveTH

    ch_TaeHyeon "혹여나 내가 죽으면 반드시 친구들이 내 복수를 해줄거야!"
    ch_TaeHyeon "그렇기에 내 희생은 헛되지 않아!"
    ch_TaeHyeon "그러니 긴 소리하지 말고 덤벼!"

    hide BraveTH
    show AngrySH

    ch_SangHai "....."
    ch_SangHai "....."

    hide AngrySH
    show SmileSH

    play music "BGM/Doki Doki Literature Club_Ohayou Sayori.wav"

    ch_SangHai "하하하!"
    ch_SangHai "죽을 수도 있는 상황에서 그런 말이 나오다니"
    ch_SangHai "가히 영웅급의 희생정신인데?"
    ch_SangHai "이거 이거... 재밌는 놈인걸?"
    ch_SangHai "흠... 죽이기에는 너무 아깝단 말이지..."
    ch_SangHai "이봐"
    ch_SangHai "너에게 한 번의 기회를 주지"
    ch_SangHai "너 우리랑 함께 일 해보지 않을래?"

    hide SmileSH

    "방금 전까지 태현이의 일행을 위협하던 상하이 조가 갑작스럽게 태현이에게 협력을 요청하였다"

    menu:
        "그의 제안에 승낙할까?"
        "승낙한다":
            $Interchange += 1
            show BraveTH
            jump Agreement_Ending
        "거절한다":
            show BraveTH
            $Interchange -= 1
            jump Refusal_Ending
        "침묵한다":
            show BraveTH
            jump Silence_Ending

    return

# 엔딩 조건

label Run_Ending: # 도망친다

    "태현이는 조금 떨면서 말했다"

    show TaeHyeon at center

    ch_TaeHyeon "위험해...!"
    ch_TaeHyeon "우리가 상대할 수 있을만한 사람은 아닌 것 같아..."

    "태현이는 뒤를 돌아보며 소리쳤다"

    hide TaeHyeon
    show BraveTH at center with dissolve

    ch_TaeHyeon "얘들아 도망가!!"
    ch_TaeHyeon "여기는 내가 막고 있을테니까..."

    show BraveTH at movetoleft

    "윤수가 태현이의 말에 끼어들며 소리쳤다"

    show YoonSu at right with moveinright

    ch_YoonSu "헛소리 하지마!"
    ch_YoonSu "우리가 널 버리고 어떻게 도망가?"
    ch_YoonSu "우리도 저 녀석을 막을 수 있게 해줘!"

    "태현이는 윤수의 말에 미소를 지으며 대답했다"

    ch_TaeHyeon "고맙기는 한데 저 사람을 우리가 이길 수 있을 것 같지는 않아"
    ch_YoonSu "그럼 너도 같이 도망가자"
    ch_TaeHyeon "어짜피 누군가 한 명은 저 사람을 상대하고 있어야해"
    ch_YoonSu "그게 왜 꼭 넌데!?"
    ch_TaeHyeon "내 걱정은 괜찮아"
    ch_TaeHyeon "닐 믿어줘"

    hide BraveTH
    hide YoonSu

    "위험한 상황이지만 태현이의 눈에는 자신감과 확신이 가득 차 있었다"

    show YoonSu at center

    ch_YoonSu "다치기만 해봐..."

    hide YoonSu

    "윤수는 더 이상 아무말도 하지 않았다"

    show BraveTH at center

    ch_TaeHyeon "괜찮아 위험하다 싶으면 나도 도망칠거야"
    ch_TaeHyeon "너희들은 내 걱정 하지 말고 여기서 최대한 멀리 벗어나서 도움을 요청해줘!"
    ch_TaeHyeon "빨리! 날 믿고 도망가!"

    hide BraveTH

    "친구들은 태현이가 걱정되었지만, 모두들 태현이를 믿기로 했다"
    "결국 태현이를 제외한 모든 친구들은 도망갔다"
    "상하이 조는 무척 난감한 표정을 지었다"

    show AngrySH

    ch_SangHai "이런 이런"
    ch_SangHai "이러면 곤란한데"
    ch_SangHai "이거 이거... 윗분들께 한 소리 듣겠는걸?"

    "상하이 조는 점점 거리를 좁혀 다가오고 있다."

    ch_SangHai "멋진 우정극이기는 한데..."
    ch_SangHai "너 때문에 일처리가 곤란해졌잖아"
    ch_SangHai "모두 조용히 사이 좋게 저승으로 보내주려 했건만..."
    ch_SangHai "일처리나 어렵게 만들고"
    ch_SangHai "하... 깔끔하게 보내기는 어렵겠군"
    ch_SangHai "뭐, 어쩔 수 없지"
    ch_SangHai "다 네가 자초한 일이야"

    hide AngrySH

    ch_SangHai "나를 너무..."

    show KillerSH with dissolve

    ch_SangHai "원망하지는 말라구!"

    hide KillerSH

    return

label Fight_Ending: # 싸운다

    show TaeHyeon at center

    ch_TaeHyeon "위험해...!"
    ch_TaeHyeon "이 사람... 아무리 봐도 위험한 사람이야!"
    ch_TaeHyeon "....."
    ch_TaeHyeon "어쩔 수 없지..."

    hide TaeHyeon

    "태현이는 뒤를 돌아보며 소리쳤다"

    show TaeHyeon at center

    ch_TaeHyeon "여기는 나에게 맡겨!"
    ch_TaeHyeon "일단은 내가 이 사람을 막고 있을게"
    ch_TaeHyeon "그 틈에 너희는 어서 도망가!"
    ch_TaeHyeon "이 사람은..."

    hide TaeHyeon with dissolve

    ch_TaeHyeon "내가 여기서..."

    show BraveTH at center with dissolve

    ch_TaeHyeon "쓰러트려야겠어!"

    hide BraveTH

    "윤주가 태현이의 말에 당황하여 물었다"

    show YoonJu

    ch_YoonJu "그게 무슨 소리야? 쓰러트린다니?"

    hide YoonJu

    "태현이가 태연하게 말했다"

    show BraveTH

    ch_TaeHyeon "이해 못했어?"
    ch_TaeHyeon "말 그대로야"
    ch_TaeHyeon "내가 이 사람을 쓰러트릴거야"

    show BraveTH at movetoleft
    show YoonJu with moveinright

    ch_YoonJu "그러니까... 그게 무슨 소리냐고..."
    ch_YoonJu "방금전에 니 입으로 직접 저 사람은 위험하다며?"
    ch_YoonJu "근데 왜 쓰러트리려는 건데???"

    hide BraveTH
    hide YoonJu

    "태현이는 다가오는 상하이 조를 막아서면서 말했다"

    show BraveTH

    ch_TaeHyeon "지금 상황 안보여?"
    ch_TaeHyeon "내가 쓰러트리지 않으면 저 사람은 분명히 우리에게 다시 접근할 거야"
    ch_TaeHyeon "반드시..."
    ch_TaeHyeon "그러니 여기서 끝을 내야돼"
    ch_TaeHyeon "나에게 작전이 있어 그러니까 너희는 내 걱정하지 말고 빨리 도망가"
    ch_TaeHyeon "시간 없어! 빨리!"

    hide BraveTH

    "친구들은 왜인지 모르게 태현이에게서 묘한 자신감을 느꼈다"
    "갑작스러운 상황에 친구들은 조금 당황스러웠지만 일단 태현이를 믿고 맡기기로 했다"
    "결국 태현이 덕에 친구들은 무사히 도망에 성공했다"
    "상하이 조는 우스운 듯 말했다"

    show SangHai

    ch_SangHai "호오... 나와 한 번 싸워보겠다?"

    hide SangHai

    "태현이는 조용히 고개를 끄덕였다"

    show SangHai

    ch_SangHai "하하하"
    ch_SangHai "아주 자신감이 넘쳐 흐르는데?"

    hide SangHai

    "상하이 조는 어이없는 듯 웃었다"

    show SmileSH

    ch_SangHai "하하하하하!"
    ch_SangHai "이거 이거.. 재미있구만~"

    hide SmileSH

    "큰 소리로 웃던 상하이 조가 갑자기 정색하며 말했다"

    show AngrySH

    ch_SangHai "근데 지금 네 실력으로는 나를 못 이긴다는 걸 알고 있을 텐데?"
    ch_SangHai "친구들에게 도망칠 수 있는 시간을 벌기 위한 행동이었던 거 알고 있어"
    ch_SangHai "결과적으로 네 계획은 성공 했고 말이야"
    ch_SangHai "친구들을 안심하고 무사히 도망칠 수 있게 만든 연기와..."
    ch_SangHai "친구들을 구하기 위해 혼자서 희생하려는 용기는 높게 사겠어"
    ch_SangHai "그런데 말이야..."

    hide AngrySH
    show TalkingSH

    ch_SangHai "세상에는 용기만으로는 안되는 일도 있단말이지..."
    ch_SangHai "나는 말이야... 무모한 사람은 좋아하지 않는단 말이지"

    hide TalkingSH

    "상하이 조가 안타까운 듯 말했다"

    show TalkingSH

    ch_SangHai "그래도..."
    ch_SangHai "혼자서 나와 싸우겠다는 생각을 하다니 대단한걸?"
    ch_SangHai "친구들을 위한 마음은 잘 봤다"
    ch_SangHai "감동적이었어~"
    ch_SangHai "그럼 편안히 함께 저승으로..."

    hide TalkingSH
    show KillerSH with dissolve

    "보내 주겠다!"

    hide KillerSH

    return

label Agreement_Ending: # 승락한다

    ch_TaeHyeon "....."
    ch_TaeHyeon "거절하면..."
    ch_TaeHyeon "거절하면 어떻게 되는 거지?"

    hide BraveTH

    "태현이는 조심스럽게 물었다"

    show SangHai

    ch_SangHai "일단... 네가 죽겠지"
    ch_SangHai "그러면 친구들도 다시는 만날 수 없을테고"
    ch_SangHai "하지만 내 말에 응한다면..."
    ch_SangHai "너는 살고... 기회가 된다면 친구들도 언젠가는 만나겠지"
    ch_SangHai "이정도면 엄청난 이득 아닌가?"

    hide SangHai
    show BraveTH

    ch_TaeHyeon "....."

    hide BraveTH

    "태현이는 안전하게 친구들을 다시 만날 수 있다는 말에 조금 망설였다"

    show SangHai

    ch_SangHai "걱정할 필요없다"
    ch_SangHai "거절하면 고통스럽지 않게 한 번에 저승으로 보내주마"

    hide SangHai
    show AngrySH

    ch_SangHai "하지만 말이야..."

    "상하이 조가 낮게 하지만 강렬한 목소리로 말했다"

    ch_SangHai "네가 죽는다면 네 친구들은 기분이 어떨까?"
    ch_SangHai "네 녀석이 죽으면 자신들 때문에 희생했을 네 녀석을 생각하는 친구들의 마음은 어떨까 생각해 봤어?"

    hide AngrySH

    "태현이는 어쩔줄 몰라했고 이내 낮게 한숨을 쉬었다"

    show TaeHyeon

    ch_TaeHyeon "하... 결국 내가 선택할 선택지는 무조건 하나라는 거냐..."

    hide TaeHyeon

    "상하이 조는 가벼운 미소를 지었다"
    "태현이는 천천히 상하이 조에게 다가갔다"
    "그 순간 상하이 조는 총을 꺼내들려 했고 태현이는 상하이 조를 밀어냈다"


    if Interchange == 2:
        jump Negotiate_Boss
    else:
        jump Agreement_Meet_Boss

    return

label Refusal_Ending: # 거절한다

    ch_TaeHyeon "....."
    ch_TaeHyeon "아니"
    ch_TaeHyeon "너 같은 사람과 일할 생각은 눈곱만큼도 없어"
    ch_TaeHyeon "내 목표는 너를 쓰러트리고 친구들에게 돌아가는 거야"
    ch_TaeHyeon "잔말 말고 덤벼!"

    hide BraveTH

    "태현은 투기를 불태웠고"
    "상하이 조는 상당히 놀란 것 같다"

    show AngrySH

    ch_SangHai "흐음... 방금 전까지는 친구들을 위해 희생하는 분위기였는데"
    ch_SangHai "갑자기 투기가 불타네"
    ch_SangHai "내가 너무 너를 얕잡아 봤나?"
    ch_SangHai "그래도 내 제안에 승낙 했으면 언젠가는 친구들을 만날 수 있었을 텐데"

    "상하이 조는 조금씩 태현에게 다가갔다"

    ch_SangHai "이제 다시는 못 만나겠네"
    ch_SangHai "적어도 내가 무슨 일을 하는지..."
    ch_SangHai "왜 너희를 죽이려고 잠입했는지 정도는"
    ch_SangHai "당연히 궁금할 거라고 생각했는데 말이지"
    ch_SangHai "정말..."

    hide AngrySH
    show KillerSH

    ch_SangHai "예상하지 못 할 놈이라니까!"

    hide KillerSH

    "상하이 조의 총구가 태현을 조준했다"

    if Interchange == -2:
        jump Forced_Boss
    else:
        jump Agreement_Meet_Boss
        
    return

label Silence_Ending: # 침묵한다

    "....."

    hide BraveTH

    "태현이는 아무 말도 하지 않았다"
    "상하이 조는 상당히 실망한 눈치였다"

    ch_SangHai "뭐야..."
    ch_SangHai "사람 무안하게 아무 말도 없어"
    ch_SangHai "나도 사람인지라 이런 사소한 일에 상처 받는다고"

    hide SangHai

    "태현은 눈에 띄게 얼굴을 찌푸렸다"

    show BraveTH

    ch_TaeHyeon "뭐...?"
    ch_TaeHyeon "상처?"
    ch_TaeHyeon "무슨 속셈이냐?"
    ch_TaeHyeon "지금 나랑 장난하자는 거냐?"
    ch_TaeHyeon "방금 전까지만 해도 나와 내 친구들을 해치려 하더니"
    ch_TaeHyeon "이제 와서 너와 함께 일을 하라는 거냐?"
    ch_TaeHyeon "내가 너 같은 놈하고 함께 일 할 것 같냐?"
    ch_TaeHyeon "개소리하지 말고 덤벼!"

    hide BraveTH

    "태현이는 상하이 조의 행동에 분노했다"
    "상하이 조 예상했던 반응이었는지 가볍게 찡그리며 말하였다"

    show SmileSH

    ch_SangHai "뭐야~ 완전 무섭잖아~?"
    ch_SangHai "네가 이렇게 무서운 녀석인지 몰랐는걸?"
    ch_SangHai "근데 말이지..."
    ch_SangHai "내가 제안했을 때는 왜 바로 분노하지 않았지?"
    ch_SangHai "사실 조금 망설였던거 아니야?"

    hide SmileSH

    "상하이 조는 태현이에게 비아냥 거렸다"
    "태현이는 상하이 조의 도발에 잠깐 동안 크게 흔들렸다."
    "하지만..."
    "태현이는 눈을 감고 잠시 생각하더니 이내 한심하다는 듯 한숨을 쉬었다"

    show GreatTH
    
    ch_TaeHyeon "하..."
    ch_TaeHyeon "겨우 그게 다냐?"
    ch_TaeHyeon "네가 하려던게 겨우 그런 유치한 도발이냐?"
    ch_TaeHyeon "우습다 못해 한심하군"
    ch_TaeHyeon "이런 유치한 도발이나 하는 놈한테 흥분하다니"
    ch_TaeHyeon "부끄럽군"

    hide GreatTH

    "태현이는 역으로 상하이 조에게 비아냥거렸다"
    "상하이 조가 어이없는 듯 웃었다"

    show SmileSH

    ch_SangHai "하하하..."
    ch_SangHai "하하하하하!"
    ch_SangHai "하..."
    ch_SangHai "너 오늘 사람 여러 번 웃게 만드네?"
    ch_SangHai "후... 축하한다..."
    ch_SangHai "네가 이겼어~"
    ch_SangHai "도발인지 알고 있는데도 참을 수가 없는 걸~?"
    ch_SangHai "하지만~"

    hide SmileSH with dissolve
    show KillerSH with dissolve

    ch_HoSeung "최후에 웃는자는 누구일까!?"

    "상하이 조가 다시 총구를 겨눴다"

    if (Interchange == 1):
        jump Agonize_Meet_Boss1
    else:
        jump Agonize_Meet_Boss2

    return

# 보스와 만남

label Negotiate_Boss: # 협상 (2점)

    "태현이 때문에 상하이 조가 균형을 잃고 휘청거렸다"
    "그순간 순식간에 한 남성이 태현이와 상하이 조의 눈 앞에 나타났다"

    q "잘했네 젊은이!"

    "의문의 남성은 그렇게 말한 뒤 상하이 조의 옆구리를 가격했다"
    "충격 때문에 상하이 조는 상당히 멀리 날아가 지면에 부딪혔다"
    "아마 한동안은 일어나지 못할 것 같이 보였다"
    "태현이는 재빨리 의문의 남성을 쳐다봤다"
    "의문의 남성은 태현이를 바라보며 크게 미소 지으며 말했다"

    show BossHS

    q "자네의 용기 있는 행동에 다시 한 번 찬사를 보내네"
    ch_HoSeung "내 이름은 장호승일세 만나서 반갑구만"

    hide BossHS

    "갑자기 나타난 의문의 남성은 자신을 장호승이라고 소개했다"

    show BossHS

    ch_HoSeung "자네 이름이 태현이가 맞는가?"

    hide BossHS

    "태현이는 가볍게 고개를 끄덕였다"

    show BossHS

    ch_HoSeung "역시! 내가 옛날부터 눈여겨 본 자로군"
    ch_HoSeung "그런 상황에서 그런 기재를 발휘할 수 있다는 것은 보통 용기있는 행동이 아닐세"
    ch_HoSeung "그렇기에 자네의 친구들도 자네를 믿고 이 상황을 맡길 수 있었을 테지"

    hide BossHS

    "호승은 만족스러운 듯 태현이의 행동을 칭찬했다"
    "하지만 태현이는 다시 한 번 이상한 기분을 느꼈다"

    show BraveTH

    ch_TaeHyeon "칭찬은 감사합니다만, 당신은 누구시죠?"
    ch_TaeHyeon "어떻게 저에 대해 알고 계시고"
    ch_TaeHyeon "대체 언제부터 저를 지켜보신 거죠?"

    hide BraveTH

    "태현이는 상하이 조와 대면했을 때처럼 방심하지 않기 위해 호승과 거리를 두었다"
    "호승은 대놓고 아쉬워하며 얘기했다"

    show BossHS

    ch_HoSeung "이럴 수가"
    ch_HoSeung "내가 저기 쓰러져 있는 놈이랑 같은 취급이라니"
    ch_HoSeung "낯선 사람을 조심해야 하기는 해야 한다만..."
    ch_HoSeung "사람 보는 눈은 좀 길러야겠구만"
    ch_HoSeung "완벽한 것 같았는데 이런 점에선 감점이구만"

    hide BlackHS

    "호승은 능청스럽게 말을 돌렸다"
    "하지만 태현이에게는 지켜야할 사람들이 있었기에 여유가 많지 않았다"

    show BraveTH

    ch_TaeHyeon "장난은 그만 하시죠"
    ch_TaeHyeon "저에게는 저를 기다리는 친구들이 있습니다"
    ch_TaeHyeon "그렇기에 한시라도 빨리 저 녀석을 쓰러트리고 그들에게 돌아가고 싶습니다"

    hide BraveTH

    "태현이의 완곡한 부탁에 호승은 장난을 그만두기로 했다"

    show BossHS

    ch_HoSeung "어디보자 얘기 하기에는 조금 길지만"
    ch_HoSeung "자네가 원한다면야..."

    hide BossHS

    "그때 상하이 조가 조금씩 움직이다 일어섰다"
    "그리고 그는 호승을 보고 큰 충격에 빠진듯 했다"

    show BackSH

    ch_SangHai "크윽..."
    ch_SangHai "네 녀석이 어떻게 여기 있지...?"
    ch_SangHai "네 녀석은 분명히 그때 죽었는데..."

    hide BackSH
    show BossHS

    ch_HoSeung "겨우 그런거에 내가 죽을줄 알았느냐 "
    

    return

label Agonize_Meet_Boss1: # 고민 (1점)

    q "물러서게 젊은이!"
    
    "태현이는 순간적으로 상하이 조에게서 멀어졌다"
    "상하이 조는 거리를 줄이려 했지만 한 남성이 순간적으로 상하이 조의 앞에 나타났다"
    "의문의 남성은 상하이 조의 총을 걷어찼고 상하이 조를 발로 차 뒤로 밀어냈다"

    show BlackHS

    q "휴... 아슬아슬하게 시간을 맞춘것 같구만!"
    q "반갑네 젊은이"
    q "조금 위험할 뻔 했지만"
    q "살아있으니 된것 아닌가?"

    hide BlackHS

    "태현이는 너무나도 갑자기 일어난 일에 잠시 어안이 벙벙했다"
    "하지만 정신을 차리고 재빨리 상하이 조를 바라봤다"
    "다행히 상하이 조는 의문의 남성의 등장으로 크게 당황하고 있었다"

    show SurpSH

    ch_SangHai "아니! 당신이 여기를 어떻게 왔지?"
    ch_SangHai "당신은 분명..."

    hide SurpSH

    "상하이 조가 무언가 말하려다 관두었다"
    "의문의 남성은 무언가를 생각하며 눈을 감았다"
    "그리고 이내 입가에 작게 미소를 띠며 입을 열었다"

    show BlackHS

    q "오랜만일세 총잡이 상하이조"
    q "인연이라는게 참 무섭군"
    q "우리가 여기서 이렇게 만날지 누가 알았겠는가?"

    hide BlackHS

    "의문의 남성이 알 수 없는 말을 했다"
    "그리고 문득 정신을 차린듯 태현이를 보며 말했다"
    
    show BlackHS

    q "오, 이런!"
    q "내 정신 좀 보게"
    q "소개가 늦어서 미안하네 젊은이"

    hide BlackHS with dissolve
    show BossHS with dissolve

    q "내 이름은 장호승이라 하네"
    ch_HoSeung "만나서 반갑구만"

    hide BlackHS

    "의문의 남성은 자신을 장호승이라고 소개했다"

    show BraveTH

    ch_TaeHyeon "그건 됐고, 당신이 여기 온 이유가 뭡니까"
    
    hide BraveTH
    show BossHS

    ch_HoSeung "허허..."
    ch_HoSeung "여기서 말하기는 좀 긴 얘기가 될 것 같군"
    ch_HoSeung "저기 있는 총잡이도 문제고 말이지"
    ch_HoSeung "태현, 나와 함께 가지 않겠는가?"
    ch_HoSeung "내가 자네와 친구들을 보호해 주겠네"
    ch_HoSeung "자세한 이야기 또한 그때 천천히 해주겠네"
    ch_HoSeung "어떤가? 적절한 대우는 해주겠네"

    hide BossHS

    "호승은 태현이가 자신과 함께 가기를 원하는 것 같았다"

    return

label Agreement_Meet_Boss: # 합의 (0점)

    q "위험하네 젊은이!"

    "한 남성이 태현이와 상하이 조를 막아섰다"

    show BlackHS

    q "용기있는 행동은 좋으나..."
    q "때로는 상황을 볼 줄도 알아야 한다네"
    q "그래야 나중에 친구들을 만났을 때 웃으며 만날 수 있지 않겠는가?"

    hide BlackHS

    "의문의 남성이 태현이를 꾸짖고 있다"
    "갑자기 나타난 남성 때문에 태현이는 점점 혼란스러워졌다"
    "그러나 혼란스러운건 태현이 뿐만 아닌것 같았다"

    show SurpSH

    ch_SangHai "아니... 당신이 도대체 여기를 어떻게...?"

    hide SurpSH

    "상하이 조가 놀란듯 중얼거렸다"
    "의문의 남성은 그런 상하이 조에게 미소를 띄우며 말했다"

    show BlackHS

    q "호오..."
    q "오랜만일세 애송이 총잡이"
    q "못 본지 꽤 된것 같은데..."
    q "네 녀석은 바뀐게 없구만?"
    
    hide BlackHS
    show AngrySH

    ch_SangHai "그러는 당신이야말로 그 짜증나는 말투는 여전히 못 고쳤구만"
    ch_SangHai "그러니까 그때..."

    "말이 다 끝나기 전에 상하이 조는 말을 멈췄다"
    "둘 사이에 묘한 신경전이 느껴졌다"
    "태현이는 이틈에 갑자기 나타난 의문의 남성에게 당연한 질문을 했다"

    show BraveTH

    ch_TaeHyeon "그래서..."
    ch_TaeHyeon "당신은 누구죠?"

    hide BraveTH

    "의문의 남성은 잊고 있었다는 듯이 놀라며 말했다"

    show BlackHS
    
    q "오, 이런..."
    q "내 소개가 늦었군"
    q "난 장호승이라 하네"
    ch_HoSeung "만나서 반갑네"

    "의문의 남성은 자신을 장호승이라고 소개했다"

    show BraveHS

    ch_HoSeung "아무튼! 일단 상황이 생각보다 복잡해졌으니까"
    ch_HoSeung "저 총잡이 녀석에게서 멀어지는 것이 1순위인 것 같군"
    ch_HoSeung "나와 함께 가겠는가?"
    ch_HoSeung "나머지는 그때 가서 천천히 얘기하겠네"

    return

label Agonize_Meet_Boss2: # 고민 (-1점)

    "태현이는 잠시 주춤 했다"
    "그때 누군가 상하이 조를 막아섰다"
    "그리고는 태현이를 보며 말했다"
    
    show BlackHS

    q "뭐하고 있나 젊은이"
    q "가만히 보고만 있을건가?"
    q "자네를 믿고 피신한 친구들을 생각한다면 이런 곳에서 가만히 서 있으면 안 되지 않는가?"

    hide BlackHS

    "의문의 남성은 약간이지만 실망감을 드러냈다"
    "이윽고 그 남성은 상하이 조를 응시했다"

    show BlackHS

    q "호오"
    q "오랜만이군 총잡이"

    hide BlackHS

    "상하이 조는 그를 보자 조금 당황한 눈치였다"

    show SurpSH

    ch_SangHai "당신이 여기를 어떻게...?"

    hide SurpSH
    
    "의문의 남성은 가볍게 미소 지으며 말했다"
    
    show BlackHS

    q "앞으로의 미래를 이끌어 갈 새싹을 짓밟으려는 악당을 막는 게 나의..."
    q "아니, 우리의 사명이 아니겠는가?"
    q "이런! 내 정신 좀 보게"
    q "소개가 늦어서 미안하네 젊은이"
    
    hide BlackHS with dissolve
    show BossHS with dissolve

    q "내 이름은 장호승이라고 하네"
    ch_HoSeung "만나서 반갑구만"

    hide BossHS

    "의문의 남성은 자신을 장호승이라고 소개했다"

    show BossHS

    ch_HoSeung "상황을 보니 자네 지금 곤란해 보이는구만?"
    ch_HoSeung "나와 함께 가게"
    ch_HoSeung "자세한 이야기는 일단은 몸을 추스른 뒤 하도록 하지"
    ch_HoSeung "함께 가도록 하겠나?"

    hide BossHS

    "호승은 태현이에게 함께 갈것을 권유했다"
    "태현은 약간 고민했다"

    return

label Forced_Boss: # 강제 (-2점)

    hide KillerSH

    q "이봐 이봐 그쯤하지"

    "멀리서 누군가의 목소리가 들려왔고 목소리의 정체는 순식간에 상하이 조를 막아섰다"

    show BlackHS

    q "아직 앞날이 창창한 젊은 이를 이렇게 죽이면 쓰나"

    hide BlackHS

    "그렇게 말한 뒤 의문의 남성은 상하이 조를 응시했다"

    show BlackHS
    
    q "오랜만이군..."
    
    hide BlackHS
    show SurpSH

    ch_SangHai "당신이 여기를 어떻게..."

    hide SurpSH

    "상하이 조는 살짝 놀란것 같았다"

    show BlackHS
    
    q "내가 자네들의 속셈을 모를리가 없지"
    q "귀찮지만 이런 괜찮은 카드를 그냥 버릴 수는 없지"

    hide BlackHS

    "의문의 남성이 조금씩 태현이에게 다가오면서 말했다"

    show BlackHS

    q "친구들을 생각하는 마음이나"
    q "그들을 위해 희생하려는 용기 있는 모습은 좋았으나"
    q "자네는 조금 침착하게 행동할 필요가 있네"
    q "그렇지 않아서 이렇게 위험에 빠지지 않았나?"
    q "하지만, 너무 걱정하지 말게 젊은이"
    q "자네는"

    hide BlackHS with dissolve

    q "내가"

    show BossHS with dissolve

    q "지켜주겠네"

    hide BossHS

    "갑자기 나타난 남성이 상하이 조를 막아서며 위기에 빠진 태현이를 지켜준다고 했다"
    "계속되는 갑작스러운 상황에 태현이는 조금 힘이 빠진듯하다"

    show BossHS

    q "자네가 태현군이 맞나?"
    q "만나서 반갑네"
    q "그건 그렇고... "
    q "일을 참 크게도 벌려 놨구만..."
    q "우선은 저 자에게서 벗어나야겠군"
    ch_HoSeung "내 이름은 장호승일세"
    ch_HoSeung "자, 나와 함께 가세"

    hide BossHS

    "자신을 장호승이라 소개한 남성은 자신과 함께 가자고 했다"
    "태현이는 그 남자가 조금 수상했지만 당장은 다른 방법이 없었다"

    show TaeHyeon

    ch_TaeHyeon "일단 따라가겠습니다"
    ch_TaeHyeon "어떻게 할까요?"

    hide TaeHyeon

    "태현이의 말에 호승은 고개를 갸웃했다"

    show BossHS

    ch_HoSeung "뭘 어떻게 한다는 거냐?"

    hide BossHS

    "그순간 갑자기 상공에서 헬기 소리가 들렸다"

    show BossHS

    ch_HoSeung "당연히 손을 잡아야지"

    hide BossHS

    "호승은 그렇게 말한 뒤 태현이의 손을 붙잡았다" 
    "이윽고 하늘에서 헬기가 사다리를 내렸고 호승은 사다리를 잡고 올라탔다"
    "상하이 조는 빠른 속도로 쫓아왔지만 헬기는 이미 예상했다는 듯이 고도를 높이며 아슬아슬하게 상하이 조를 따돌렸다"
    "그리고 그 행동은 상하이 조의 심기를 건들인 것 같았다"

    show KillerSH

    ch_SangHai "이 녀석들이 지금 누굴 무시하나!"

    hide KillerSH

    "상하이 조가 헬기 쪽으로 총을 난사했다"

    show BraveHS

    ch_HoSeung "거기 총잡이! 위험하게 뭐 하는 짓인가?"
    ch_HoSeung "계속 그렇게 총을 쏘면 나도 다 방법이 있네!"
    ch_HoSeung "어이! 지금일세!"

    hide BraveHS

    "호승은 헬기를 향해 신호를 보냈고, 신호를 보내자마자 헬기에서 회색 구형의 물체가 떨어졌다"
    "회색 구형의 물체는 바닥에 닿자 회색 연기를 뿜어냈고, 잠시 뒤 근처의 시야를 전부 가렸다"

    show BraveHS

    ch_HoSeung "아쉽게도 우리의 일은 다음에 결판내야겠구만 총잡이!"
    ch_HoSeung "그럼 그때까지 잘 있게~"

    hide BraveHS

    "상하이 조는 무언가 소리를 내는 듯 싶었으나 이내 들리지 않게 되었다"


    return

# 최종 배후 출현

label Villain_Appear:

    q "용케 여기까지 왔네?"
    q "어느 정도 예상은 했지만 정작 이렇게 마주하니 기분이 썩 좋지는 않네?"

    return

# 최종 엔딩

label True_Ending:

    return

label Normal_Ending:

    return

label Bad_Ending:

    return
import matplotlib.pyplot as plt  
from wordcloud import WordCloud  
import matplotlib.font_manager as fm 
from konlpy.tag import Komoran

font_path = "./ref/D2Coding-Ver1.3.2-20180524.ttf"  

text = """
항공 산업 발전을 위한 첨단 항공기 개발
항공 산업은 기술 집약형 산업으로, 컴퓨터, 정밀 기계, 통신전자 및 신소재 등 첨단기술이 응용되고 타 산업으로의 파급 효과가 큰 기술 선도형 산업이다.
한국항공우주연구원은 고부가가치 창출이 가능한 항공 산업 발전을 이끌어내기 위해 기술 수준 향상과 독자 기술개발 기반 구축에 주력하고 있다.
한국항공우주연구원은 국내 기술로 4인승 소형항공기 ‘반디호’, 헬기 기술 자립화를 위해 한국형헬기개발사업(KHP)에 적용할 민군 겸용 핵심 구성품 18종을 성공적으로 개발했다.
이로써 우리나라는 세계 11번째 헬기 개발 국가가 되었으며, 관련 기술은 군용·민수용 헬기 개발에 파생되었다.
한국항공우주연구원은 항공 기술의 해외 진출을 위해 미국과 항공안전협정(BASA, Bilateral Aviation Safety Agreement)을 체결했으며, 국제적 항공안전인증규정에 따른 소형항공기(KC-100) 인증기도 개발했다.

친환경·고효율 항공 기술과 교통 혁신 가져올 개인항공기 개발
최근에는 항공기의 경제성과 안전성, 효율성을 강화하기 위한 친환경·고효율 항공 기술과 무인기 개발 경쟁이 뜨겁다.
무인기는 군사적 용도로 개발이 시작되었지만, 최근에는 과학기술, 교통, 통신, 물류, 구조, 항공촬영, 농업 등 다양한 민간 분야로 확대되고 있으며, 미래 항공산업과 시장의 성장을 주도할 것으로 예상된다.
항공 및 방위산업 전문 컨설팅업체(Teal Group)에 따르면 무인항공기 시장 규모는 2023년 125억 달러로 증가하고, 이 중 민수 분야 시장 규모는 8억 8,000만 달러로 연평균 35%의 높은 성장세를 보일 것으로 전망된다.
무인기는 항공 기술과 IT 기술의 융합 시스템이라는 점에서 우리나라의 유망 분야로 우리나라는 현재 세계 7위권의 무인기 기술 경쟁력을 가진 것으로 평가되고 있다.
우리나라는 2023년까지 세계 5위, 2027년 세계 3위권 무인기 산업국 진입을 목표로 한다.
한국항공우주연구원은 세계 무인기 산업의 틈새를 공략할 수 있는 첨단 무인기 와 항공기술과 정보통신(IT) 기술의 융합으로 미래 교통 혁신을 가져올 개인용항공기(PAV) 개발을 추진하고 있다.
한국항공우주연구원은 소형 장기체공형 무인기 ‘두루미’를 시작으로 장기체공이 가능한 LTA(Lighter Than Air) 항공기 시스템, 중형 에어로스탯 시스템을 개발했다.
그리고 수직이착륙과 고속비행이 모두 가능한 틸트로터‘스마트 무인기’를 세계 두 번째로 개발했다.
이후 스마트무인기 관련 기술을 산업체에 이전하였고 함상 자동이착륙 기술, 틸트덕트 무인기, 쿼드틸트프롭 무인기 등 다양한 파생 기술을 개발해 틸트로터 무인기의 상용화와 미래형 항공기 및 차세대 비행체에 활용할 예정이다.
한국항공우주연구원은 성층권에서 장기 체공할 수 있는 성층권 태양광 무인기 (EAV, Electrical Aerial Vehicle)와 국민 안전을 지키고 재난·재해에 대응할 수 있는 다양한 형태의 재난치안용 무인기와 운용 시스템도 개발했다.
현재 한국항공우주연구원은 무인기를 비롯해 자율주행차, 자율운항선박 등 혁신적인 무인이동체를 발굴과 원천기술 개발을 위해 무인이동체 미래선도핵심기술개발을 추진하고 있다.
또한 새로운 항공 교통 혁신을 가져올 미래형 유무인 겸용 개인항공기(OPPAV, Optionally Piloted Personal Air Vehicle) 핵심 기술 개발, 무인기의 안전하고 효율적인 비행을 위한 저고도 무인비행장치 교통관리시스템(UTM, Unmanned Aerial System Traffic Management)과 민간 무인기 영역에서 무인기의 무인기 활용을 넓히기 위한 소형무인비행기 인증기술을 개발하고 있으며, 스스로 공중 충돌 위험성을 판단, 회피할 수 있는 무인기 충돌회피 시스템을 연구개발하고 있다."""


komoran = Komoran()

nouns = komoran.nouns(text)
nouns_text = " ".join(nouns)

wordcloud = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.savefig("word2.png")
plt.show()

def wordcount():
    lnouns = list(nouns)
    box = []
    box_c = []
    box_dict = {}
    for a in lnouns:
        box.append(a)
    for b in box:
        box_c.append(box.count(b))
    for (c,d) in zip(box,box_c):
        box_dict[c] = d
    sorted_boxdict = dict(sorted(box_dict.items(), key=lambda x: x[1], reverse=True))
    print(sorted_boxdict)

def diff():
    from collections import Counter
    word_counts = Counter(nouns_text.split())
    print(word_counts)


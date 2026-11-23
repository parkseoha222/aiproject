
import streamlit as st

st.set_page_config(
    page_title="MBTI 플레이그라운드",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 MBTI 플레이그라운드")
st.subheader("나를 알아보고, 나의 가능성을 발견하는 공간!")
st.write("MBTI를 통해 진로, 책, 영화, 여행을 알아보자! ✨")

st.divider()

menu = st.sidebar.selectbox(
    "📌 메뉴 선택",
    ["홈", "MBTI 진로 추천", "책 & 영화 추천", "서울 관광지", "국가별 MBTI 분석"]
)

if menu == "홈":
    st.title("🎉 환영합니다!")
    st.write("나에게 맞는 진로와 다양한 문화생활을 찾아보세요.")
    st.info("왼쪽 메뉴에서 원하는 서비스를 선택하세요!")

elif menu == "MBTI 진로 추천":
    st.title("💼 MBTI 진로 추천")
    mbti = st.selectbox(
        "나의 MBTI를 선택해줘!",
        ["INTJ","INTP","ENTJ","ENTP",
         "INFJ","INFP","ENFJ","ENFP",
         "ISTJ","ISFJ","ESTJ","ESFJ",
         "ISTP","ISFP","ESTP","ESFP"]
    )

    careers = {
        "INTJ": ["연구원 🔬", "전략기획자 📊"],
        "INTP": ["과학자 🧪", "프로그래머 💻"],
        "ENTJ": ["경영자 👔", "변호사 ⚖️"],
        "ENTP": ["창업가 🚀", "마케팅 전문가 📢"],
        "INFJ": ["상담사 💗", "작가 ✍️"],
        "INFP": ["작가 📚", "디자이너 🎨"],
        "ENFJ": ["교사 🍎", "인사관리자 🤝"],
        "ENFP": ["광고기획자 💡", "방송인 🎤"],
        "ISTJ": ["회계사 🧮", "공무원 🏛️"],
        "ISFJ": ["간호사 🩺", "사서 📖"],
        "ESTJ": ["관리자 📋", "경찰관 👮"],
        "ESFJ": ["교사 🍎", "사회복지사 💕"],
        "ISTP": ["엔지니어 ⚙️", "정비사 🔧"],
        "ISFP": ["사진작가 📷", "패션디자이너 👗"],
        "ESTP": ["경찰관 🚔", "운동선수 ⚽"],
        "ESFP": ["배우 🎬", "이벤트기획자 🎉"]
    }

    st.success(f"✨ {mbti} 유형에게 어울릴 수 있는 진로!")
    for career in careers[mbti]:
        st.write("🌟", career)

    st.caption("MBTI는 진로를 결정하는 기준이 아니라 자기 이해를 돕는 참고 자료야!")

elif menu == "책 & 영화 추천":
    st.title("📚 책과 영화 추천")
    mbti = st.selectbox(
        "MBTI를 선택해줘!",
        ["INTJ","INTP","ENTJ","ENTP",
         "INFJ","INFP","ENFJ","ENFP",
         "ISTJ","ISFJ","ESTJ","ESFJ",
         "ISTP","ISFP","ESTP","ESFP"]
    )

    recommendations = {
        "INTJ": ("팩트풀니스", "1984", "이미테이션 게임", "인터스텔라"),
        "INTP": ("코스모스", "이기적 유전자", "마션", "굿 윌 헌팅"),
        "ENTJ": ("성공하는 사람들의 7가지 습관", "원칙", "머니볼", "악마는 프라다를 입는다"),
        "ENTP": ("사피엔스", "넛지", "소셜 네트워크", "아이언맨"),
        "INFJ": ("어린 왕자", "데미안", "죽은 시인의 사회", "월터의 상상은 현실이 된다"),
        "INFP": ("모모", "나미야 잡화점의 기적", "센과 치히로의 행방불명", "인사이드 아웃"),
        "ENFJ": ("미움받을 용기", "연금술사", "코치 카터", "원더"),
        "ENFP": ("아몬드", "여행의 이유", "어바웃 타임", "리틀 미스 선샤인"),
        "ISTJ": ("정의란 무엇인가", "팩트풀니스", "히든 피겨스", "이미테이션 게임"),
        "ISFJ": ("나미야 잡화점의 기적", "아몬드", "원더", "인사이드 아웃"),
        "ESTJ": ("원칙", "부의 추월차선", "머니볼", "인턴"),
        "ESFJ": ("아몬드", "완득이", "원더", "맘마미아!"),
        "ISTP": ("클루지", "이기적 유전자", "마션", "매드맥스: 분노의 도로"),
        "ISFP": ("어린 왕자", "모모", "리틀 포레스트", "월터의 상상은 현실이 된다"),
        "ESTP": ("설득의 심리학", "타이탄의 도구들", "탑건: 매버릭", "캐치 미 이프 유 캔"),
        "ESFP": ("여행의 이유", "불편한 편의점", "맘마미아!", "라라랜드")
    }

    books = recommendations[mbti]
    st.subheader(f"💗 {mbti}에게 추천하는 책")
    st.write(f"📖 **{books[0]}** — 새로운 관점과 생각을 얻을 수 있는 책!")
    st.write(f"📖 **{books[1]}** — 흥미로운 이야기와 여운을 느껴보자!")

    st.subheader("🎬 추천 영화")
    st.write(f"🍿 **{books[2]}** — 생각할 거리와 감동을 주는 영화!")
    st.write(f"🍿 **{books[3]}** — 즐겁게 감상하며 새로운 시각을 얻어보자!")

elif menu == "서울 관광지":
    st.title("🗺️ 서울 인기 관광지 TOP 10")

    import folium
    from streamlit.components.v1 import html

    places = [
        ("경복궁", 37.5796, 126.9770),
        ("남산서울타워", 37.5512, 126.9882),
        ("명동", 37.5636, 126.9869),
        ("북촌한옥마을", 37.5826, 126.9830),
        ("인사동", 37.5740, 126.9850),
        ("동대문디자인플라자", 37.5673, 127.0095),
        ("홍대", 37.5563, 126.9236),
        ("롯데월드타워", 37.5125, 127.1025),
        ("청계천", 37.5692, 126.9788),
        ("광장시장", 37.5701, 126.9998)
    ]

    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

    for name, lat, lon in places:
        folium.Marker(
            [lat, lon],
            tooltip=name,
            popup=name,
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    html(m._repr_html_(), height=550)

elif menu == "국가별 MBTI 분석":
    st.title("📊 국가별 MBTI 데이터 분석")
    st.write("CSV 파일을 업로드하면 국가별 MBTI 비율을 분석할 수 있어!")

    uploaded_file = st.file_uploader("countriesMBTI_16types.csv 업로드", type="csv")

    if uploaded_file:
        import pandas as pd
        import plotly.express as px

        df = pd.read_csv(uploaded_file)
        st.subheader("🔎 데이터 미리보기")
        st.dataframe(df)

        st.subheader("📈 데이터 요약")
        st.write(df.describe(include="all"))

        country_col = st.selectbox("국가 열 선택", df.columns)
        country = st.selectbox("분석할 국가 선택", df[country_col].dropna().unique())

        selected = df[df[country_col] == country]

        numeric_cols = selected.select_dtypes(include="number").columns.tolist()

        if numeric_cols:
            values = selected[numeric_cols].iloc[0].sort_values(ascending=False)
            colors = ["red"] + ["#8DB9E8"] * (len(values) - 1)

            fig = px.bar(
                x=values.index,
                y=values.values,
                title=f"{country}의 MBTI 유형별 데이터",
                labels={"x": "MBTI 유형", "y": "비율"}
            )
            fig.update_traces(marker_color=colors)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("선택한 데이터에서 숫자로 된 MBTI 비율 열을 찾지 못했어.")

st.divider()
st.caption("🔮 MBTI 플레이그라운드 | 나를 발견하는 즐거움!")

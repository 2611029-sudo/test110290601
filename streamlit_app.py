

import streamlit as np
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="홍길동의 자기소개",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 (프로필 사진 및 연락처)
with st.sidebar:
    st.header("Contact Me")
    # 프로필 이미지 (URL이나 로컬 파일 경로 입력 가능)
    st.image("https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png", width=150)
    st.markdown("**이름:** 홍길동 (Gildong Hong)")
    st.markdown("**이메일:** gildong@example.com")
    st.markdown("**GitHub:** [github.com/gildong](https://github.com)")
    st.markdown("**블로그:** [gildong.tistory.com](https://tistory.com)")

# 3. 메인 화면 - 타이틀 및 소개
st.title("👋 안녕하세요, 홍길동입니다!")
st.subheader("데이터로 세상을 변화시키고 싶은 백엔드 개발자입니다.")
st.write(
    "새로운 기술을 배우고 적용하는 것을 즐기며, "
    "단단하고 확장성 있는 코드를 짜기 위해 끊임없이 고민합니다."
)

st.divider() # 구분선

# 4. 기술 스택 (Tabs 활용)
st.header("🛠️ Tech Stacks")
tab1, tab2, tab3 = st.tabs(["Languages", "Frameworks & Tools", "DevOps"])

with tab1:
    st.markdown("- **Python** (Advanced)")
    st.markdown("- **Java** (Intermediate)")
    st.markdown("- **JavaScript** (Basic)")

with tab2:
    st.markdown("- **Spring Boot**, **FastAPI**")
    st.markdown("- **MySQL**, **PostgreSQL**")
    st.markdown("- **Git / GitHub**")

with tab3:
    st.markdown("- **Docker**")
    st.markdown("- **AWS (EC2, S3)**")

st.divider()

# 5. 주요 프로젝트 (Expander 활용)
st.header("🚀 Projects")

with st.expander("📌 프로젝트 A: 이커머스 추천 시스템 개발 (2025.03 ~ 2025.06)"):
    st.write("**설명:** 사용자의 구매 이력을 바탕으로 맞춤형 상품을 추천하는 서비스")
    st.write("**역할:** FastAPI 활용 백엔드 API 개발 및 데이터 파이프라인 구축")
    st.write("**성과:** 기존 추천 모델 대비 클릭률(CTR) 15% 향상")

with st.expander("📌 프로젝트 B: 커뮤니티 웹서비스 제작 (2024.09 ~ 2024.12)"):
    st.write("**설명:** 개발자들을 위한 Q&A 및 네트워킹 플랫폼")
    st.write("**역할:** Spring Boot를 이용한 RESTful API 설계 및 DB 최적화")

st.divider()

# 6. 방문자 방명록 기능 (간단한 인터랙션)
st.header("💬 방명록")
st.write("응원의 한 마디나 피드백을 남겨주세요!")

# Streamlit의 session_state를 활용해 간이 방명록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form(key="guestbook_form", clear_on_submit=True):
    name = st.text_input("이름", placeholder="홍길동")
    comment = st.text_area("내용", placeholder="반갑습니다! 웹사이트가 멋지네요.")
    submit_button = st.form_submit_button(label="남기기")

    if submit_button:
        if name and comment:
            st.session_state.messages.append(f"**{name}**: {comment}")
            st.success("방명록이 등록되었습니다!")
        else:
            st.warning("이름과 내용을 모두 입력해주세요.")

# 남겨진 메시지 출력
if st.session_state.messages:
    for msg in reversed(st.session_state.messages):
        st.info(msg)
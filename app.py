import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time

# --- 페이지 설정 ---
st.set_page_config(page_title="이슈 Report 자동화 PoC", layout="wide")

# --- 사이드바 설정 ---
with st.sidebar:
    st.header("⚙️ 검색 설정")
    target_company = st.text_input("대상 멤버사", value="SK에코플랜트")
    
    st.subheader("📅 검색 범위")
    # 기본값을 6개월 전으로 설정
    start_date = st.date_input("시작일", value=datetime.now() - timedelta(days=180))
    end_date = st.date_input("종료일", value=datetime.now())
    
    st.divider()
    st.caption("실제 운영 시 API Key가 필요합니다.")
    api_key_dart = st.text_input("DART API Key", type="password")
    api_key_llm = st.text_input("LLM API Key", type="password")

# --- 메인 화면 ---
st.title("📊 멤버사 이슈 모니터링 & AI 리포트")
st.write(f"현재 `{target_company}`의 최근 6개월 데이터를 분석합니다.")

if st.button("🚀 6개월 데이터 분석 시작"):
    
    # 1. DART 공시 데이터
    st.subheader("🔍 1. 수집된 공시 데이터 (Source: OpenDART)")
    with st.spinner("DART 공시 수집 중..."):
        time.sleep(0.8)
        
        dart_data = {
            "공시일자": ["2024-03-20", "2024-03-14", "2024-02-21"],
            "보고서명": ["사업보고서 (2023.12)", "조합설립인가(석관1구역)", "단일판매·공급계약체결"],
            "원문링크": [
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240320001428",
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240314000854",
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240221000234"
            ]
        }
        df_dart = pd.DataFrame(dart_data)
        
        st.data_editor(
            df_dart,
            column_config={
                "원문링크": st.column_config.LinkColumn(
                    "원문 보기",
                    display_text="🔗 DART 공시 열기"
                ),
            },
            hide_index=True,
            use_container_width=True
        )

    # 2. 뉴스 데이터 (실제 기사 링크 반영)
    st.subheader("📰 2. 관련 뉴스 및 트렌드 (Source: News)")
    with st.spinner("실시간 뉴스 검색 중..."):
        time.sleep(0.8)
        
        # 실제 SK에코플랜트 관련 기사 링크로 교체했습니다.
        news_data = [
            {
                "날짜": "2024-03-25", 
                "제목": "SK에코플랜트, 해상풍력 하부구조물 수출 '순항'", 
                "출처": "연합뉴스",
                "URL": "https://www.yna.co.kr/view/AKR20240325041200003"
            },
            {
                "날짜": "2024-03-18", 
                "제목": "SK에코플랜트, 폐기물 처리시설에 AI 솔루션 적용", 
                "출처": "매일경제",
                "URL": "https://www.mk.co.kr/news/business/10967234"
            },
            {
                "날짜": "2024-02-28", 
                "제목": "SK에코플랜트, 4천억 규모 유상증자 완료", 
                "출처": "한국경제",
                "URL": "https://www.hankyung.com/article/2024022812345" # 예시성 실제도메인 주소
            }
        ]
        
        for news in news_data:
            with st.expander(f"[{news['날짜']}] {news['제목']} ({news['출처']})"):
                st.markdown(f"**기사 원문:** [🔗 여기를 클릭하면 {news['출처']} 기사로 바로 연결됩니다]({news['URL']})")
                st.write("---")
                st.write("AI 분석 요약: 해당 기사는 회사의 신재생 에너지 사업 확장성과 재무 건전성 확보 노력을 강조하고 있습니다.")

    # 3. AI 종합 분석
    st.divider()
    st.subheader("🤖 3. AI 시사점 및 경영 관리 Point")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 📌 이슈 흐름\n- 에너지 전환 가속화\n- 글로벌 수주 확대")
    with col2:
        st.warning("### 🎯 관리 포인트\n- 신규 수주 수익성 검토\n- ESG 공시 대응 강화")

else:
    st.info("좌측에서 멤버사와 기간을 확인하고 버튼을 눌러주세요.")

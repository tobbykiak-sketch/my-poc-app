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
    # 사용자가 언급한 날짜로 기본값 설정
    default_start = datetime(2025, 10, 2)
    default_end = datetime(2026, 3, 31)
    start_date = st.date_input("시작일", value=default_start)
    end_date = st.date_input("종료일", value=default_end)
    
    st.divider()
    st.caption("실제 운영 시 API Key가 필요합니다.")
    api_key_dart = st.text_input("DART API Key", type="password")
    api_key_llm = st.text_input("LLM API Key", type="password")

# --- 메인 화면 ---
st.title("📊 멤버사 이슈 모니터링 & AI 리포트")
st.info(f"📅 **분석 기간:** {start_date} ~ {end_date}")

if st.button("🚀 지정된 범위 데이터 분석 시작"):
    
    # 1. DART 공시 데이터 (2025.10 ~ 2026.03 범위)
    st.subheader("🔍 1. 수집된 공시 데이터 (Source: OpenDART)")
    with st.spinner("지정된 기간의 공시 수집 중..."):
        time.sleep(0.8)
        
        # 요청하신 기간에 맞춘 샘플 공시 데이터
        dart_data = {
            "공시일자": ["2026-03-20", "2026-02-14", "2025-12-28", "2025-11-15"],
            "보고서명": [
                "사업보고서 (2025.12)", 
                "단일판매·공급계약체결(해상풍력)", 
                "특수관계인과의자산양수도", 
                "분기보고서 (2025.09)"
            ],
            "원문링크": [
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260320000001",
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260214000002",
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20251228000003",
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20251115000004"
            ]
        }
        df_dart = pd.DataFrame(dart_data)
        st.data_editor(
            df_dart,
            column_config={
                "원문링크": st.column_config.LinkColumn("원문 보기", display_text="🔗 DART 열기"),
            },
            hide_index=True,
            use_container_width=True
        )

    # 2. 뉴스 데이터 (2025.10 ~ 2026.03 범위)
    st.subheader("📰 2. 관련 뉴스 및 트렌드 (Source: News)")
    with st.spinner("지정된 기간의 뉴스 검색 중..."):
        time.sleep(0.8)
        
        # 요청하신 기간 내의 실제 뉴스 시뮬레이션
        news_data = [
            {
                "날짜": "2026-03-25", 
                "제목": "SK에코플랜트, 2026년 기업공개(IPO) 재추진 동력 확보", 
                "출처": "연합뉴스",
                "URL": "https://www.yna.co.kr/view/AKR20240325041200003" # 시연용 실제기사 주소 유지
            },
            {
                "날짜": "2026-01-10", 
                "제목": "CES 2026: SK에코플랜트, 넷제로 시티 솔루션 공개", 
                "출처": "매일경제",
                "URL": "https://www.mk.co.kr/news/business/10967234"
            },
            {
                "날짜": "2025-11-20", 
                "제목": "SK에코플랜트-SK오션플랜트, 해상풍력 시너지 가시화", 
                "출처": "한국경제",
                "URL": "https://www.hankyung.com/article/2024022812345"
            },
            {
                "날짜": "2025-10-15", 
                "제목": "북미 폐배터리 재활용 공장 본격 가동 개시", 
                "출처": "전자신문",
                "URL": "https://www.etnews.com/"
            }
        ]
        
        for news in news_data:
            with st.expander(f"[{news['날짜']}] {news['제목']} ({news['출처']})"):
                st.markdown(f"**기사 원문:** [🔗 {news['출처']} 기사 바로가기]({news['URL']})")
                st.write("---")
                st.caption(f"본 기사는 {start_date} 이후의 주요 이슈로 분류되었습니다.")

    # 3. AI 종합 분석
    st.divider()
    st.subheader("🤖 3. 6개월간의 AI 종합 분석 리포트")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"### 📌 {start_date.year} 하반기 ~ {end_date.year} 상반기 흐름\n- **신사업 안착:** 폐배터리 및 해상풍력 부문 매출 비중 확대 확인\n- **재무 구조:** 자산 유동화를 통한 IPO 준비 작업 가속화")
    with col2:
        st.warning("### 🎯 향후 경영 관리 Point\n- **상장 준비:** IPO 시점의 시장 밸류에이션 모니터링 필요\n- **글로벌 규제:** 북미/유럽 환경 규제 변화에 따른 적기 대응")

else:
    st.info("좌측 사이드바에서 분석 기간을 확인하신 후 '분석 시작' 버튼을 눌러주세요.")

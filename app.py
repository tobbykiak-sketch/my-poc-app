import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time

# --- 페이지 설정 ---
st.set_page_config(page_title="이슈 Report 자동화 PoC", layout="wide")

# --- 헬퍼 함수: 6개월 전 날짜 계산 ---
def get_six_months_ago():
    return (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')

# --- 사이드바 설정 ---
with st.sidebar:
    st.header("⚙️ 검색 설정")
    target_company = st.text_input("대상 멤버사", value="SK에코플랜트")
    
    st.subheader("📅 검색 범위")
    start_date = st.date_input("시작일", value=datetime.now() - timedelta(days=180))
    end_date = st.date_input("종료일", value=datetime.now())
    st.caption(f"현재 설정: {start_date} ~ {end_date} (약 6개월)")
    
    st.divider()
    api_key_dart = st.text_input("DART API Key", type="password")
    api_key_llm = st.text_input("LLM API Key", type="password")

# --- 메인 화면 ---
st.title("📊 멤버사 이슈 모니터링 & AI 리포트")
st.markdown(f"**검색 대상:** `{target_company}` | **데이터 범위:** `{start_date}` ~ `{end_date}`")

if st.button("🚀 6개월 데이터 분석 시작"):
    
    # 1. DART 공시 데이터 (6개월 필터 적용 시뮬레이션)
    st.subheader("🔍 1. 수집된 공시 데이터 (Source: OpenDART)")
    with st.spinner("DART API 연동 중..."):
        time.sleep(1.5)
        # 실제 구현 시 여기에 DART API 호출 로직이 들어갑니다.
        dart_df = pd.DataFrame({
            "공시일자": ["2026-03-20", "2026-01-15", "2025-11-30", "2025-10-05"],
            "보고서명": ["단일판매·공급계약체결", "분기보고서(2025.09)", "유상증자 결정", "타법인 주식 및 출자증권 취득결정"],
            "출처": ["fss.or.kr (DART)", "fss.or.kr (DART)", "fss.or.kr (DART)", "fss.or.kr (DART)"]
        })
        st.dataframe(dart_df, use_container_width=True)

    # 2. 뉴스 데이터 (6개월 필터 및 출처 표기)
    st.subheader("📰 2. 관련 뉴스 및 트렌드 (Source: Google/Naver News)")
    with st.spinner("포털 뉴스 검색 중..."):
        time.sleep(1.5)
        news_data = [
            {"날짜": "2026-03-21", "제목": "SK에코플랜트, 해상풍력 하부구조물 대규모 수주", "출처": "경제신문 A"},
            {"날짜": "2026-02-10", "제목": "환경 에너지 기업 전환 가속화, 자회사 합병 추진", "출처": "매일경제 B"},
            {"날짜": "2025-12-05", "제목": "재무구조 개선 위한 자산 매각 검토 중", "출처": "한국경제 C"},
            {"날짜": "2025-10-20", "제목": "AI 기반 폐기물 처리 솔루션 현장 도입", "출처": "IT뉴스 D"},
        ]
        
        # 뉴스 카드 형태로 출력
        for news in news_data:
            with st.expander(f"[{news['날짜']}] {news['제목']}"):
                st.write(f"**원본 출처:** {news['출처']}")
                st.write("해당 기사의 본문 요약 내용이 이 자리에 표시됩니다.")

    # 3. AI 종합 분석 (시사점 도출)
    st.divider()
    st.subheader("🤖 3. AI 시사점 및 경영 관리 Point")
    
    with st.status("종합 분석 리포트 생성 중...") as status:
        time.sleep(2)
        st.write("✅ 6개월간의 수주 패턴 분석 완료")
        st.write("✅ 재무 공시 기반 위험 요인 체크 완료")
        status.update(label="분석 완료", state="complete")

    col1, col2 = st.columns(2)
    with col1:
        st.info("### 📌 6개월 주요 이슈 흐름")
        st.markdown("""
        - **수주 모멘텀:** 4분기 대비 1분기 수주 건수가 20% 증가하며 성장세 유지.
        - **사업 포트폴리오:** 단순 건설 비중은 줄고, 에너지 관련 공시 비중이 60% 이상으로 확대됨.
        """)
    with col2:
        st.warning("### 🎯 핵심 관리 포인트")
        st.markdown("""
        - **현금 흐름:** 유상증자 및 자산 매각 공시를 고려할 때, 단기 유동성 확보 전략 확인 필요.
        - **ESG 대응:** 환경 관련 뉴스 빈도가 높아짐에 따라 브랜드 이미지 관리 지표 설정 권장.
        """)

else:
    st.info("좌측 사이드바에서 기간을 확인하고 '분석 시작' 버튼을 눌러주세요.")

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
    start_date = st.date_input("시작일", value=datetime.now() - timedelta(days=180))
    end_date = st.date_input("종료일", value=datetime.now())
    
    st.divider()
    api_key_dart = st.text_input("DART API Key", type="password")
    api_key_llm = st.text_input("LLM API Key", type="password")

# --- 메인 화면 ---
st.title("📊 멤버사 이슈 모니터링 & AI 리포트")

if st.button("🚀 6개월 데이터 분석 시작"):
    
    # 1. DART 공시 데이터 (하이퍼링크 적용)
    st.subheader("🔍 1. 수집된 공시 데이터 (Source: OpenDART)")
    with st.spinner("DART API 연동 중..."):
        time.sleep(1)
        
        # 샘플 데이터에 실제 연결될 URL 추가
        dart_data = {
            "공시일자": ["2026-03-20", "2026-01-15", "2025-11-30"],
            "보고서명": ["단일판매·공급계약체결", "분기보고서(2025.09)", "유상증자 결정"],
            "출처기구": ["DART", "DART", "DART"],
            "원문링크": [
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240320000001", # 예시 링크
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240115000002",
                "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20231130000003"
            ]
        }
        df_dart = pd.DataFrame(dart_data)
        
        # 표 내부의 링크를 클릭 가능하게 설정
        st.data_editor(
            df_dart,
            column_config={
                "원문링크": st.column_config.LinkColumn(
                    "원문 보기",
                    help="클릭하면 DART 공시 원문으로 이동합니다",
                    display_text="🔗 열기"
                ),
            },
            hide_index=True,
            use_container_width=True
        )

    # 2. 뉴스 데이터 (제목에 링크 걸기)
    st.subheader("📰 2. 관련 뉴스 및 트렌드 (Source: Google/Naver News)")
    with st.spinner("포털 뉴스 검색 중..."):
        time.sleep(1)
        news_data = [
            {
                "날짜": "2026-03-21", 
                "제목": "SK에코플랜트, 해상풍력 하부구조물 대규모 수주", 
                "출처": "경제신문 A",
                "URL": "https://www.google.com/search?q=SK에코플랜트+수주" # 예시 링크
            },
            {
                "날짜": "2026-02-10", 
                "제목": "환경 에너지 기업 전환 가속화, 자회사 합병 추진", 
                "출처": "매일경제 B",
                "URL": "https://www.google.com/search?q=SK에코플랜트+에너지"
            }
        ]
        
        for news in news_data:
            # 제목 옆에 클릭 가능한 마크다운 링크 생성
            with st.expander(f"[{news['날짜']}] {news['제목']}"):
                st.write(f"**신문사:** {news['출처']}")
                # 마크다운 문법 [텍스트](URL)을 사용해 클릭 가능한 링크 구현
                st.markdown(f"**원문 읽기:** [이곳을 클릭하여 기사 원문으로 이동합니다]({news['URL']})")
                st.write("---")
                st.write("AI 요약: 해당 기사는 SK에코플랜트의 전략적 변화를 다루고 있습니다...")

    # 3. AI 종합 분석
    st.divider()
    st.subheader("🤖 3. AI 시사점 및 경영 관리 Point")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 📌 6개월 주요 이슈 흐름\n- 수주 패턴 분석 완료\n- 에너지 공시 비중 확대")
    with col2:
        st.warning("### 🎯 핵심 관리 포인트\n- 유동성 확보 전략 확인 필요\n- ESG 대응 지표 설정 권장")

else:
    st.info("좌측 사이드바에서 기간을 확인하고 '분석 시작' 버튼을 눌러주세요.")

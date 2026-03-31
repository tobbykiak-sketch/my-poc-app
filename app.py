import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- 페이지 설정 ---
st.set_page_config(page_title="이슈 Report 자동화 PoC", layout="wide")

# --- 사이드바: 설정 및 API 키 입력 ---
with st.sidebar:
    st.header("⚙️ 설정")
    target_company = st.text_input("대상 멤버사", value="SK에코플랜트")
    api_key_dart = st.text_input("DART API Key", type="password", help="OpenDART에서 발급받은 키를 입력하세요.")
    api_key_llm = st.text_input("LLM API Key (Claude/GPT)", type="password")
    st.info("※ PoC 단계에서는 샘플 데이터를 활용해 구동 가능합니다.")

# --- 메인 화면 ---
st.title("📊 멤버사 이슈 모니터링 & AI 리포트")
st.markdown(f"**대상 기업:** `{target_company}` | **기준 일자:** {datetime.now().strftime('%Y-%m-%d')}")

# --- 실행 버튼 ---
if st.button("🚀 리포트 생성 시작"):
    
    # 1. DART 공시 수집 (시뮬레이션)
    with st.status("🔍 DART 공시 자료 수집 중...", expanded=True) as status:
        time.sleep(1.5)
        st.write("✅ SK에코플랜트 최근 공시 5건 확인 완료")
        
        # 샘플 데이터 생성
        dart_data = pd.DataFrame({
            "공시일자": ["2026-03-27", "2026-03-20", "2026-03-15"],
            "보고서명": ["[기재정정]사업보고서", "단일판매·공급계약체결", "특수관계인과의거래"],
            "비고": ["정기공시", "수주", "계열사"]
        })
        st.table(dart_data)
        
        # 2. 관련 뉴스 검색 (시뮬레이션)
        st.write("📰 관련 인터넷 뉴스 수집 중...")
        time.sleep(1.5)
        news_list = [
            "SK에코플랜트, 해상풍력 하부구조물 대규모 수주 성공",
            "환경 기업 넘어 에너지 기업으로... SK에코플랜트의 변신",
            "건설 경기 침체 속에서도 신사업 비중 확대 중"
        ]
        for news in news_list:
            st.write(f"- {news}")

        # 3. AI 분석 및 시사점 도출 (시뮬레이션)
        st.write("🤖 AI(Claude 3.5) 기반 시사점 분석 중...")
        time.sleep(2)
        status.update(label="✅ 분석 완료!", state="complete", expanded=False)

    # --- 결과 리포트 섹션 ---
    st.divider()
    st.subheader("💡 AI 생성 이슈 리포트")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 📌 핵심 요약")
        st.write("""
        1. **사업구조 재편 가속화:** 공시 자료 분석 결과, 환경/에너지 신사업 부문의 자본 투입이 전년 대비 15% 증가함.
        2. **수주 경쟁력 강화:** 최근 해상풍력 하부구조물 수주는 단순 건설을 넘어 에너지 가치사슬 진입을 의미함.
        """)
        
    with col2:
        st.warning("### 🎯 경영 관리 Point")
        st.write("""
        - **유동성 관리:** 신사업 확장에 따른 부채 비율 모니터링 필요.
        - **EPC 시너지:** 기존 건설 역량과 환경 플랜트 사업 간의 인력 효율화 방안 검토 필요.
        """)

    # 4. 리포트 내보내기
    st.success("🎉 리포트 생성이 완료되었습니다.")
    st.button("📄 PDF로 저장하기 (기능 구현 예정)")

else:
    st.info("왼쪽 설정에서 대상 기업을 확인하고 '리포트 생성' 버튼을 클릭하세요.")

# --- 하단 안내 ---
st.caption("본 페이지는 2026년 상반기 AI 변화과제 PoC용으로 제작된 프로토타입입니다.")




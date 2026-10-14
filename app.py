import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# Cấu hình trang
st.set_page_config(page_title="Hệ thống phân tích & Dự báo cổ phiếu", layout="wide")

st.markdown("📈 **Hệ thống phân tích lịch sử dữ liệu và dự báo xu hướng giá cổ phiếu thông minh.**")
st.divider()

# Tạo 2 cột giao diện
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### ⚙️ Cài đặt tham số")
    ticker = st.text_input("Nhập mã cổ phiếu (VD: VNM.VN, FPT.VN, AAPL):", "VNM.VN")
    
    start_date = st.date_input("Chọn ngày bắt đầu:", datetime.date(2018, 1, 1))
    end_date = st.date_input("Chọn ngày kết thúc:", datetime.date.today())
    
    forecast_days = st.slider("Số ngày muốn dự báo:", 1, 30, 10)
    
    run_button = st.button("🚀 Tải dữ liệu & Chạy dự báo", type="primary")

with col2:
    st.markdown("### 📊 Biểu đồ & Kết quả phân tích")
    
    if not run_button:
        st.info("👉 Vui lòng cấu hình tham số ở cột bên trái và bấm nút 'Tải dữ liệu & Chạy dự báo' để bắt đầu.")
    else:
        with st.spinner("Đang tải dữ liệu và phân tích..."):
            data = yf.download(ticker, start=start_date, end=end_date)
            
            if not data.empty:
                st.success(f"Đã tải thành công dữ liệu cho mã: {ticker}")
                st.dataframe(data.tail())
                
                st.subheader("Biểu đồ lịch sử giá đóng cửa")
                st.line_chart(data['Close'])
            else:
                st.error("Không tìm thấy dữ liệu hoặc mã cổ phiếu không hợp lệ. Vui lòng kiểm tra lại!")

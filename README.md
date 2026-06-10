# 🏭 SWOT Analysis — Hoa Phat Group (HPG)

Web thuyết trình tương tác phân tích **SWOT Tập đoàn Hòa Phát (HPG)** — nhà sản xuất
thép lớn nhất Đông Nam Á. Xây dựng bằng **Python + Streamlit + Plotly**.

> *Industrial Leadership and Strategic Positioning: SWOT Analysis of Hoa Phat Group*
> — Business English 3, năm học 2025–2026.

---

## ✨ Tính năng

- **7 mục điều hướng**: Tổng quan, Điểm mạnh (S), Điểm yếu (W), Cơ hội (O), Thách thức (T), Dashboard tài chính, Ma trận SWOT & Khuyến nghị.
- **Biểu đồ tương tác** (Plotly): tăng trưởng doanh thu, thị phần, năng lực sản xuất, cơ cấu nợ, lãi vay, hiệu quả theo phân khúc.
- **KPI cards & ma trận SWOT** trực quan, giao diện được tùy biến theo tông màu công nghiệp.
- Mọi số liệu **trích trực tiếp từ báo cáo** và đặt riêng trong `data.py` để dễ chỉnh.

---

## 🚀 Chạy local

Yêu cầu: **Python 3.9+**

```bash
# 1. Clone repo
git clone https://github.com/<username>/hoa-phat-swot.git
cd hoa-phat-swot

# 2. (khuyến nghị) tạo môi trường ảo
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Cài thư viện
pip install -r requirements.txt

# 4. Chạy app
streamlit run app.py
```

App sẽ mở tại `http://localhost:8501`.

---

## ☁️ Deploy miễn phí (Streamlit Community Cloud)

1. Push project này lên một repo GitHub.
2. Vào [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Chọn repo, branch `main`, file chính `app.py` → **Deploy**.

Bạn sẽ nhận được một link công khai để trình bày.

---

## 📁 Cấu trúc

```
hoa-phat-swot/
├── app.py                  # Ứng dụng Streamlit chính (giao diện + biểu đồ)
├── data.py                 # Toàn bộ số liệu & nội dung SWOT
├── requirements.txt        # Thư viện cần thiết
├── .gitignore
├── .streamlit/
│   └── config.toml         # Cấu hình theme
└── README.md
```

---

## 🛠️ Tùy chỉnh

- **Đổi số liệu / nội dung**: sửa trong `data.py` (không cần đụng tới `app.py`).
- **Đổi màu sắc**: chỉnh các biến `NAVY`, `STEEL`, `ACCENT`… ở đầu `app.py` và `.streamlit/config.toml`.

---

## 👥 Nhóm thực hiện

| Họ tên | MSSV |
|---|---|
| Trương Minh Trí | 10325008 |
| Nguyễn Bình Minh | 10625012 |
| Ngô Đình Nguyên Phúc | 10625048 |
| Nguyễn Anh Dương Thanh | 10625099 |

**Giảng viên:** Nguyễn Thành Được · **Môn:** Business English 3

---

## 📌 Lưu ý

Đây là sản phẩm học thuật. Số liệu lấy từ báo cáo thường niên Hòa Phát 2025, báo cáo tài
chính hợp nhất đã kiểm toán 2025, World Steel Association và các nguồn được trích dẫn trong
báo cáo gốc. Không nhằm mục đích tư vấn đầu tư.

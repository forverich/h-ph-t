"""
data.py
--------
Toàn bộ số liệu sử dụng trong bài thuyết trình được trích trực tiếp từ báo cáo
"Industrial Leadership and Strategic Positioning: SWOT Analysis of Hoa Phat Group"
(Business English 3, 2025-2026) và các nguồn được trích dẫn trong báo cáo đó.

Đơn vị tiền tệ mặc định: tỷ VND (billion VND), trừ khi ghi chú khác.
"""

# ---------------------------------------------------------------------------
# Thông tin chung
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Tập đoàn Hòa Phát (Hoa Phat Group)",
    "ticker": "HPG",
    "exchange": "HOSE (niêm yết 2007)",
    "founded": 1992,
    "revenue_2025_trillion": 158.33,
    "country": "Việt Nam",
    "rank_world": "Nhà sản xuất thép thô lớn thứ 11 thế giới",
    "rank_region": "Lớn nhất Đông Nam Á",
    "export_countries": "Hơn 40 quốc gia trên 5 châu lục",
    "vn_output_2025_mt": 24.661,  # triệu tấn thép thô (World Steel Association)
}

SECTORS = [
    ("Sắt & Thép", "Thép thô, thép xây dựng, HRC, phôi thép, thép dự ứng lực"),
    ("Nông nghiệp", "Thức ăn chăn nuôi, chăn nuôi gia cầm"),
    ("Bất động sản", "Khu công nghiệp & xây dựng dân dụng"),
    ("Sản phẩm thép", "Ống thép, tôn mạ kẽm, tôn màu, dây rút"),
    ("Điện máy gia dụng", "Tủ lạnh, điều hòa, tủ đông, thiết bị nhà bếp"),
]

# ---------------------------------------------------------------------------
# Tài chính: Doanh thu & Lợi nhuận
# ---------------------------------------------------------------------------
# Doanh thu (tỷ VND) - các mốc được nêu trong báo cáo
REVENUE = {
    "years": [2016, 2025],
    "values": [33_885, 158_332],
    "growth_x": 4.7,
}

# Lợi nhuận sau thuế (tỷ VND) - các mốc được nêu trong báo cáo
PROFIT = {
    "years": [2021, 2023, 2025],
    "values": [35_000, 7_757, 15_515],  # 2023 ≈ một nửa của 2025 (2025 gấp đôi 2023)
    "note": "2021 là đỉnh lợi nhuận; 2025 phục hồi gấp đôi so với 2023 nhờ Dung Quất 2.",
}

# ---------------------------------------------------------------------------
# Thị phần & Năng lực sản xuất
# ---------------------------------------------------------------------------
MARKET_SHARE = {
    "Thép xây dựng": 33,
    "Ống thép": 25,
}

CAPACITY = {
    "labels": ["Thép thô 2025\n(Dung Quất 2)", "Mục tiêu năng lực\nhàng năm"],
    "values": [11, 16],  # triệu tấn
    "cost_advantage": "Chi phí sản xuất thấp hơn đối thủ 10-15%",
}

# ---------------------------------------------------------------------------
# Hiệu quả theo phân khúc (Segment Performance) - 2025
# ---------------------------------------------------------------------------
SEGMENT_REVENUE = {  # nghìn tỷ VND (trillion)
    "Thép": 163.1,
    "Nông nghiệp": 8.1,
    "Bất động sản": 1.7,
}

SEGMENT_PROFIT = {  # nghìn tỷ VND (trillion)
    "Thép": 27.17,
    "Nông nghiệp": 1.6,
    "Bất động sản": 1.23,
}

# ---------------------------------------------------------------------------
# Cơ cấu nợ & thanh khoản (rủi ro)
# ---------------------------------------------------------------------------
SHORT_TERM_DEBT = {  # nghìn tỷ VND
    "labels": ["Đầu 2025", "Cuối 2025"],
    "values": [55.88, 64.69],
    "growth_pct": 16,
}

INTEREST_EXPENSE = {  # nghìn tỷ VND
    "labels": ["Q4/2024", "Q4/2025"],
    "values": [0.56249, 1.236],
    "fy_2025": 3.11,
}

RECEIVABLES = {  # nghìn tỷ VND - phải thu ngắn hạn từ khách hàng
    "labels": ["Đầu 2025", "Cuối 2025"],
    "values": [4.35, 10.97],
}

# ---------------------------------------------------------------------------
# Nội dung phân tích SWOT
# ---------------------------------------------------------------------------
STRENGTHS = [
    {
        "title": "Công nghệ sản xuất khép kín (Closed-loop)",
        "body": (
            "Áp dụng quy trình lò cao - lò thổi oxy (BOF) tại các khu liên hợp: từ "
            "quặng → gang → phôi → thép thành phẩm. Hệ thống thu hồi khí than và nhiệt "
            "giúp tự chủ ~80% nhu cầu điện và tiết kiệm ~7.600 tấn than mỗi năm "
            "(ví dụ tại khu liên hợp Hải Dương)."
        ),
    },
    {
        "title": "Vị thế dẫn đầu ngành thép",
        "body": (
            "Nắm hơn 33% thị phần thép xây dựng và hơn 25% thị phần ống thép. Là doanh "
            "nghiệp duy nhất tại Việt Nam tự chủ hoàn toàn từ quặng đến HRC, chi phí sản "
            "xuất thấp hơn đối thủ 10-15% nhờ lợi thế kinh tế quy mô, chuỗi giá trị khép "
            "kín và hệ thống cảng nước sâu."
        ),
    },
    {
        "title": "Tài chính vững mạnh",
        "body": (
            "Doanh thu tăng từ 33.885 tỷ VND (2016) lên 158.332 tỷ VND (2025) — gần 4,7 "
            "lần. Lợi nhuận sau thuế 2025 đạt 15.515 tỷ VND, gấp đôi 2023 nhờ Dung Quất 2 "
            "nâng năng lực thép thô lên 11 triệu tấn."
        ),
    },
]

WEAKNESSES = [
    {
        "title": "Áp lực từ CapEx cao & đòn bẩy vận hành",
        "body": (
            "Các đại dự án (Dung Quất, Hải Dương) ngốn chi phí xây dựng dở dang lớn "
            "(~6,3 nghìn tỷ và 186,32 tỷ VND tại 31/12/2025) và đòi hỏi lượng máy móc "
            "khổng lồ. Điều này tạo đòn bẩy vận hành cao: phải sản xuất tối đa để bù khấu "
            "hao và lãi vay — một cú sốc ngắn hạn có thể xóa sạch biên lợi nhuận."
        ),
    },
    {
        "title": "Cơ cấu vốn đòn bẩy cao & áp lực thanh khoản",
        "body": (
            "Vay & thuê tài chính ngắn hạn tăng từ 55,88 lên 64,69 nghìn tỷ VND trong "
            "2025 (+16%). Chi phí lãi vay cả năm 2025 đạt 3,11 nghìn tỷ VND; riêng Q4/2025 "
            "(~1,236 nghìn tỷ) gấp hơn đôi cùng kỳ. Phải thu ngắn hạn tăng gần gấp đôi "
            "(4,35 → 10,97 nghìn tỷ), tiềm ẩn rủi ro nợ xấu và kẹt vốn lưu động."
        ),
    },
    {
        "title": "Rủi ro tập trung vào thép",
        "body": (
            "Thép chiếm ~94% doanh thu phân khúc và ~91% lợi nhuận phân khúc. Nông nghiệp "
            "và bất động sản còn quá nhỏ để bù đắp khi chu kỳ thép đi xuống — hiệu quả hợp "
            "nhất của HPG về bản chất là một 'canh bạc đòn bẩy' vào thị trường thép."
        ),
    },
]

OPPORTUNITIES = [
    {
        "title": "Mở rộng năng lực sản xuất",
        "body": (
            "Khu liên hợp Dung Quất 2 (Quảng Ngãi) vận hành đầy đủ từ Q1/2026, nâng tổng "
            "năng lực thép lên 16 triệu tấn/năm. Dự kiến sản xuất ray đường sắt tốc độ cao "
            "chất lượng cao từ 2027 với dây chuyền châu Âu hiện đại (đầu tư 10.000 tỷ VND)."
        ),
    },
    {
        "title": "Các siêu dự án sắp tới",
        "body": (
            "Đường sắt cao tốc Bắc - Nam dài 1.541 km, nối 20 tỉnh/thành, khởi công cuối "
            "2027 và hoàn thành 2035, dự kiến cần hơn 10 triệu tấn thép. HPG ở vị thế cung "
            "ứng thép, ray, trục bánh tàu — sản lượng thép thô đã tăng ~25% so với 2024."
        ),
    },
]

THREATS = [
    {
        "title": "Rủi ro cầu thị trường & chu kỳ ngành",
        "body": (
            "Ngành thép có tính chu kỳ cao, phụ thuộc tăng trưởng kinh tế, đầu tư công, "
            "bất động sản. Khi chu kỳ đảo chiều, cầu giảm nhanh nhưng năng lực đã đầu tư "
            "không thể giảm tương ứng → dư cung kéo dài, cạnh tranh gay gắt, áp lực giảm giá."
        ),
    },
    {
        "title": "Biến động giá nhiên liệu & nguyên liệu",
        "body": (
            "Chi phí nguyên liệu chiếm khoảng 72-75% tổng chi phí sản phẩm. Chỉ 1% biến "
            "động giá quặng sắt, than, thép phế cũng tác động đáng kể tới chi phí sản xuất."
        ),
    },
    {
        "title": "Cơ chế CBAM của EU",
        "body": (
            "Từ 01/01/2026, Cơ chế Điều chỉnh Biên giới Carbon (CBAM) của EU vận hành đầy "
            "đủ. Nhà nhập khẩu thép vào EU phải mua chứng chỉ CBAM tương ứng lượng phát "
            "thải ẩn — tạo rào cản thương mại mới, tăng chi phí xuất khẩu và đòi hỏi báo "
            "cáo phát thải chính xác tuyệt đối."
        ),
    },
]

RECOMMENDATION = {
    "body": (
        "Với nhu cầu ~10 triệu tấn thép cho dự án đường sắt cao tốc Bắc - Nam khởi công "
        "cuối 2027, Hòa Phát nên tận dụng cơ hội này ở vị thế nhà cung ứng & sản xuất thép "
        "dẫn đầu. Tập đoàn vẫn đang đầu tư năng lực sản xuất để chủ động đáp ứng khi hợp "
        "đồng được trao."
    ),
    "quote": (
        "Nếu sản phẩm tốt và giá hợp lý, khách hàng sẽ tự tìm đến bạn."
    ),
    "quote_author": "Trần Đình Long — Chủ tịch Hòa Phát (Tam, 2025)",
}

AUTHORS = [
    "Trương Minh Trí — 10325008",
    "Nguyễn Bình Minh — 10625012",
    "Ngô Đình Nguyên Phúc — 10625048",
    "Nguyễn Anh Dương Thanh — 10625099",
]

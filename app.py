"""
app.py
-------
Web thuyết trình tương tác: Phân tích SWOT Tập đoàn Hòa Phát (HPG).

Chạy local:
    streamlit run app.py
"""

import plotly.graph_objects as go
import streamlit as st

import data as D

# ---------------------------------------------------------------------------
# Cấu hình trang & bảng màu
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="SWOT • Hòa Phát Group (HPG)",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

NAVY = "#0B2A4A"
STEEL = "#3E6D9C"
ACCENT = "#E63946"      # đỏ thép / cảnh báo
GOLD = "#F4A024"
GREEN = "#2A9D8F"
GREY = "#8895A7"
LIGHT = "#F1F4F8"

PLOTLY_FONT = dict(family="Inter, Segoe UI, system-ui, sans-serif", color=NAVY)


def _style_fig(fig, height=380, legend=True):
    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=PLOTLY_FONT,
        title_font=dict(size=17, color=NAVY),
        showlegend=legend,
        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5),
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="rgba(11,42,74,0.08)", zeroline=False)
    return fig


# ---------------------------------------------------------------------------
# CSS tùy chỉnh
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{ background: linear-gradient(180deg, #FFFFFF 0%, {LIGHT} 100%); }}
    h1, h2, h3, h4, h5, h6 {{ color: {NAVY} !important; letter-spacing: -0.3px; }}
    /* Ép chữ vùng nội dung chính sang tông tối, tránh bị trắng khi máy ở dark mode */
    section[data-testid="stMain"] p,
    section[data-testid="stMain"] li,
    section[data-testid="stMain"] label,
    section[data-testid="stMain"] .stMarkdown {{ color: #324A63; }}
    .hero {{
        background: linear-gradient(120deg, {NAVY} 0%, {STEEL} 100%);
        color: white; padding: 2.2rem 2rem; border-radius: 18px;
        box-shadow: 0 12px 30px rgba(11,42,74,0.25);
    }}
    .hero h1 {{ color: white; margin: 0 0 .4rem 0; font-size: 2.1rem; }}
    .hero p {{ color: #DCE6F2; margin: 0; font-size: 1.02rem; }}
    .kpi {{
        background: white; border-radius: 14px; padding: 1.1rem 1.2rem;
        border: 1px solid rgba(11,42,74,0.08);
        box-shadow: 0 4px 14px rgba(11,42,74,0.06); height: 100%;
    }}
    .kpi .v {{ font-size: 1.7rem; font-weight: 800; color: {NAVY}; line-height: 1.1; }}
    .kpi .l {{ font-size: .82rem; color: {GREY}; margin-top: .25rem; }}
    .card {{
        background: white; border-radius: 14px; padding: 1.3rem 1.4rem;
        border-left: 5px solid {STEEL}; margin-bottom: 1rem;
        box-shadow: 0 4px 14px rgba(11,42,74,0.05);
    }}
    .card.s {{ border-left-color: {GREEN}; }}
    .card.w {{ border-left-color: {ACCENT}; }}
    .card.o {{ border-left-color: {STEEL}; }}
    .card.t {{ border-left-color: {GOLD}; }}
    .card h4 {{ margin: 0 0 .5rem 0; color: {NAVY}; font-size: 1.08rem; }}
    .card p {{ margin: 0; color: #324A63; line-height: 1.55; font-size: .96rem; }}
    .quote {{
        background: {NAVY}; color: white; padding: 1.6rem 1.8rem; border-radius: 16px;
        font-size: 1.25rem; font-style: italic; line-height: 1.5;
    }}
    .quote .a {{ display:block; margin-top: .8rem; font-size: .9rem; font-style: normal; color: {GOLD}; }}
    .pill {{
        display:inline-block; background: {LIGHT}; color: {NAVY};
        padding: .2rem .7rem; border-radius: 999px; font-size: .8rem;
        margin: .15rem .25rem .15rem 0; border: 1px solid rgba(11,42,74,0.1);
    }}
    table.tbl {{
        width: 100%; border-collapse: collapse; background: white;
        border-radius: 12px; overflow: hidden;
        box-shadow: 0 4px 14px rgba(11,42,74,0.06);
    }}
    table.tbl th {{
        background: {NAVY}; color: white !important; text-align: left;
        padding: .7rem 1rem; font-size: .92rem;
    }}
    table.tbl td {{
        padding: .65rem 1rem; color: #324A63 !important; font-size: .95rem;
        border-bottom: 1px solid rgba(11,42,74,0.08);
    }}
    table.tbl tr:last-child td {{ border-bottom: none; }}
    table.tbl tr:nth-child(even) td {{ background: {LIGHT}; }}
    section[data-testid="stSidebar"] {{ background: {NAVY}; }}
    section[data-testid="stSidebar"] * {{ color: #E6EEF7 !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Sidebar điều hướng
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🏭 HPG • SWOT")
    st.caption("Industrial Leadership & Strategic Positioning")
    page = st.radio(
        "Mục lục",
        [
            "Tổng quan",
            "Điểm mạnh (S)",
            "Điểm yếu (W)",
            "Cơ hội (O)",
            "Thách thức (T)",
            "Dashboard tài chính",
            "Ma trận SWOT & Khuyến nghị",
        ],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("Nhóm thực hiện")
    for a in D.AUTHORS:
        st.caption("• " + a)
    st.caption("Business English 3 · 2025-2026")


def section_header(title, sub=""):
    st.markdown(f"## {title}")
    if sub:
        st.markdown(f"<p style='color:{GREY};margin-top:-.5rem'>{sub}</p>", unsafe_allow_html=True)
    st.write("")


def render_cards(items, css):
    for it in items:
        st.markdown(
            f"<div class='card {css}'><h4>{it['title']}</h4><p>{it['body']}</p></div>",
            unsafe_allow_html=True,
        )


# ===========================================================================
# 1. TỔNG QUAN
# ===========================================================================
if page == "Tổng quan":
    st.markdown(
        f"""
        <div class='hero'>
          <h1>Phân tích SWOT — Tập đoàn Hòa Phát (HPG)</h1>
          <p>Nhà sản xuất thép lớn nhất Đông Nam Á · Doanh thu {D.COMPANY['revenue_2025_trillion']} nghìn tỷ VND (2025)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    c1, c2, c3, c4 = st.columns(4)
    kpis = [
        ("158,33 nghìn tỷ", "Doanh thu 2025 (VND)"),
        (">33%", "Thị phần thép xây dựng"),
        ("11 triệu tấn", "Năng lực thép thô 2025"),
        ("Top 11", "SX thép thô thế giới"),
    ]
    for col, (v, l) in zip([c1, c2, c3, c4], kpis):
        col.markdown(f"<div class='kpi'><div class='v'>{v}</div><div class='l'>{l}</div></div>", unsafe_allow_html=True)

    st.write("")
    left, right = st.columns([1.15, 1])
    with left:
        section_header("Giới thiệu", "Bối cảnh & vị thế")
        st.markdown(
            f"""
            **{D.COMPANY['name']}** (mã **{D.COMPANY['ticker']}**) là công ty cổ phần sản xuất công nghiệp
            của Việt Nam, thành lập năm **{D.COMPANY['founded']}**, niêm yết trên **{D.COMPANY['exchange']}**.

            Khởi đầu là công ty kinh doanh máy xây dựng (1992), chuyển sang sản xuất ống thép (2000),
            đến nay Hòa Phát cung cấp vật liệu đạt chuẩn cho hạ tầng, đường sắt, nhà cao tầng và
            **xuất khẩu tới {D.COMPANY['export_countries'].lower()}**.

            Năm 2025, Việt Nam là **{D.COMPANY['rank_world'].lower()}** và **{D.COMPANY['rank_region'].lower()}**,
            sản xuất **{D.COMPANY['vn_output_2025_mt']} triệu tấn** thép thô (World Steel Association).
            """
        )
    with right:
        section_header("5 lĩnh vực hoạt động")
        for name, desc in D.SECTORS:
            st.markdown(f"**{name}** — {desc}")

    st.divider()
    st.markdown("#### Bối cảnh ngành thép Việt Nam")
    cc = st.columns(3)
    points = [
        ("🔄 Tính chu kỳ cao", "Cầu thép tăng/giảm mạnh theo kinh tế & bất động sản."),
        ("⚔️ Cạnh tranh gay gắt", "Đối thủ nội (Hoa Sen, Pomina, VNSteel) & thép nhập khẩu giá rẻ."),
        ("🌱 Rào cản môi trường", "CBAM của EU buộc siết tiêu chuẩn phát thải carbon."),
    ]
    for col, (t, b) in zip(cc, points):
        col.markdown(f"<div class='card'><h4>{t}</h4><p>{b}</p></div>", unsafe_allow_html=True)


# ===========================================================================
# 2. ĐIỂM MẠNH
# ===========================================================================
elif page == "Điểm mạnh (S)":
    section_header("💪 Điểm mạnh (Strengths)", "Phân tích nội bộ")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        render_cards(D.STRENGTHS, "s")
    with col2:
        # Tăng trưởng doanh thu
        fig = go.Figure()
        fig.add_bar(
            x=[str(y) for y in D.REVENUE["years"]],
            y=D.REVENUE["values"],
            marker_color=[STEEL, GREEN],
            text=[f"{v:,.0f}" for v in D.REVENUE["values"]],
            textposition="outside",
        )
        fig.update_layout(title=f"Doanh thu: 2016 → 2025 (×{D.REVENUE['growth_x']})")
        fig.update_yaxes(title="tỷ VND")
        st.plotly_chart(_style_fig(fig, legend=False), use_container_width=True)

        # Thị phần
        labels = list(D.MARKET_SHARE.keys())
        vals = list(D.MARKET_SHARE.values())
        fig2 = go.Figure()
        fig2.add_bar(y=labels, x=vals, orientation="h", marker_color=NAVY,
                     text=[f"{v}%" for v in vals], textposition="outside")
        fig2.update_layout(title="Thị phần dẫn đầu của HPG")
        fig2.update_xaxes(range=[0, 45], title="%")
        st.plotly_chart(_style_fig(fig2, height=260, legend=False), use_container_width=True)

    st.info("💡 " + D.CAPACITY["cost_advantage"] + " nhờ chuỗi giá trị khép kín & lợi thế quy mô.")


# ===========================================================================
# 3. ĐIỂM YẾU
# ===========================================================================
elif page == "Điểm yếu (W)":
    section_header("⚠️ Điểm yếu (Weaknesses)", "Phân tích nội bộ — rủi ro thanh khoản & đòn bẩy")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        render_cards(D.WEAKNESSES, "w")
    with col2:
        # Nợ ngắn hạn
        fig = go.Figure()
        fig.add_bar(x=D.SHORT_TERM_DEBT["labels"], y=D.SHORT_TERM_DEBT["values"],
                    marker_color=[GREY, ACCENT],
                    text=[f"{v:.2f}" for v in D.SHORT_TERM_DEBT["values"]], textposition="outside")
        fig.update_layout(title=f"Vay ngắn hạn (+{D.SHORT_TERM_DEBT['growth_pct']}% trong 2025)")
        fig.update_yaxes(title="nghìn tỷ VND")
        st.plotly_chart(_style_fig(fig, height=300, legend=False), use_container_width=True)

        # Phải thu ngắn hạn
        fig2 = go.Figure()
        fig2.add_bar(x=D.RECEIVABLES["labels"], y=D.RECEIVABLES["values"],
                     marker_color=[GREY, GOLD],
                     text=[f"{v:.2f}" for v in D.RECEIVABLES["values"]], textposition="outside")
        fig2.update_layout(title="Phải thu ngắn hạn (gần gấp đôi)")
        fig2.update_yaxes(title="nghìn tỷ VND")
        st.plotly_chart(_style_fig(fig2, height=300, legend=False), use_container_width=True)

    st.write("")
    m1, m2, m3 = st.columns(3)
    m1.markdown(f"<div class='kpi'><div class='v'>3,11</div><div class='l'>Chi phí lãi vay cả năm 2025 (nghìn tỷ VND)</div></div>", unsafe_allow_html=True)
    m2.markdown(f"<div class='kpi'><div class='v'>×2+</div><div class='l'>Lãi vay Q4/2025 so với cùng kỳ 2024</div></div>", unsafe_allow_html=True)
    m3.markdown(f"<div class='kpi'><div class='v'>~94%</div><div class='l'>Doanh thu phân khúc đến từ thép</div></div>", unsafe_allow_html=True)


# ===========================================================================
# 4. CƠ HỘI
# ===========================================================================
elif page == "Cơ hội (O)":
    section_header("🚀 Cơ hội (Opportunities)", "Phân tích bên ngoài")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        render_cards(D.OPPORTUNITIES, "o")
    with col2:
        fig = go.Figure()
        fig.add_bar(x=D.CAPACITY["labels"], y=D.CAPACITY["values"],
                    marker_color=[STEEL, GREEN],
                    text=[f"{v} triệu tấn" for v in D.CAPACITY["values"]], textposition="outside")
        fig.update_layout(title="Năng lực sản xuất hướng tới 16 triệu tấn/năm")
        fig.update_yaxes(title="triệu tấn", range=[0, 19])
        st.plotly_chart(_style_fig(fig, legend=False), use_container_width=True)

    st.write("")
    st.markdown("#### 🛤️ Siêu dự án đường sắt cao tốc Bắc - Nam")
    r = st.columns(4)
    facts = [("1.541 km", "Chiều dài tuyến"), ("20", "Tỉnh/thành kết nối"),
             (">10 triệu tấn", "Nhu cầu thép"), ("2027–2035", "Khởi công → hoàn thành")]
    for col, (v, l) in zip(r, facts):
        col.markdown(f"<div class='kpi'><div class='v'>{v}</div><div class='l'>{l}</div></div>", unsafe_allow_html=True)


# ===========================================================================
# 5. THÁCH THỨC
# ===========================================================================
elif page == "Thách thức (T)":
    section_header("⚡ Thách thức (Threats)", "Phân tích bên ngoài")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        render_cards(D.THREATS, "t")
    with col2:
        # Cơ cấu chi phí nguyên liệu
        fig = go.Figure(go.Pie(
            labels=["Nguyên liệu (72-75%)", "Chi phí khác"],
            values=[73.5, 26.5], hole=0.55,
            marker_colors=[ACCENT, LIGHT],
        ))
        fig.update_traces(textinfo="label+percent", textposition="outside")
        fig.update_layout(title="Nguyên liệu chiếm phần lớn chi phí sản phẩm")
        st.plotly_chart(_style_fig(fig, legend=False), use_container_width=True)

    st.warning("🌍 **CBAM** vận hành đầy đủ từ 01/01/2026 — nhà xuất khẩu thép vào EU phải mua chứng chỉ carbon, tăng chi phí & yêu cầu báo cáo phát thải chính xác.")


# ===========================================================================
# 6. DASHBOARD TÀI CHÍNH
# ===========================================================================
elif page == "Dashboard tài chính":
    section_header("📊 Dashboard tài chính", "Tổng hợp các chỉ số chính (theo báo cáo)")

    c1, c2 = st.columns(2)
    with c1:
        # Lợi nhuận sau thuế
        fig = go.Figure()
        fig.add_bar(x=[str(y) for y in D.PROFIT["years"]], y=D.PROFIT["values"],
                    marker_color=[GOLD, GREY, GREEN],
                    text=[f"{v:,.0f}" for v in D.PROFIT["values"]], textposition="outside")
        fig.update_layout(title="Lợi nhuận sau thuế (tỷ VND)")
        st.plotly_chart(_style_fig(fig, legend=False), use_container_width=True)
        st.caption(D.PROFIT["note"])

    with c2:
        # Doanh thu phân khúc
        fig2 = go.Figure(go.Pie(
            labels=list(D.SEGMENT_REVENUE.keys()),
            values=list(D.SEGMENT_REVENUE.values()), hole=0.5,
            marker_colors=[NAVY, GREEN, GOLD],
        ))
        fig2.update_traces(textinfo="label+percent", textposition="outside")
        fig2.update_layout(title="Doanh thu theo phân khúc 2025 (nghìn tỷ VND)")
        st.plotly_chart(_style_fig(fig2), use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        # Lợi nhuận phân khúc
        fig3 = go.Figure(go.Pie(
            labels=list(D.SEGMENT_PROFIT.keys()),
            values=list(D.SEGMENT_PROFIT.values()), hole=0.5,
            marker_colors=[NAVY, GREEN, GOLD],
        ))
        fig3.update_traces(textinfo="label+percent", textposition="outside")
        fig3.update_layout(title="Lợi nhuận theo phân khúc 2025 (nghìn tỷ VND)")
        st.plotly_chart(_style_fig(fig3), use_container_width=True)

    with c4:
        # Lãi vay
        fig4 = go.Figure()
        fig4.add_bar(x=D.INTEREST_EXPENSE["labels"], y=D.INTEREST_EXPENSE["values"],
                     marker_color=[GREY, ACCENT],
                     text=[f"{v:.3f}" for v in D.INTEREST_EXPENSE["values"]], textposition="outside")
        fig4.update_layout(title="Chi phí lãi vay theo quý (nghìn tỷ VND)")
        st.plotly_chart(_style_fig(fig4, legend=False), use_container_width=True)

    st.divider()
    st.markdown("#### Bảng số liệu tổng hợp")
    rows = [
        ("Doanh thu 2016", "33.885 tỷ VND"),
        ("Doanh thu 2025", "158.332 tỷ VND"),
        ("LNST 2021 (đỉnh)", "~35.000 tỷ VND"),
        ("LNST 2025", "15.515 tỷ VND"),
        ("Vay ngắn hạn cuối 2025", "64,69 nghìn tỷ VND"),
        ("Chi phí lãi vay 2025", "3,11 nghìn tỷ VND"),
        ("Phải thu NH cuối 2025", "10,97 nghìn tỷ VND"),
    ]
    body = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in rows)
    st.markdown(
        f"<table class='tbl'><thead><tr><th>Chỉ tiêu</th><th>Giá trị</th></tr></thead>"
        f"<tbody>{body}</tbody></table>",
        unsafe_allow_html=True,
    )


# ===========================================================================
# 7. MA TRẬN SWOT & KHUYẾN NGHỊ
# ===========================================================================
elif page == "Ma trận SWOT & Khuyến nghị":
    section_header("🎯 Ma trận SWOT", "Tổng hợp 4 nhóm yếu tố")

    def matrix_cell(emoji, title, items, css):
        body = "".join(f"<div style='margin-bottom:.4rem'>• <b>{it['title']}</b></div>" for it in items)
        return f"<div class='card {css}'><h4>{emoji} {title}</h4>{body}</div>"

    a, b = st.columns(2)
    a.markdown(matrix_cell("💪", "Strengths", D.STRENGTHS, "s"), unsafe_allow_html=True)
    b.markdown(matrix_cell("⚠️", "Weaknesses", D.WEAKNESSES, "w"), unsafe_allow_html=True)
    c, d = st.columns(2)
    c.markdown(matrix_cell("🚀", "Opportunities", D.OPPORTUNITIES, "o"), unsafe_allow_html=True)
    d.markdown(matrix_cell("⚡", "Threats", D.THREATS, "t"), unsafe_allow_html=True)

    st.divider()
    section_header("✅ Khuyến nghị")
    st.markdown(f"<div class='card o'><p>{D.RECOMMENDATION['body']}</p></div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='quote'>“{D.RECOMMENDATION['quote']}”"
        f"<span class='a'>— {D.RECOMMENDATION['quote_author']}</span></div>",
        unsafe_allow_html=True,
    )

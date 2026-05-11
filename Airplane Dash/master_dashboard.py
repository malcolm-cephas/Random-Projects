# master_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import time
import io
from fpdf import FPDF

# Set Page Config
st.set_page_config(
    page_title="SkyFlow | Aviation Executive Insights",
    layout="wide",
    page_icon="✈️",
    initial_sidebar_state="expanded"
)

# --- PREMIUM MODERN LIGHT THEME CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap');

    /* Global Soft Gradient Background */
    html, body, [data-testid="stapp"], .main {
        font-family: 'Outfit', sans-serif;
        background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%) !important;
        color: #000000 !important;
    }

    /* Modern Glassmorphism Cards (Light) */
    div[data-testid="stVerticalBlock"] > div:has(div.stPlotlyChart), 
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric) {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.02) !important;
        backdrop-filter: blur(10px);
    }

    /* Professional Metric Styling */
    [data-testid="stMetric"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 100%) !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 14px !important;
        padding: 20px !important;
        box-shadow: inset 0 2px 4px rgba(255,255,255,0.8) !important;
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        color: #000000 !important;
    }

    [data-testid="stMetricLabel"] {
        font-weight: 700 !important;
        color: #475569 !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    /* Sidebar Styling - Modern Minimalist */
    [data-testid="stSidebar"], [data-testid="stSidebarContent"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
        box-shadow: 10px 0 15px -3px rgba(0, 0, 0, 0.05) !important;
    }

    [data-testid="stSidebar"] * {
        color: #000000 !important;
    }

    /* Interactive Buttons */
    button {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.2rem !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    button:hover {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px rgba(0,0,0,0.1) !important;
    }

    /* Typography Overhaul */
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
    }

    /* Hide Default Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# 📂 HELPER: PDF Generator
class SkyFlowReport(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 15)
        self.set_text_color(15, 23, 42)
        self.cell(0, 10, 'SKYFLOW EXECUTIVE ANALYTICS', ln=True, align='C')
        self.set_font('Helvetica', '', 10)
        self.cell(0, 5, 'Operational Efficiency & Financial Performance', ln=True, align='C')
        self.ln(10)
        self.line(10, 30, 200, 30)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | Confidential Enterprise Intelligence', 0, 0, 'C')

def create_pdf(otp, nps, margin, mbr):
    pdf = SkyFlowReport()
    pdf.add_page()
    
    # KPI Section
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, 'Mission Critical KPIs', ln=True)
    pdf.ln(2)
    
    pdf.set_font('Helvetica', '', 11)
    kpis = [
        ['Metric', 'Current Value'],
        ['On-Time Performance', f"{otp:.2f}%"],
        ['Net Promoter Score', f"{nps:.0f}"],
        ['Operating Margin', f"{margin:.2f}%"],
        ['Mishandled Bag Rate', f"{mbr:.1f}"]
    ]
    
    # Table styling
    pdf.set_fill_color(241, 245, 249)
    for row in kpis:
        fill = row[0] == 'Metric'
        pdf.cell(90, 10, row[0], 1, 0, 'L', fill)
        pdf.cell(90, 10, row[1], 1, 1, 'C', fill)
    
    pdf.ln(10)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, 'Strategic Summary', ln=True)
    pdf.set_font('Helvetica', '', 11)
    summary_text = (
        "The current reporting period shows stable operational consistency with "
        "positive trends in on-time performance and margin optimization. "
        "Customer sentiment remains a key area for strategic investment."
    )
    pdf.multi_cell(0, 10, summary_text)
    
    return bytes(pdf.output())

# 📂 HELPER: Load Data
@st.cache_data
def load_data(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

# Load all datasets
df_flights = load_data("01_Flight_Delay_Prediction/data/flights_sample.csv")
df_reviews = load_data("02_Customer_Satisfaction/data/processed_reviews.csv")
df_prices = load_data("03_Dynamic_Pricing/data/ticket_prices.csv")
df_profit = load_data("04_Route_Profitability/data/route_profitability.csv")
df_demand = load_data("06_Demand_Forecasting/data/historical_demand.csv")
df_baggage = load_data("07_Baggage_Analytics/data/baggage_flow.csv")

# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/airplane-take-off.png", width=80)
    st.markdown("<h2 style='color:#1E3A8A; font-weight:800; margin-top:10px;'>SkyFlow Admin</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("Global Control")
    region = st.selectbox("Market Region", ["North America", "Europe", "Asia-Pacific", "LATAM"])
    timeframe = st.radio("Reporting Period", ["Last 24 Hours", "Last 7 Days", "Quarter to Date"], index=1)
    
    st.markdown("---")
    st.subheader("System Status")
    st.success("API Integration: Active")
    st.info("Next Sync: in 12 mins")
    
    if st.button("🚀 Re-calculate Analytics"):
        st.toast("Syncing with live data...", icon="🔄")

# ---------------------------------------------------------
# HEADER SECTION
# ---------------------------------------------------------
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.markdown("<h1 style='color: black !important; font-size: 3rem;'>Aviation Executive Scorecard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#475569; font-size:1.2rem; font-weight:600; margin-top:-10px;'>Operational intelligence and financial oversight platform.</p>", unsafe_allow_html=True)

with header_col2:
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("📄 Generate Professional PDF", width="stretch"):
        if df_flights is not None and df_reviews is not None and df_profit is not None and df_baggage is not None:
            # Calculate values
            otp_val = (df_flights['arrival_delay'] <= 15).mean() * 100
            nps_val = ((df_reviews['overall_score'] >= 9).sum() - (df_reviews['overall_score'] <= 6).sum()) / len(df_reviews) * 100
            margin_val = df_profit['margin_pct'].mean()
            mbr_val = (df_baggage['is_mishandled'].mean() * 1000)

            with st.status("Synthesizing Executive PDF...", expanded=True) as status:
                st.write("Applying brand guidelines...")
                time.sleep(0.5)
                st.write("Formatting data tables...")
                pdf_bytes = create_pdf(otp_val, nps_val, margin_val, mbr_val)
                time.sleep(0.5)
                status.update(label="Professional PDF Ready!", state="complete", expanded=False)
            
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_bytes,
                file_name="SkyFlow_Executive_Report.pdf",
                mime="application/pdf",
                width="stretch"
            )

# ---------------------------------------------------------
# ROW 1: MISSION CRITICAL KPIs
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    if df_flights is not None:
        otp = (df_flights['arrival_delay'] <= 15).mean() * 100
        st.metric("On-Time Performance", f"{otp:.1f}%")

with kpi2:
    if df_reviews is not None:
        nps = ((df_reviews['overall_score'] >= 9).sum() - (df_reviews['overall_score'] <= 6).sum()) / len(df_reviews) * 100
        st.metric("Net Promoter Score", f"{nps:.0f}")

with kpi3:
    if df_profit is not None:
        avg_margin = df_profit['margin_pct'].mean()
        st.metric("Operating Margin", f"{avg_margin:.1f}%")

with kpi4:
    if df_baggage is not None:
        mbr = (df_baggage['is_mishandled'].mean() * 1000)
        st.metric("Mishandled Bag Rate", f"{mbr:.1f}")

# ---------------------------------------------------------
# ROW 2: STRATEGIC INSIGHTS
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
row2_col1, row2_col2 = st.columns([1.8, 1])

with row2_col1:
    st.markdown('### Carrier Efficiency Index')
    if df_flights is not None:
        carrier_otp = df_flights.groupby('carrier').apply(lambda x: (x['arrival_delay'] <= 15).mean() * 100, include_groups=False).reset_index(name='otp')
        fig_bar = px.bar(carrier_otp, x='carrier', y='otp', color='otp', 
                         color_continuous_scale='Blues', text_auto='.1f',
                         template="plotly_white")
        fig_bar.update_layout(
            height=400, 
            plot_bgcolor="rgba(0,0,0,0)", 
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(t=20, b=20, l=0, r=0),
            yaxis_title="OTP %",
            xaxis_title=None,
            font=dict(color="black")
        )
        st.plotly_chart(fig_bar, width="stretch", config={'displayModeBar': False})

with row2_col2:
    st.markdown('### Customer Sentiment')
    if df_reviews is not None:
        fig_pie = px.pie(df_reviews, names='sentiment_label', hole=0.6,
                         color_discrete_sequence=['#0EA5E9', '#6366F1', '#F43F5E'],
                         template="plotly_white")
        fig_pie.update_layout(
            height=400, 
            plot_bgcolor="rgba(0,0,0,0)", 
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(t=50, b=20, l=0, r=0),
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
            font=dict(color="black")
        )
        st.plotly_chart(fig_pie, width="stretch", config={'displayModeBar': False})

# ---------------------------------------------------------
# ROW 3: TREND ANALYSIS
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2>Operational Trends</h2>", unsafe_allow_html=True)
row3_col1, row3_col2, row3_col3 = st.columns(3)

with row3_col1:
    st.markdown("**DELAY VOLATILITY**")
    if df_flights is not None:
        fig_spark1 = px.area(df_flights.groupby('flight_date')['arrival_delay'].mean().reset_index(), 
                             x='flight_date', y='arrival_delay', template="plotly_white")
        fig_spark1.update_traces(
            line_color='#0EA5E9', 
            fillcolor='rgba(14, 165, 233, 0.2)',
            mode='lines+markers',
            marker=dict(size=4, color='#0EA5E9', opacity=0.8),
            line=dict(width=2)
        )
        fig_spark1.update_layout(
            height=250, 
            xaxis_visible=False, 
            yaxis_visible=True, 
            yaxis_title=None,
            margin=dict(l=10,r=10,t=10,b=10),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(gridcolor='rgba(0,0,0,0.1)', zeroline=False),
            font=dict(color="black")
        )
        st.plotly_chart(fig_spark1, width="stretch", config={'displayModeBar': False})

with row3_col2:
    st.markdown("**PRICE ELASTICITY**")
    if df_prices is not None:
        fig_spark2 = px.line(df_prices.groupby('days_to_departure')['price'].mean().reset_index(), 
                             x='days_to_departure', y='price', template="plotly_white")
        fig_spark2.update_traces(
            line_color='#EAB308',
            mode='lines+markers',
            marker=dict(size=4, opacity=0.6),
            line=dict(width=2, dash='solid')
        )
        fig_spark2.update_layout(
            height=250, 
            xaxis_visible=True, 
            yaxis_visible=True,
            xaxis_title="Days to Dept",
            yaxis_title=None,
            margin=dict(l=10,r=10,t=10,b=20),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(gridcolor='rgba(0,0,0,0.1)'),
            yaxis=dict(gridcolor='rgba(0,0,0,0.1)'),
            font=dict(color="black")
        )
        st.plotly_chart(fig_spark2, width="stretch", config={'displayModeBar': False})

with row3_col3:
    st.markdown("**DEMAND FORECAST**")
    if df_demand is not None:
        fig_spark3 = px.line(df_demand, x='month', y='passengers', template="plotly_white")
        fig_spark3.update_traces(
            line_color='#22C55E',
            mode='lines+markers',
            marker=dict(size=4, opacity=0.8),
            line=dict(width=2, shape='spline')
        )
        fig_spark3.update_layout(
            height=250, 
            xaxis_visible=False, 
            yaxis_visible=True,
            yaxis_title=None,
            margin=dict(l=10,r=10,t=10,b=10),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(gridcolor='rgba(0,0,0,0.1)', zeroline=False),
            font=dict(color="black")
        )
        st.plotly_chart(fig_spark3, width="stretch", config={'displayModeBar': False})

st.markdown("---")
footer_col1, footer_col2 = st.columns([3, 1])
with footer_col1:
    st.caption("SkyFlow | Enterprise Intelligence Platform | v2.5.0-PRO")
with footer_col2:
    st.markdown("<p style='text-align:right; font-size:0.8rem; color:#64748B;'>Last updated: 2026-05-06 09:07</p>", unsafe_allow_html=True)

import streamlit as st
from calendar import monthrange
import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Milk Bill Generator",
    page_icon="🥛",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Sans+3:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #fef9f0 0%, #fde8c8 50%, #fce0b0 100%);
    min-height: 100vh;
}

/* Title */
h1 {
    font-family: 'Playfair Display', serif !important;
    color: #7a3b00 !important;
    text-align: center;
    font-size: 2.6rem !important;
    letter-spacing: -0.5px;
    margin-bottom: 0.2rem !important;
}

.subtitle {
    text-align: center;
    color: #b36000;
    font-size: 1rem;
    margin-bottom: 2rem;
}

/* Card panels */
.card {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(8px);
    border-radius: 18px;
    padding: 2rem 2.2rem;
    box-shadow: 0 4px 24px rgba(180,100,0,0.10);
    border: 1px solid rgba(255,200,120,0.35);
    margin-bottom: 1.5rem;
}

/* Bill output */
.bill-card {
    background: linear-gradient(135deg, #7a3b00, #c46000);
    border-radius: 18px;
    padding: 2rem 2.4rem;
    color: #fff;
    box-shadow: 0 8px 32px rgba(120,60,0,0.22);
    margin-top: 1.5rem;
}
.bill-card h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    margin-bottom: 1.2rem;
    border-bottom: 1px solid rgba(255,255,255,0.25);
    padding-bottom: 0.6rem;
}
.bill-row {
    display: flex;
    justify-content: space-between;
    font-size: 1rem;
    padding: 0.35rem 0;
}
.bill-row.total {
    font-size: 1.4rem;
    font-weight: 700;
    border-top: 1px solid rgba(255,255,255,0.35);
    margin-top: 0.7rem;
    padding-top: 0.8rem;
}
.badge {
    background: rgba(255,255,255,0.18);
    border-radius: 8px;
    padding: 0.15rem 0.65rem;
    font-size: 0.88rem;
}

/* Divider */
hr { border: none; border-top: 1px solid #f0c080; margin: 1rem 0; }

/* Streamlit number/select overrides */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.7) !important;
    border-radius: 10px !important;
}
input[type="number"] {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("<h1>🥛 Milk Bill Generator</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Calculate your monthly milk bill in seconds</p>', unsafe_allow_html=True)

# ── Month / Year selector ─────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📅 Bill Period")
col1, col2 = st.columns(2)
months = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}
current = datetime.date.today()
with col1:
    month_name = st.selectbox("Month", list(months.keys()),
                              index=current.month - 1)
with col2:
    year = st.number_input("Year", min_value=2000, max_value=2100,
                           value=current.year, step=1)

month_num = months[month_name]
total_days = monthrange(int(year), month_num)[1]
st.markdown(f'<p style="color:#7a3b00;font-size:0.92rem;">📌 {month_name} {int(year)} has <b>{total_days}</b> days.</p>',
            unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Milk Details ──────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🐄 Milk Details")
col3, col4, col5 = st.columns(3)
with col3:
    liters_per_day = st.number_input("Milk per day (Liters)",
                                     min_value=0.0, max_value=50.0,
                                     value=1.0, step=0.5,
                                     format="%.2f")
with col4:
    rate_per_liter = st.number_input("Rate per Liter (₹)",
                                     min_value=0.0, max_value=500.0,
                                     value=60.0, step=1.0,
                                     format="%.2f")
with col5:
    absent_days = st.number_input("Absent / Missing Days",
                                  min_value=0, max_value=total_days,
                                  value=0, step=1)
st.markdown('</div>', unsafe_allow_html=True)

# ── Calculation & Output ──────────────────────────────────────────────────────
if st.button("🧾 Generate Bill", use_container_width=True):

    delivery_days = total_days - absent_days
    if delivery_days < 0:
        st.error("Absent days cannot exceed total days in the month!")
    else:
        total_liters = liters_per_day * delivery_days
        total_amount = total_liters * rate_per_liter

        bill_html = f"""
        <div class="bill-card">
            <h2>🧾 Monthly Milk Bill</h2>
            <div class="bill-row">
                <span>Period</span>
                <span class="badge">{month_name} {int(year)}</span>
            </div>
            <div class="bill-row">
                <span>Total Days in Month</span>
                <span>{total_days} days</span>
            </div>
            <div class="bill-row">
                <span>Absent / Missing Days</span>
                <span>{absent_days} days</span>
            </div>
            <div class="bill-row">
                <span>Delivery Days</span>
                <span>{delivery_days} days</span>
            </div>
            <hr style="border-color:rgba(255,255,255,0.2);margin:0.8rem 0;">
            <div class="bill-row">
                <span>Milk per Day</span>
                <span>{liters_per_day:.2f} L</span>
            </div>
            <div class="bill-row">
                <span>Total Milk Delivered</span>
                <span>{total_liters:.2f} L</span>
            </div>
            <div class="bill-row">
                <span>Rate per Liter</span>
                <span>₹ {rate_per_liter:.2f}</span>
            </div>
            <div class="bill-row total">
                <span>💰 Total Amount</span>
                <span>₹ {total_amount:,.2f}</span>
            </div>
        </div>
        """
        st.markdown(bill_html, unsafe_allow_html=True)

        # Download as text receipt
        receipt = f"""
==============================
       MILK BILL RECEIPT
==============================
Period        : {month_name} {int(year)}
------------------------------
Total Days    : {total_days}
Absent Days   : {absent_days}
Delivery Days : {delivery_days}
------------------------------
Milk/Day      : {liters_per_day:.2f} L
Total Milk    : {total_liters:.2f} L
Rate/Liter    : Rs. {rate_per_liter:.2f}
------------------------------
TOTAL AMOUNT  : Rs. {total_amount:,.2f}
==============================
        """
        st.download_button(
            label="⬇️ Download Receipt (.txt)",
            data=receipt.strip(),
            file_name=f"milk_bill_{month_name}_{int(year)}.txt",
            mime="text/plain",
            use_container_width=True,
        )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<p style="text-align:center;color:#b36000;font-size:0.82rem;">Made with ❤️ using Streamlit</p>',
            unsafe_allow_html=True)

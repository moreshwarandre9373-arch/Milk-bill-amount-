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

/* ── Animated background ── */
@keyframes bgShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background: linear-gradient(
        135deg,
        #fff8ee 0%,
        #fde8c8 20%,
        #fcd5a0 40%,
        #f9c07a 60%,
        #fde8c8 80%,
        #fff8ee 100%
    );
    background-size: 300% 300%;
    animation: bgShift 12s ease infinite;
    min-height: 100vh;
}

/* ── Title ── */
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

/* ── Card panels ── */
.card {
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 18px;
    padding: 2rem 2.2rem;
    box-shadow: 0 4px 28px rgba(180, 100, 0, 0.12);
    border: 1px solid rgba(255, 200, 120, 0.45);
    margin-bottom: 1.5rem;
}

/* ── Bill output ── */
.bill-card {
    background: linear-gradient(135deg, #7a3b00, #c46000);
    border-radius: 18px;
    padding: 2rem 2.4rem;
    color: #fff;
    box-shadow: 0 8px 32px rgba(120, 60, 0, 0.28);
    margin-top: 1.5rem;
}
.bill-card h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    margin-bottom: 1.2rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.25);
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
    border-top: 1px solid rgba(255, 255, 255, 0.35);
    margin-top: 0.7rem;
    padding-top: 0.8rem;
}
.badge {
    background: rgba(255, 255, 255, 0.18);
    border-radius: 8px;
    padding: 0.15rem 0.65rem;
    font-size: 0.88rem;
}

/* ── Divider ── */
hr { border: none; border-top: 1px solid #f0c080; margin: 1rem 0; }

/* ── Streamlit widget overrides ── */
div[data-baseweb="select"] > div {
    background: rgba(255, 255, 255, 0.75) !important;
    border-radius: 10px !important;
}
input[type="number"] {
    border-radius: 10px !important;
}

/* ── Generate button ── */
.stButton > button {
    background: linear-gradient(135deg, #c46000, #7a3b00) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    padding: 0.65rem 1.5rem !important;
    box-shadow: 0 4px 14px rgba(120, 60, 0, 0.22) !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
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
    "September": 9, "October": 10, "November": 11, "December": 12,
}
current = datetime.date.today()
with col1:
    month_name = st.selectbox("Month", list(months.keys()), index=current.month - 1)
with col2:
    year = st.number_input("Year", min_value=2000, max_value=2100,
                           value=current.year, step=1)

month_num = months[month_name]
total_days = monthrange(int(year), month_num)[1]
st.markdown(
    f'<p style="color:#7a3b00;font-size:0.92rem;">📌 {month_name} {int(year)} has <b>{total_days}</b> days.</p>',
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)

# ── Milk Details ──────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🐄 Milk Details")

col3, col4 = st.columns(2)
with col3:
    liters_per_day = st.number_input(
        "Milk per day (Liters)",
        min_value=0.0, max_value=50.0,
        value=1.0, step=0.5, format="%.2f",
    )
with col4:
    rate_per_liter = st.number_input(
        "Rate per Liter (₹)",
        min_value=0.0, max_value=500.0,
        value=60.0, step=1.0, format="%.2f",
    )

col5, col6 = st.columns(2)
with col5:
    absent_days = st.number_input(
        "Absent / Missing Days",
        min_value=0, max_value=total_days,
        value=0, step=1,
    )
with col6:
    extra_liters = st.number_input(
        "Extra Litres (one-time addition)",
        min_value=0.0, max_value=500.0,
        value=0.0, step=0.5, format="%.2f",
        help="Add any one-time extra litres purchased outside the daily schedule.",
    )

st.markdown('</div>', unsafe_allow_html=True)

# ── Calculation & Output ──────────────────────────────────────────────────────
if st.button("🧾 Generate Bill", use_container_width=True):

    delivery_days = total_days - absent_days
    if delivery_days < 0:
        st.error("Absent days cannot exceed total days in the month!")
    else:
        daily_liters   = liters_per_day * delivery_days
        total_liters   = daily_liters + extra_liters
        total_amount   = total_liters * rate_per_liter
        extra_amount   = extra_liters * rate_per_liter

        # Build extra-litre row only when relevant
        extra_row = ""
        if extra_liters > 0:
            extra_row = f"""
            <div class="bill-row">
                <span>Extra Litres (one-time)</span>
                <span>{extra_liters:.2f} L &nbsp;·&nbsp; ₹ {extra_amount:,.2f}</span>
            </div>"""

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
                <span>Daily Milk Delivered</span>
                <span>{daily_liters:.2f} L</span>
            </div>
            {extra_row}
            <div class="bill-row">
                <span>Total Milk (incl. extra)</span>
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

        # ── Download receipt ──
        extra_receipt_line = (
            f"Extra Litres  : {extra_liters:.2f} L (₹ {extra_amount:,.2f})\n"
            if extra_liters > 0 else ""
        )
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
Daily Milk    : {daily_liters:.2f} L
{extra_receipt_line}Total Milk    : {total_liters:.2f} L
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

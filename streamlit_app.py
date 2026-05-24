import streamlit as st
import datetime
import random

st.set_page_config(
    page_title="AgroShield AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Sora:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main-header {
    background: linear-gradient(135deg, #0f4c2a 0%, #1a6b3c 50%, #0d3b22 100%);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    color: white;
    margin-bottom: 1.5rem;
}

.main-header h1 {
    font-family: 'Sora', sans-serif;
    font-size: 2.2rem;
    font-weight: 600;
    margin: 0;
    letter-spacing: -0.5px;
}

.main-header p {
    font-size: 1rem;
    opacity: 0.8;
    margin: 0.4rem 0 0;
}

.metric-card {
    background: white;
    border: 1px solid #e8f5e9;
    border-radius: 14px;
    padding: 1.2rem 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.weather-card {
    background: linear-gradient(135deg, #1a3a2a 0%, #1e4530 100%);
    border-radius: 16px;
    padding: 1.5rem;
    color: white;
}

.crop-card {
    background: white;
    border: 1px solid #e0f2e9;
    border-radius: 14px;
    padding: 1.2rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    height: 100%;
}

.alert-box {
    background: #fffbeb;
    border: 1px solid #fbbf24;
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    margin: 0.5rem 0;
}

.market-row {
    background: white;
    border: 1px solid #e8f5e9;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}

.section-header {
    font-family: 'Sora', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: #1a3a2a;
    margin: 1.2rem 0 0.8rem;
}

.badge-success { background: #d1fae5; color: #065f46; border-radius: 6px; padding: 2px 10px; font-size: 0.78rem; font-weight: 500; }
.badge-warning { background: #fef3c7; color: #92400e; border-radius: 6px; padding: 2px 10px; font-size: 0.78rem; font-weight: 500; }
.badge-danger  { background: #fee2e2; color: #991b1b; border-radius: 6px; padding: 2px 10px; font-size: 0.78rem; font-weight: 500; }
.badge-info    { background: #dbeafe; color: #1e40af; border-radius: 6px; padding: 2px 10px; font-size: 0.78rem; font-weight: 500; }

.chat-bubble-user {
    background: #1a6b3c;
    color: white;
    border-radius: 16px 16px 4px 16px;
    padding: 0.7rem 1rem;
    margin: 0.4rem 0;
    max-width: 80%;
    margin-left: auto;
    font-size: 0.92rem;
}

.chat-bubble-bot {
    background: #f0f9f4;
    color: #1a3a2a;
    border: 1px solid #c6e8d4;
    border-radius: 16px 16px 16px 4px;
    padding: 0.7rem 1rem;
    margin: 0.4rem 0;
    max-width: 80%;
    font-size: 0.92rem;
}

.stButton > button {
    background: #1a6b3c;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 500;
    transition: all 0.2s;
}

.stButton > button:hover {
    background: #15593e;
    box-shadow: 0 4px 12px rgba(26,107,60,0.3);
}

.sidebar-nav-item {
    padding: 0.6rem 1rem;
    border-radius: 10px;
    cursor: pointer;
    font-weight: 500;
    color: #2d6a4f;
    transition: background 0.15s;
}

.sidebar-nav-item:hover {
    background: #e8f5e9;
}

[data-testid="stSidebar"] {
    background: #f0f9f4;
    border-right: 1px solid #c8e6d4;
}

.progress-track {
    background: #e8f5e9;
    border-radius: 4px;
    height: 6px;
    margin: 0.4rem 0;
    overflow: hidden;
}

.progress-fill-green { background: #1a6b3c; height: 6px; border-radius: 4px; }
.progress-fill-amber { background: #d97706; height: 6px; border-radius: 4px; }
.progress-fill-blue  { background: #2563eb; height: 6px; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 1rem 0 0.5rem; text-align: center;'>
        <div style='font-size: 2rem;'>🌿</div>
        <div style='font-family: Sora, sans-serif; font-size: 1.1rem; font-weight: 600; color: #1a3a2a;'>AgroShield AI</div>
        <div style='font-size: 0.78rem; color: #6b7280; margin-top: 2px;'>Smart farming assistant</div>
    </div>
    <hr style='border: none; border-top: 1px solid #c8e6d4; margin: 0.8rem 0;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🏠  Dashboard", "🔬  Crop Scanner", "🤖  AI Assistant", "📈  Market Prices", "🌾  Harvest Planner"],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border: none; border-top: 1px solid #c8e6d4; margin: 1rem 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size: 0.78rem; color: #6b7280; padding: 0 0.5rem;'>
        <div style='font-weight: 500; color: #2d6a4f; margin-bottom: 0.4rem;'>📍 Your farm</div>
        <div>Kandy Region, Sri Lanka</div>
        <div style='margin-top: 0.3rem;'>🌱 3 active crops</div>
        <div style='margin-top: 0.3rem;'>📐 2.4 acres</div>
    </div>
    """, unsafe_allow_html=True)


# ── Pages ─────────────────────────────────────────────────────────────────────

# ── DASHBOARD ──
if page == "🏠  Dashboard":
    st.markdown("""
    <div class='main-header'>
        <h1>🌿 Good morning, Suresh</h1>
        <p>Monday, 26 May 2025 · Kandy Region · Everything looks healthy today</p>
    </div>
    """, unsafe_allow_html=True)

    # Weather row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <div style='font-size: 0.78rem; color: #6b7280; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;'>TEMPERATURE</div>
            <div style='font-size: 2rem; font-weight: 600; color: #1a3a2a; font-family: Sora, sans-serif;'>28°C</div>
            <div style='font-size: 0.82rem; color: #6b7280;'>☁️ Partly cloudy</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <div style='font-size: 0.78rem; color: #6b7280; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;'>HUMIDITY</div>
            <div style='font-size: 2rem; font-weight: 600; color: #1a3a2a; font-family: Sora, sans-serif;'>74%</div>
            <div style='font-size: 0.82rem; color: #6b7280;'>💧 Optimal range</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <div style='font-size: 0.78rem; color: #6b7280; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;'>RAIN CHANCE</div>
            <div style='font-size: 2rem; font-weight: 600; color: #1a3a2a; font-family: Sora, sans-serif;'>30%</div>
            <div style='font-size: 0.82rem; color: #6b7280;'>🌦️ Light showers</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class='metric-card'>
            <div style='font-size: 0.78rem; color: #6b7280; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;'>WIND SPEED</div>
            <div style='font-size: 2rem; font-weight: 600; color: #1a3a2a; font-family: Sora, sans-serif;'>12 km/h</div>
            <div style='font-size: 0.82rem; color: #6b7280;'>🌬️ Gentle breeze</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Alert
    st.markdown("""
    <div class='alert-box'>
        ⚠️ <strong>Heavy rain alert — Wednesday:</strong> Consider early harvesting of ripe tomatoes. Secure any dry harvested crops before Tuesday evening.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>My crops</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    crops = [
        ("🍅 Tomatoes", "Fruiting stage", 78, "#1a6b3c", "progress-fill-green", "Harvest in ~12 days", "success"),
        ("🧅 Onions", "Bulbing stage", 55, "#d97706", "progress-fill-amber", "Harvest in ~28 days", "warning"),
        ("🌾 Rice", "Tillering stage", 30, "#2563eb", "progress-fill-blue", "Harvest in ~62 days", "info"),
    ]
    for col, (name, stage, pct, color, fill_cls, harvest, badge) in zip([c1, c2, c3], crops):
        with col:
            st.markdown(f"""
            <div class='crop-card'>
                <div style='font-family: Sora, sans-serif; font-weight: 600; font-size: 1rem; color: #1a3a2a;'>{name}</div>
                <div style='font-size: 0.82rem; color: #6b7280; margin: 0.3rem 0;'>{stage}</div>
                <div class='progress-track'>
                    <div class='{fill_cls}' style='width: {pct}%;'></div>
                </div>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-top: 0.6rem;'>
                    <span style='font-size: 0.82rem; color: #6b7280;'>{harvest}</span>
                    <span class='badge-{badge}'>{pct}%</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>Recent AI insights</div>", unsafe_allow_html=True)
    insights = [
        ("🌿", "Tomato leaves show early signs of water stress. Increase irrigation by 15% for next 3 days.", "2 hours ago"),
        ("💡", "Onion prices at Dambulla market up 12% this week. Consider holding 30% of harvest.", "5 hours ago"),
        ("☀️", "UV index will be high Thursday–Friday. Shade young rice seedlings if possible.", "8 hours ago"),
    ]
    for icon, text, time in insights:
        st.markdown(f"""
        <div style='background: white; border: 1px solid #e0f2e9; border-radius: 12px; padding: 0.9rem 1.2rem; margin-bottom: 0.5rem; display: flex; align-items: flex-start; gap: 0.8rem; box-shadow: 0 1px 4px rgba(0,0,0,0.04);'>
            <span style='font-size: 1.3rem;'>{icon}</span>
            <div style='flex: 1;'>
                <div style='font-size: 0.9rem; color: #1a3a2a;'>{text}</div>
                <div style='font-size: 0.78rem; color: #9ca3af; margin-top: 0.3rem;'>{time}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── CROP SCANNER ──
elif page == "🔬  Crop Scanner":
    st.markdown("""
    <div class='main-header'>
        <h1>🔬 AI Plant Doctor</h1>
        <p>Upload a leaf photo to detect diseases, pests, and nutrient deficiencies instantly</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### Upload leaf photo")
        uploaded = st.file_uploader("Choose a photo of your crop leaf", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        crop_type = st.selectbox("Crop type", ["Tomato", "Rice", "Onion", "Chilli", "Beans", "Cabbage", "Other"])

        if uploaded:
            st.image(uploaded, use_container_width=True)
            analyze = st.button("🔍  Analyze with AI", use_container_width=True)
        else:
            st.markdown("""
            <div style='border: 2px dashed #a7d7b8; border-radius: 14px; padding: 3rem; text-align: center; background: #f8fdf9; color: #6b9e7a;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📷</div>
                <div style='font-weight: 500;'>Drop a photo here</div>
                <div style='font-size: 0.85rem; margin-top: 0.3rem;'>JPG or PNG, clear photo of a single leaf</div>
            </div>
            """, unsafe_allow_html=True)
            analyze = False

    with col2:
        st.markdown("#### Scan result")
        if uploaded and analyze:
            with st.spinner("Analyzing your crop..."):
                import time; time.sleep(1.5)

            st.markdown("""
            <div style='background: #fffbeb; border: 1px solid #fbbf24; border-radius: 14px; padding: 1.2rem; margin-bottom: 1rem;'>
                <div style='display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.8rem;'>
                    <span style='font-size: 1.4rem;'>⚠️</span>
                    <div>
                        <div style='font-family: Sora, sans-serif; font-weight: 600; color: #92400e;'>Early Blight Detected</div>
                        <div style='font-size: 0.82rem; color: #a16207;'>Alternaria solani · Moderate severity</div>
                    </div>
                    <span class='badge-warning' style='margin-left: auto;'>Moderate</span>
                </div>
                <div style='font-size: 0.85rem; color: #78350f;'><strong>Confidence:</strong> 87%</div>
            </div>

            <div style='background: #f0f9f4; border: 1px solid #bbf7d0; border-radius: 14px; padding: 1.2rem;'>
                <div style='font-family: Sora, sans-serif; font-weight: 600; color: #1a3a2a; margin-bottom: 0.8rem;'>✅ Treatment recommendations</div>
                <div style='font-size: 0.88rem; color: #2d4a3e; line-height: 1.7;'>
                    <div>🌿 Remove and destroy infected leaves immediately</div>
                    <div>💊 Apply copper-based fungicide (2g/L) every 7 days</div>
                    <div>💧 Avoid overhead watering — use drip irrigation</div>
                    <div>🌬️ Improve air circulation between plants</div>
                    <div>🌱 Apply balanced NPK fertilizer to boost immunity</div>
                </div>
                <div style='margin-top: 0.8rem; padding-top: 0.8rem; border-top: 1px solid #bbf7d0;'>
                    <div style='font-size: 0.78rem; color: #6b9e7a;'>⏰ Act within 48 hours to prevent spread</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='background: #f8fdf9; border: 1px solid #c6e8d4; border-radius: 14px; padding: 2.5rem; text-align: center; color: #6b9e7a;'>
                <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🌱</div>
                <div style='font-weight: 500; font-family: Sora, sans-serif;'>Results will appear here</div>
                <div style='font-size: 0.85rem; margin-top: 0.3rem;'>Upload a photo and click Analyze</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("#### Common diseases in your region")
        for disease, crop, risk in [("Early Blight", "Tomato", "High"), ("Blast", "Rice", "Medium"), ("Purple Blotch", "Onion", "Low")]:
            badge = "danger" if risk == "High" else ("warning" if risk == "Medium" else "success")
            st.markdown(f"""
            <div style='background: white; border: 1px solid #e0f2e9; border-radius: 10px; padding: 0.7rem 1rem; margin-bottom: 0.4rem; display: flex; justify-content: space-between; align-items: center;'>
                <div><span style='font-weight: 500; color: #1a3a2a;'>{disease}</span><span style='font-size: 0.8rem; color: #6b7280; margin-left: 0.5rem;'>({crop})</span></div>
                <span class='badge-{badge}'>{risk} risk</span>
            </div>
            """, unsafe_allow_html=True)


# ── AI ASSISTANT ──
elif page == "🤖  AI Assistant":
    st.markdown("""
    <div class='main-header'>
        <h1>🤖 AI Farming Assistant</h1>
        <p>Ask anything about your crops, weather, fertilizers, or farming practices — 24/7</p>
    </div>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "bot", "text": "Hello Suresh! 🌿 I'm your AgroShield AI assistant. I know your farm in Kandy is growing tomatoes, onions, and rice. How can I help you today?"}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div style='text-align: right; margin: 0.4rem 0;'><span class='chat-bubble-user'>{msg['text']}</span></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='margin: 0.4rem 0;'><span class='chat-bubble-bot'>🌿 {msg['text']}</span></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    suggestions = ["How much water for tomatoes?", "Best fertilizer for onions?", "When should I harvest?", "Signs of nitrogen deficiency?"]
    cols = st.columns(4)
    for col, sug in zip(cols, suggestions):
        with col:
            if st.button(sug, use_container_width=True, key=f"sug_{sug}"):
                st.session_state.messages.append({"role": "user", "text": sug})
                responses = {
                    "How much water for tomatoes?": "Tomatoes need 25–50mm of water per week. In Kandy's current heat (28°C), water deeply every 2 days. Morning watering is best — wet leaves at night increase blight risk. Drip irrigation saves 40% water vs overhead.",
                    "Best fertilizer for onions?": "For onions in bulbing stage: use NPK 5-10-15. Apply 50g per sq meter now, 2 weeks before harvest. Avoid high nitrogen at this stage — it grows leaves, not bulbs. Potassium (K) is key for bulb quality.",
                    "When should I harvest?": "Your tomatoes are 78% mature — check in 10–12 days. Look for: deep red color, slight give when pressed, easy stem separation. Harvest morning for best shelf life. For onions, wait until 50% of tops fall over naturally.",
                    "Signs of nitrogen deficiency?": "Watch for: yellowing starting from older/lower leaves, pale green color overall, stunted growth. In rice: yellow-green stripes parallel to leaf veins. Fix: apply urea (46-0-0) at 30kg/acre, or liquid foliar spray for faster uptake."
                }
                reply = responses.get(sug, "I can help with that! Based on your farm conditions in Kandy, here's my recommendation...")
                st.session_state.messages.append({"role": "bot", "text": reply})
                st.rerun()

    user_input = st.chat_input("Ask about your crops, weather, or farming practices...")
    if user_input:
        st.session_state.messages.append({"role": "user", "text": user_input})
        st.session_state.messages.append({"role": "bot", "text": f"Great question about '{user_input}'! Based on your Kandy farm conditions and current crop stages, I recommend checking soil moisture levels and maintaining consistent irrigation schedules. For more specific advice, please also mention which crop you're asking about."})
        st.rerun()


# ── MARKET PRICES ──
elif page == "📈  Market Prices":
    st.markdown("""
    <div class='main-header'>
        <h1>📈 Market Prices</h1>
        <p>Real-time crop prices from Dambulla, Colombo, and regional markets</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>Today's prices — Dambulla market</div>", unsafe_allow_html=True)

    market_data = [
        ("🍅", "Tomatoes", "Rs 180 / kg", "+12%", True, "High demand this week"),
        ("🧅", "Onions", "Rs 220 / kg", "-5%", False, "Prices easing"),
        ("🌾", "Rice (raw)", "Rs 145 / kg", "+3%", True, "Stable market"),
        ("🌶️", "Green Chilli", "Rs 390 / kg", "+28%", True, "Best time to sell!"),
        ("🥬", "Cabbage", "Rs 65 / kg", "-8%", False, "Oversupply warning"),
        ("🫘", "Beans", "Rs 280 / kg", "+6%", True, "Steady growth"),
    ]

    for icon, name, price, change, up, note in market_data:
        color = "#065f46" if up else "#991b1b"
        bg = "#d1fae5" if up else "#fee2e2"
        arrow = "↑" if up else "↓"
        st.markdown(f"""
        <div style='background: white; border: 1px solid #e0f2e9; border-radius: 14px; padding: 1rem 1.4rem; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.04);'>
            <span style='font-size: 1.6rem;'>{icon}</span>
            <div style='flex: 1;'>
                <div style='font-weight: 600; color: #1a3a2a; font-family: Sora, sans-serif;'>{name}</div>
                <div style='font-size: 0.8rem; color: #6b7280;'>{note}</div>
            </div>
            <div style='text-align: right;'>
                <div style='font-size: 1.05rem; font-weight: 600; color: #1a3a2a;'>{price}</div>
                <div style='font-size: 0.82rem; font-weight: 500; color: {color}; background: {bg}; padding: 2px 8px; border-radius: 6px; display: inline-block;'>{arrow} {change}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>AI price insight</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background: #f0f9f4; border: 1px solid #a7d7b8; border-radius: 14px; padding: 1.2rem 1.5rem;'>
        <div style='font-family: Sora, sans-serif; font-weight: 600; color: #1a3a2a; margin-bottom: 0.6rem;'>💡 This week's recommendation</div>
        <div style='font-size: 0.9rem; color: #2d4a3e; line-height: 1.7;'>
            Green chilli prices are up 28% — highest in 3 months. If you can allocate 0.3–0.5 acres in your next planting cycle, the projected return is <strong>2.3× higher than tomatoes</strong> at current rates.<br><br>
            Onion prices dipping — consider holding your harvest for 1–2 more weeks if storage is available.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── HARVEST PLANNER ──
elif page == "🌾  Harvest Planner":
    st.markdown("""
    <div class='main-header'>
        <h1>🌾 Harvest Planner</h1>
        <p>AI-powered harvest date prediction and yield estimation</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### Plan a new crop")
        crop = st.selectbox("Crop type", ["Tomato", "Rice", "Onion", "Chilli", "Beans"])
        planting_date = st.date_input("Planting date", datetime.date.today())
        area = st.number_input("Field area (acres)", min_value=0.1, max_value=100.0, value=0.5, step=0.1)
        soil = st.selectbox("Soil type", ["Loamy (best)", "Clay", "Sandy", "Red soil"])
        irrigation = st.selectbox("Irrigation", ["Drip (recommended)", "Flood", "Sprinkler", "Rainfed"])

        if st.button("🌱  Predict harvest", use_container_width=True):
            with st.spinner("Calculating..."):
                import time; time.sleep(0.8)
            st.session_state.show_prediction = True
            st.session_state.pred_crop = crop
            st.session_state.pred_area = area
            st.session_state.pred_date = planting_date

    with col2:
        st.markdown("#### Prediction result")
        if st.session_state.get("show_prediction"):
            durations = {"Tomato": 75, "Rice": 120, "Onion": 90, "Chilli": 80, "Beans": 55}
            yields = {"Tomato": 8, "Rice": 3.5, "Onion": 12, "Chilli": 2.5, "Beans": 6}
            crop = st.session_state.pred_crop
            days = durations.get(crop, 80)
            harvest_date = st.session_state.pred_date + datetime.timedelta(days=days)
            yld = yields.get(crop, 5) * st.session_state.pred_area

            st.markdown(f"""
            <div style='background: #f0f9f4; border: 1px solid #a7d7b8; border-radius: 14px; padding: 1.4rem; margin-bottom: 1rem;'>
                <div style='font-family: Sora, sans-serif; font-weight: 600; color: #1a3a2a; font-size: 1.05rem; margin-bottom: 1rem;'>📊 {crop} · {st.session_state.pred_area} acres</div>
                <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem;'>
                    <div style='background: white; border-radius: 10px; padding: 0.9rem; border: 1px solid #c6e8d4;'>
                        <div style='font-size: 0.75rem; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px;'>Harvest date</div>
                        <div style='font-size: 1.1rem; font-weight: 600; color: #1a3a2a; margin-top: 0.3rem;'>{harvest_date.strftime("%d %b %Y")}</div>
                    </div>
                    <div style='background: white; border-radius: 10px; padding: 0.9rem; border: 1px solid #c6e8d4;'>
                        <div style='font-size: 0.75rem; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px;'>Duration</div>
                        <div style='font-size: 1.1rem; font-weight: 600; color: #1a3a2a; margin-top: 0.3rem;'>{days} days</div>
                    </div>
                    <div style='background: white; border-radius: 10px; padding: 0.9rem; border: 1px solid #c6e8d4;'>
                        <div style='font-size: 0.75rem; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px;'>Est. yield</div>
                        <div style='font-size: 1.1rem; font-weight: 600; color: #1a3a2a; margin-top: 0.3rem;'>{yld:.1f} MT</div>
                    </div>
                    <div style='background: white; border-radius: 10px; padding: 0.9rem; border: 1px solid #c6e8d4;'>
                        <div style='font-size: 0.75rem; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px;'>Risk level</div>
                        <div style='font-size: 1.1rem; font-weight: 600; color: #d97706; margin-top: 0.3rem;'>Low ✓</div>
                    </div>
                </div>
                <div style='margin-top: 1rem; font-size: 0.85rem; color: #2d4a3e; padding-top: 0.8rem; border-top: 1px solid #c6e8d4;'>
                    💡 Based on current weather trends and your soil type, expected yield is <strong>above district average</strong>. Maintain consistent irrigation schedule for best results.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='background: #f8fdf9; border: 1px solid #c6e8d4; border-radius: 14px; padding: 3rem; text-align: center; color: #6b9e7a;'>
                <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🌾</div>
                <div style='font-weight: 500; font-family: Sora, sans-serif;'>Fill in your crop details</div>
                <div style='font-size: 0.85rem; margin-top: 0.3rem;'>AI will predict harvest date and yield</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>Active crops timeline</div>", unsafe_allow_html=True)
    today = datetime.date.today()
    for name, planted_offset, total_days, color in [
        ("🍅 Tomatoes", 63, 75, "#1a6b3c"),
        ("🧅 Onions", 49, 90, "#d97706"),
        ("🌾 Rice", 36, 120, "#2563eb"),
    ]:
        planted = today - datetime.timedelta(days=planted_offset)
        harvest = planted + datetime.timedelta(days=total_days)
        days_left = (harvest - today).days
        pct = min(100, int(planted_offset / total_days * 100))
        st.markdown(f"""
        <div style='background: white; border: 1px solid #e0f2e9; border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.5rem;'>
            <div style='display: flex; justify-content: space-between; margin-bottom: 0.5rem;'>
                <span style='font-weight: 600; color: #1a3a2a;'>{name}</span>
                <span style='font-size: 0.82rem; color: #6b7280;'>{days_left} days to harvest</span>
            </div>
            <div class='progress-track'>
                <div style='width: {pct}%; height: 6px; border-radius: 4px; background: {color};'></div>
            </div>
            <div style='display: flex; justify-content: space-between; margin-top: 0.4rem; font-size: 0.78rem; color: #9ca3af;'>
                <span>Planted: {planted.strftime("%d %b")}</span>
                <span>{pct}% complete</span>
                <span>Harvest: {harvest.strftime("%d %b")}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

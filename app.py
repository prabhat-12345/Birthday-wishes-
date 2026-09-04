import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP रोमांटिक सेटिंग (No Scroll)
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="centered")

# 2. एडवांस और लाइटवेट CSS: साइड-बाय-साइड लेआउट, गुलाबी नियॉन पार्टिकल्स और एनिमेटेड कोट्स
custom_css = """
<style>
    /* ऐप का शानदार डार्क रोमांटिक और आलीशान लव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0003 0%, #200005 50%, #3a000a 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
        position: relative;
    }
    
    /* जादुई गुलाबी नियॉन पार्टिकल्स (Romantic Pink Glow) - यह क्रैश नहीं होगा */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(#ff4d94, rgba(255,77,148,.2) 2px, transparent 30px),
            radial-gradient(#ff0055, rgba(255,0,85,.15) 1px, transparent 25px);
        background-size: 300px 350px, 200px 250px;
        animation: pinkFloat 8s linear infinite;
        opacity: 0.5;
        z-index: 1;
    }
    @keyframes pinkFloat {
        from { transform: translateY(0); }
        to { transform: translateY(-350px); }
    }
    
    /* मुख्य कंटेनर मोबाइल स्क्रीन के लिए */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
        position: relative;
        z-index: 10;
    }
    
    /* मुख्य चमकती हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.4rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 0px;
        margin-bottom: 10px;
        background: linear-gradient(to right, #ff0055, #FFD700, #ff80b3, #ff0055);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite;
    }
    
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    /* सबसे ऊपर दिखने वाला जादुई लव संदेश */
    .love-sender-box {
        text-align: center;
        margin-top: 5px;
        margin-bottom: 12px;
        line-height: 1.4;
    }
    .love-name {
        font-family: 'Georgia', serif;
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #FFD700, #ff80b3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(255, 128, 179, 0.6);
        display: inline-block;
    }
    .love-receiver-name {
        font-family: 'Georgia', serif;
        font-size: 2.2rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #ff0055, #ff80b3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 20px #ff0055, 0px 0px 10px #ff80b3;
        display: inline-block;
    }

    /* नया: फोटो के बगल में खाली जगह पर दिखने वाले छोटे रोमांटिक नियॉन वर्ड्स */
    .side-love-text {
        font-family: 'Georgia', serif;
        font-size: 1.2rem;
        font-weight: bold;
        line-height: 1.8;
        text-align: center;
        margin-top: 30px;
        background: linear-gradient(45deg, #ff0055, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textPulse 1.5s ease-in-out infinite alternate;
    }
    
    @keyframes textPulse {
        0% { transform: scale(0.95); filter: drop-shadow(0 0 2px #ff0055); }
        100% { transform: scale(1.05); filter: drop-shadow(0 0 10px #ff0055); }
    }
    
    /* इमेज का नियॉन हार्टबिट फ्रेम जो बाईं तरफ एकदम सही सेट रहेगा */
    .stImage img {
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 85, 0.5) !important;
        box-shadow: 0px 0px 25px #ff0055, 0px 0px 10px #ff80b3 !important;
        animation: romanticFloat 4s ease-in-out infinite;
        max-height: 240px !important;
        width: auto !important;
    }

    /* नीचे का प्रीमियम लव कोट्स बॉक्स */
    .wishes-container {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        padding: 12px;
        margin-top: 15px;
        border: 1px solid rgba(255, 0, 85, 0.15);
        box-shadow: 0px 0px 20px rgba(255, 0, 85, 0.15);
        text-align: center;
    }
    .wish-text {
        font-family: 'Georgia', serif;
        color: #ffffff;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    @keyframes romanticFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. नाम प्रॉम्ट सेटिंग
query_params = st.query_params
sender = query_params.get("name", "PRABHAT")
receiver = query_params.get("to", "LAXMI")

if sender and receiver:
    st.markdown(
        f"""
        <div class="love-sender-box">
            <span class="love-name">🎉 {sender} 🎉</span><br>
            <span style="color: #ff4d94; font-weight: bold;">Wishes Happy Birthday To His Lifeline</span><br>
            <span class="love-receiver-name">💖 {receiver} 💖</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown("<h1 class='main-title'>🎂 Happy Birthday My Love 🎂</h1>", unsafe_allow_html=True)

# 4. फोटो बाईं तरफ रहेगी और दाईं तरफ छोटे-छोटे चमकते हुए लव वर्ड्स एनिमेट होंगे (लाइटवेट, 0% क्रैश चांस)
col1, col2 = st.columns([1.4, 0.8])

with col1:
    # बाईं तरफ लक्ष्मी भाभी की फोटो
    all_files = os.listdir(".")
    found_image = None
    for file in all_files:
        if file.lower().endswith((".jpeg", ".jpg", ".png")):
            found_image = file
            break
    if found_image:
        st.image(found_image, use_container_width=False)

with col2:
    # दाईं तरफ की खाली जगह पर चमकते हुए छोटे लव वर्ड्स
    st.markdown(
        """
        <div class="side-love-text">
            ❤️ I Luv U<br>
            👑 My Queen<br>
            🧸 My Jaan<br>
            💞 जानू 🌹
        </div>
        """, 
        unsafe_allow_html=True
    )

# 5. रोमांटिक विशेज बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">❤️ चेहरे पर आपके रहे हमेशा नूर, खुदा कभी न करे हमसे आपको दूर... <span style="color:#FFD700; font-weight:bold;">Happy Birthday Jaan! 🌹</span></p>
        <p class="wish-text" style="color:#ff80b3;">✨ मेरी दुनिया, मेरी धड़कन, मेरा सब कुछ सिर्फ तुम हो! हर जनम में मुझे सिर्फ तुम्हारा साथ चाहिए... 🥰</p>
    </div>
    """, 
    unsafe_allow_html=True
)

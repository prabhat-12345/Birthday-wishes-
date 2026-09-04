import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP रोमांटिक सेटिंग
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="centered")

# 2. एडवांस CSS: फुल-स्क्रीन नियॉन ग्लो, गिरती गुलाब की पंखुड़ियाँ और साइड-बाय-साइड रोमांटिक एनीमेशन
custom_css = """
<style>
    /* ऐप का शानदार डार्क रोमांटिक और आलीशान लव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0003 0%, #2a0007 50%, #4d004f 100%) !important;
        color: #ffffff;
        position: relative;
    }
    
    /* मुख्य कंटेनर मोबाइल स्क्रीन के लिए */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 480px !important;
        position: relative;
        z-index: 10;
    }

    /* आसमान से धीरे-धीरे गिरने वाली असली गुलाब की पंखुड़ियाँ */
    .rose-petals-container {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        z-index: 1;
        overflow: hidden;
    }
    .rose-petal {
        position: absolute;
        background: linear-gradient(135deg, #ff0055, #990022);
        border-radius: 0 100% 0 100%;
        opacity: 0.8;
        animation: petalFall linear infinite;
        box-shadow: 0 0 8px rgba(255, 0, 85, 0.5);
    }
    .rp1 { left: 10%; width: 12px; height: 18px; animation-duration: 6s; }
    .rp2 { left: 35%; width: 16px; height: 24px; animation-duration: 8s; animation-delay: 2s; }
    .rp3 { left: 55%; width: 10px; height: 15px; animation-duration: 5s; animation-delay: 0.5s; }
    .rp4 { left: 78%; width: 14px; height: 20px; animation-duration: 7s; animation-delay: 3s; }
    .rp5 { left: 92%; width: 18px; height: 26px; animation-duration: 9s; animation-delay: 1s; }

    @keyframes petalFall {
        0% { transform: translateY(-20px) rotate(0deg); opacity: 0; }
        10% { opacity: 0.8; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
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
    .love-text {
        font-family: 'Georgia', serif;
        color: #ff4d94;
        font-size: 1.1rem;
        font-weight: bold;
        letter-spacing: 1px;
        text-shadow: 0px 0px 8px rgba(255, 77, 148, 0.4);
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
        letter-spacing: 2px;
    }
    
    /* मुख्य चमकती हुई बर्थडे हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.4rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 0px;
        margin-bottom: 15px;
        background: linear-gradient(to right, #ff0055, #FFD700, #ff80b3, #ff0055);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite, heartBeatGlow 2s ease-in-out infinite alternate;
    }

    /* नया: फोटो के साइड में दिखने वाले शानदार रोमांटिक नियॉन टेक्स्ट इफेक्ट्स */
    .side-text-left, .side-text-right {
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        font-weight: bold;
        line-height: 1.5;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
        margin-top: 60px;
    }
    .side-text-left {
        background: linear-gradient(45deg, #ff0055, #ff80b3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textPulse 2s ease-in-out infinite alternate;
    }
    .side-text-right {
        background: linear-gradient(45deg, #FFD700, #ffcc00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textPulse 2s ease-in-out infinite alternate-reverse;
    }

    @keyframes textPulse {
        0% { filter: drop-shadow(0 0 2px rgba(255, 0, 85, 0.4)); transform: scale(0.97); }
        100% { filter: drop-shadow(0 0 10px rgba(255, 0, 85, 0.8)); transform: scale(1.03); }
    }
    
    /* इमेज का नियॉन हार्टबिट फ्रेम जो बिल्कुल स्क्रीन के बीच में (Center) लॉक रहेगा */
    .stImage img {
        display: block;
        margin: 0 auto !important;
        max-height: 250px !important;
        width: 100% !important;
        max-width: 200px !important;
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 85, 0.5) !important;
        box-shadow: 0px 0px 25px #ff0055, 0px 0px 10px #ff80b3 !important;
        animation: romanticFloat 4s ease-in-out infinite;
    }

    /* नीचे का प्रीमियम लव कोट्स बॉक्स */
    .wishes-container {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        padding: 15px;
        margin-top: 25px;
        border: 1px solid rgba(255, 0, 85, 0.15);
        box-shadow: 0px 0px 20px rgba(255, 0, 85, 0.15);
        text-align: center;
    }

    .wish-text {
        font-family: 'Georgia', serif;
        color: #ffffff;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 8px;
        background: linear-gradient(to right, #ffffff, #FFD700, #ff80b3, #ffffff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 5s linear infinite;
    }

    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    @keyframes heartBeatGlow {
        0% { filter: drop-shadow(0 0 5px rgba(255, 0, 85, 0.6)); }
        100% { filter: drop-shadow(0 0 18px rgba(255, 215, 0, 0.8)); }
    }
    @keyframes romanticFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. लाइव स्क्रीन पर गुलाब की पंखुड़ियाँ तैराने का ढांचा
st.markdown(
    """
    <div class="rose-petals-container">
        <div class="rose-petal rp1"></div>
        <div class="rose-petal rp2"></div>
        <div class="rose-petal rp3"></div>
        <div class="rose-petal rp4"></div>
        <div class="rose-petal rp5"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# 4. नाम प्रॉम्ट सेटिंग
query_params = st.query_params
sender = query_params.get("name", "PRABHAT")
receiver = query_params.get("to", "LAXMI")

if sender and receiver:
    st.markdown(
        f"""
        <div class="love-sender-box">
            <span class="love-name">🎉 {sender} 🎉</span><br>
            <span class="love-text">Wishes Happy Birthday To His Lifeline</span><br>
            <span class="love-receiver-name">💖 {receiver} 💖</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown("<h1 class='main-title'>🎂 Happy Birthday My Love 🎂</h1>", unsafe_allow_html=True)

# 5. जादुई 3-कॉलम लेआउट: फ़ोटो बीच में और दोनों तरफ शानदार एनीमेशन टेक्स्ट
col1, col2, col3 = st.columns([1, 1.8, 1])

with col1:
    # बाएँ हाथ का रोमांटिक एनिमेटेड टेक्स्ट
    st.markdown('<div class="side-text-left">❤️<br>तुम<br>मेरी<br>जान<br>हो</div>', unsafe_allow_html=True)

with col2:
    # बिल्कुल बीच में आप दोनों की सुंदर फ़ोटो
    image_path = "images (52).jpeg"
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=False)
    else:
        st.warning("कृपया पेज को एक बार रिफ्रेश करें।")

with col3:
    # दाएँ हाथ का रोमांटिक एनिमेटेड टेक्स्ट
    st.markdown('<div class="side-text-right">🌹<br>मेरा<br>सब<br>कुछ<br>तुम</div>', unsafe_allow_html=True)

# 6. रोमांटिक विशेज बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">❤️ चेहरे पर आपके रहे हमेशा नूर, खुदा कभी न करे हमसे आपको दूर... <span style="font-weight:bold; color:#FFD700;">Happy Birthday Jaan! 🌹</span></p>
        <p class="wish-text">✨ मेरी दुनिया, मेरी धड़कन, मेरा सब कुछ सिर्फ तुम हो! हर जनम में मुझे सिर्फ तुम्हारा साथ चाहिए... <span style="font-weight:bold; color:#FFD700;">I Love You So Much! 🏹</span></p>
    </div>
    """, 
    unsafe_allow_html=True
)

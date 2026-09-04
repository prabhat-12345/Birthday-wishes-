import streamlit as st
import base64
import os

# 1. पेज की पूरी प्रीमियम VLVIP रोमांटिक सेटिंग (मोबाइल स्क्रीन पर स्क्रॉल बार छिपाने के लिए)
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="centered")

# 2. एडवांस CSS: परफेक्ट सेंटर फोटो, चमकती हेडिंग और 100% लाइव असली गुलाब की पंखुड़ियों की बारिश
custom_css = """
<style>
    /* ऐप का शानदार डार्क रोमांटिक और आलीशान लव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0003 0%, #2a0007 50%, #4d004f 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
        position: relative;
    }
    
    /* मुख्य कंटेनर को मोबाइल स्क्रीन की हाइट में फिट करने के लिए */
    .block-container {
        padding-top: 2.2rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
        position: relative;
        z-index: 10;
    }
    
    /* जादू 1: असली लाल गुलाब की पंखुड़ियाँ जो 100% लाइव गिरेंगी */
    .rose-leaves-falling {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        z-index: 999;
        overflow: hidden;
    }
    .single-petal {
        position: absolute;
        background: linear-gradient(135deg, #ff0055, #b3003b);
        border-radius: 0 100% 0 100%;
        opacity: 0.85;
        animation: leafDrop linear infinite;
        box-shadow: 0 0 8px rgba(255, 0, 85, 0.6);
    }
    .leaf1 { left: 10%; width: 14px; height: 20px; animation-duration: 6s; animation-delay: 0s; }
    .leaf2 { left: 35%; width: 18px; height: 26px; animation-duration: 8s; animation-delay: 1.5s; }
    .leaf3 { left: 55%; width: 12px; height: 18px; animation-duration: 5.5s; animation-delay: 0.3s; }
    .leaf4 { left: 75%; width: 16px; height: 22px; animation-duration: 7s; animation-delay: 2.2s; }
    .leaf5 { left: 90%; width: 19px; height: 28px; animation-duration: 8.5s; animation-delay: 0.8s; }

    @keyframes leafDrop {
        0% { transform: translateY(-30px) rotate(0deg) translateX(0px); opacity: 0; }
        10% { opacity: 0.9; }
        90% { opacity: 0.9; }
        100% { transform: translateY(100vh) rotate(450deg) translateX(30px); opacity: 0; }
    }
    
    /* मुख्य चमकती हुई बर्थडे हेडिंग */
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
        animation: textShine 4s linear infinite, heartBeatGlow 2s ease-in-out infinite alternate;
    }
    
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    @keyframes heartBeatGlow {
        0% { filter: drop-shadow(0 0 5px rgba(255, 0, 85, 0.6)); transform: scale(1); }
        100% { filter: drop-shadow(0 0 18px rgba(255, 215, 0, 0.8)); transform: scale(1.02); }
    }

    /* भेजने वाले और पाने वाले का नाम */
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

    /* फोटो के ऊपर और नीचे चमकने वाले शानदार रोमांटिक नियॉन टेक्स्ट बॉक्स */
    .romantic-badge {
        font-family: 'Georgia', serif;
        font-size: 1.25rem;
        font-weight: bold;
        text-align: center;
        margin: 10px auto;
        padding: 5px 15px;
        border-radius: 50px;
        background: rgba(255, 0, 85, 0.1);
        border: 1px solid rgba(255, 0, 85, 0.3);
        width: fit-content;
        animation: textPulse 2s ease-in-out infinite alternate;
    }
    .badge-left { color: #ff0055; text-shadow: 0 0 8px #ff0055; }
    .badge-right { color: #FFD700; text-shadow: 0 0 8px #FFD700; }

    @keyframes textPulse {
        0% { transform: scale(0.96); box-shadow: 0 0 5px rgba(255, 0, 85, 0.2); }
        100% { transform: scale(1.04); box-shadow: 0 0 15px rgba(255, 0, 85, 0.5); }
    }
    
    /* ब्रह्मांड का सबसे शक्तिशाली सेंटर फोटो फॉर्मूला (HTML Container) */
    .photo-center-holder {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin: 15px 0 !important;
    }
    .photo-center-holder img {
        max-height: 260px !important;
        width: auto !important;
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 85, 0.5) !important;
        box-shadow: 0px 0px 25px #ff0055, 0px 0px 10px #ff80b3 !important;
        animation: romanticFloat 4s ease-in-out infinite;
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
        margin-bottom: 8px;
        background: linear-gradient(to right, #ffffff, #FFD700, #ff80b3, #ffffff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 5s linear infinite;
    }
    
    .wish-highlight {
        font-weight: bold;
        background: linear-gradient(to right, #ff0055, #FFD700, #ff0055);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 3s linear infinite;
    }

    @keyframes romanticFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. HTML लेआउट जो स्क्रीन पर गुलाब की पंखुड़ियाँ लगातार लाइव तैराएगा
st.markdown(
    """
    <div class="rose-leaves-falling">
        <div class="single-petal leaf1"></div>
        <div class="single-petal leaf2"></div>
        <div class="single-petal leaf3"></div>
        <div class="single-petal leaf4"></div>
        <div class="single-petal leaf5"></div>
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

st.markdown('<div class="romantic-badge badge-left">❤️ तुम मेरी जान हो 🌹</div>', unsafe_allow_html=True)

# 5. ऑटो-इमेज स्कैनर और HTML जादुई बेस64 कनवर्टर (ताकि फोटो 100% सेंटर में रेंडर हो)
all_files = os.listdir(".")
found_image = None

for file in all_files:
    if file.lower().endswith((".jpeg", ".jpg", ".png")):
        found_image = file
        break

if found_image:
    with open(found_image, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    
    # शुद्ध HTML टैग से फोटो को स्क्रीन के 100% सेंटर (बीचों-बीच) में लॉक करना
    st.markdown(
        f"""
        <div class="photo-center-holder">
            <img src="data:image/jpeg;base64,{b64_string}" alt="Laxmi Bhabhi">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("फोटो फोल्डर में नहीं मिल सकी।")

st.markdown('<div class="romantic-badge badge-right">💞 मेरा सब कुछ तुम हो 🧸</div>', unsafe_allow_html=True)

# 6. रोमांटिक विशेज बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">❤️ चेहरे पर आपके रहे हमेशा नूर, खुदा कभी न करे हमसे आपको दूर... <span class="wish-highlight">Happy Birthday Jaan! 🌹</span></p>
        <p class="wish-text">✨ मेरी दुनिया, मेरी धड़कन, मेरा सब कुछ सिर्फ तुम हो! हर जनम में मुझे सिर्फ तुम्हारा साथ चाहिए... <span class="wish-highlight">I Love You So Much! 🏹</span></p>
    </div>
    """, 
    unsafe_allow_html=True
)

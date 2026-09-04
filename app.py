import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP रोमांटिक सेटिंग (मोबाइल स्क्रीन पर स्क्रॉल बार छिपाने के लिए)
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="centered")

# 2. एडवांस CSS: लाइटवेट नियॉन ग्लो, परफेक्ट सेंटर फोटो और एनिमेटेड लव कोट्स
custom_css = """
<style>
    /* ऐप का शानदार डार्क रोमांटिक और आलीशान लव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0003 0%, #2a0007 50%, #4d004f 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
    }
    
    /* मुख्य कंटेनर को मोबाइल स्क्रीन की हाइट में फिट करने के लिए */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
    }
    
    /* मुख्य चमकती और धीरे-धीरे धड़कने वाली बर्थडे हेडिंग */
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

    /* जिसने भेजा है उसका नाम दिखाने के लिए VIP शाइनिंग स्टाइल */
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
    .badge-left {
        color: #ff0055;
        text-shadow: 0 0 8px #ff0055;
    }
    .badge-right {
        color: #FFD700;
        text-shadow: 0 0 8px #FFD700;
    }

    @keyframes textPulse {
        0% { transform: scale(0.96); box-shadow: 0 0 5px rgba(255, 0, 85, 0.2); }
        100% { transform: scale(1.04); box-shadow: 0 0 15px rgba(255, 0, 85, 0.5); }
    }
    
    /* इमेज का नियॉन हार्टबिट फ्रेम जो बिल्कुल स्क्रीन के बीच में (Center) लॉक रहेगा */
    .stImage img {
        display: block;
        margin: 0 auto !important;
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

# 3. जादुई नाम बदलने वाला कोड (URL Parameters)
query_params = st.query_params
sender = query_params.get("name", "PRABHAT")
receiver = query_params.get("to", "LAXMI")

# 4. सबसे ऊपर रोमांटिक अंदाज में नाम चमकेगा
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

# 5. मुख्य एनिमेटेड हेडिंग
st.markdown("<h1 class='main-title'>🎂 Happy Birthday My Love 🎂</h1>", unsafe_allow_html=True)

# 6. फोटो के ऊपर चमकने वाला पहला रोमांटिक नियॉन टेक्स्ट बॉक्स
st.markdown('<div class="romantic-badge badge-left">❤️ तुम मेरी जान हो 🌹</div>', unsafe_allow_html=True)

# 7. जादू: फोल्डर में मौजूद किसी भी इमेज को ऑटोमैटिक स्कैन करके बिल्कुल बीच में लोड करना
all_files = os.listdir(".")
found_image = None

for file in all_files:
    if file.lower().endswith((".jpeg", ".jpg", ".png")):
        found_image = file
        break

if found_image:
    st.image(found_image, use_container_width=False)
else:
    st.error("फोटो फोल्डर में नहीं मिल सकी।")

# 8. फोटो के नीचे चमकने वाला दूसरा रोमांटिक नियॉन टेक्स्ट बॉक्स
st.markdown('<div class="romantic-badge badge-right">💞 मेरा सब कुछ तुम हो 🧸</div>', unsafe_allow_html=True)

# 9. रोमांटिक विशेज बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">❤️ चेहरे पर आपके रहे हमेशा नूर, खुदा कभी न करे हमसे आपको दूर... <span class="wish-highlight">Happy Birthday Jaan! 🌹</span></p>
        <p class="wish-text">✨ मेरी दुनिया, मेरी धड़कन, मेरा सब कुछ सिर्फ तुम हो! हर जनम में मुझे सिर्फ तुम्हारा साथ चाहिए... <span class="wish-highlight">I Love You So Much! 🏹</span></p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 10. आसमान से सितारों और बर्फ की जादुई बारिश (100% सुरक्षित और क्रैश-फ्री)
st.snow()

import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP रोमांटिक सेटिंग (No Scroll)
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="centered")

# 2. पूरी तरह ऑप्टिमाइज्ड लाइटवेट CSS (फोटो के बगल की खाली जगह को भरने के लिए)
custom_css = """
<style>
    /* ऐप का शानदार डार्क रोमांटिक बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0003 0%, #2a0007 50%, #4d004f 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
    }
    
    /* मुख्य कंटेनर मोबाइल स्क्रीन के लिए */
    .block-container {
        padding-top: 2.2rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
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
    }
    .badge-left { color: #ff0055; text-shadow: 0 0 8px #ff0055; }
    .badge-right { color: #FFD700; text-shadow: 0 0 8px #FFD700; }
    
    /* इमेज का नियॉन हार्टबिट फ्रेम जो बिल्कुल सही सेट रहेगा */
    .stImage {
        position: relative;
    }
    .stImage img {
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 85, 0.5) !important;
        box-shadow: 0px 0px 25px #ff0055, 0px 0px 10px #ff80b3 !important;
        animation: romanticFloat 4s ease-in-out infinite;
        max-height: 240px !important;
        width: auto !important;
    }

    /* जादू: बिना कॉलम के सीधे HTML फॉर्मूले से फोटो के दाईं तरफ की खाली जगह को पूरी तरह भरना */
    .stImage::after {
        content: "❤️ LOVE ❤️\\A 🌹 JAAN 🌹\\A 👑 QUEEN 👑\\A 🧸 MY LIFE 🧸";
        white-space: pre-wrap;
        position: absolute;
        top: 20px;
        right: -130px; /* खाली जगह को पूरी तरह कवर करने के लिए पोजीशन फिक्स */
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        font-weight: bold;
        line-height: 2.2; /* लाइनों के बीच सही गैप */
        text-align: center;
        background: linear-gradient(45deg, #ff0055, #FFD700, #ff0055);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: sideTextPulse 1.5s ease-in-out infinite alternate, textShine 4s linear infinite;
    }

    @keyframes sideTextPulse {
        0% { transform: scale(0.98); filter: drop-shadow(0 0 2px #ff0055); }
        100% { transform: scale(1.02); filter: drop-shadow(0 0 12px #ff0055); }
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

st.markdown('<div class="romantic-badge badge-left">❤️ तुम मेरी जान हो 🌹</div>', unsafe_allow_html=True)

# 4. फोटो लोड होना (यह अपनी जगह पर रहेगी, और दाईं तरफ की पूरी खाली जगह सुंदर डिज़ाइन से भर जाएगी)
all_files = os.listdir(".")
found_image = None
for file in all_files:
    if file.lower().endswith((".jpeg", ".jpg", ".png")):
        found_image = file
        break
if found_image:
    st.image(found_image, use_container_width=False)

st.markdown('<div class="romantic-badge badge-right">💞 मेरा सब कुछ तुम हो 🧸</div>', unsafe_allow_html=True)

# 5. रोमांटिक विशेज बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">❤️ चेहरे पर आपके रहे हमेशा नूर, खुदा कभी न करे हमसे आपको दूर... <span style="color:#FFD700; font-weight:bold;">Happy Birthday Jaan! 🌹</span></p>
        <p class="wish-text" style="color:#ff80b3;">✨ मेरी दुनिया, मेरी धड़कन,  मेरा सब कुछ सिर्फ तुम हो! हर जनम में मुझे सिर्फ तुम्हारा साथ चाहिए... 🥰</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 6. पुराना नॉर्मल सेफ स्नोफॉल (क्रैश-फ्री)
st.snow()

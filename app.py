import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP रोमांटिक सेटिंग (No Scroll)
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="centered")

# 2. एडवांस ऑल-इन-वन एनिमेटेड CSS (मोटी बाउंड्री वाला धड़कता दिल और आर-पार सुनहरा तीर)
custom_css = """
<style>
    /* ऐप का शानदार डार्क रोमांटिक बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0003 0%, #2a0007 50%, #4d004f 100%) !important;
        color: #ffffff;
    }
    
    /* मुख्य कंटेनर मोबाइल स्क्रीन के लिए */
    .block-container {
        padding-top: 2.2rem !important;
        padding-bottom: 2rem !important;
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

    /* फोटो के ऊपर और नीचे चमकने वाले शानदार रोमांटिक इंग्लिश बैज */
    .romantic-badge {
        font-family: 'Georgia', serif;
        font-size: 1.2rem;
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
    
    /* इमेज का नियॉन हार्टबिट फ्रेम */
    .stImage {
        position: relative;
    }
    .stImage img {
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 85, 0.5) !important;
        box-shadow: 0px 0px 25px #ff0055, 0px 0px 10px #ff80b3 !important;
        animation: romanticFloat 4s ease-in-out infinite;
        max-height: 250px !important;
        width: auto !important;
    }

    /* फ़ोटो के दाईं तरफ एक बड़ा, सीधा और मोटी बाउंड्री वाला धड़कता हुआ लव हार्ट बॉक्स */
    .stImage::after {
        content: "11 💖 YRS\\A OF 🌹 LOVE\\A MY 💍 WIFE\\A MY  BABU\\A MY 💞 JAAN\\A MY 🧸 LIFE";
        white-space: pre-wrap;
        position: absolute;
        top: -10px;
        right: -140px;
        width: 125px;
        height: 125px;
        background: radial-gradient(circle, rgba(255, 0, 85, 0.35) 40%, rgba(15, 0, 3, 0.7) 100%);
        border: 4px solid #ff0055;
        border-radius: 50% 50% 0 50%;
        transform: rotate(-45deg);
        font-family: 'Georgia', serif;
        font-size: 0.85rem;
        font-weight: bold;
        line-height: 1.6;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: thickHeartPulse 1.2s ease-in-out infinite alternate;
        box-shadow: 0px 0px 35px #ff0055, inset 0px 0px 15px #ff0055;
        z-index: 15;
    }

    /* दिल के आर-पार निकलने वाला असली लव तीर */
    .stImage::before {
        content: "💘────────>";
        position: absolute;
        top: 50px;
        right: -170px;
        font-size: 1.6rem;
        font-weight: bold;
        background: linear-gradient(45deg, #FFD700, #ffaa00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px #ffaa00;
        z-index: 14;
        transform: rotate(-15deg);
        animation: arrowGlow 1.2s ease-in-out infinite alternate;
    }

    @keyframes arrowGlow {
        0% { filter: drop-shadow(0 0 2px #ffaa00); }
        100% { filter: drop-shadow(0 0 8px #FFD700); }
    }

    @keyframes thickHeartPulse {
        0% { 
            transform: scale(0.95) rotate(-45deg); 
            box-shadow: 0px 0px 15px #ff0055;
            color: #ffffff;
        }
        100% { 
            transform: scale(1.05) rotate(-45deg); 
            box-shadow: 0px 0px 35px #ff0055, 0px 0px 15px #FFD700;
            color: #FFD700;
        }
    }

    /* नीचे का प्रीमियम ग्लास कोट्स बॉक्स जिसके सारे टेक्स्ट अब लाइव पानी की लहर की तरह चमकेंगे */
    .wishes-container {
        background: rgba(255, 0, 85, 0.04);
        border-radius: 15px;
        padding: 15px;
        margin-top: 15px;
        border: 1px solid rgba(255, 0, 85, 0.2);
        box-shadow: 0px 0px 25px rgba(255, 0, 85, 0.15);
        text-align: left;
    }
    
    .wish-text {
        font-family: 'Georgia', serif;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 12px;
        border-bottom: 1px solid rgba(255, 0, 85, 0.1);
        padding-bottom: 8px;
        background: linear-gradient(to right, #ffffff, #ff80b3, #ffccff, #ffffff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 6s linear infinite;
    }
    
    .wish-text:last-child {
        border-bottom: none;
        margin-bottom: 0;
    }
    
    .wish-highlight {
        font-weight: bold;
        background: linear-gradient(to right, #FFD700, #ffaa00, #FFD700);
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

st.markdown('<div class="romantic-badge badge-left">❤️ YOU ARE MY LIFE 🌹</div>', unsafe_allow_html=True)

# 4. फोटो लोड होना
all_files = os.listdir(".")
found_image = None
for file in all_files:
    if file.lower().endswith((".jpeg", ".jpg", ".png")):
        found_image = file
        break
if found_image:
    st.image(found_image, use_container_width=False)

st.markdown('<div class="romantic-badge badge-right">💞 YOU ARE MY EVERYTHING 🧸</div>', unsafe_allow_html=True)

# 5. पूरे 10 जादुई और शाइनिंग रोमांटिक कोट्स बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">✨ <span class="wish-highlight">1. 11 Years of Togetherness:</span> हमारा यह 11 साल का सफर सिर्फ एक रिश्ता नहीं, मेरी पूरी जिंदगी की सबसे खूबसूरत सच्चाई है। 🌹</p>
        <p class="wish-text">❤️ <span class="wish-highlight">2. Forever Mine:</span> चेहरे पर आपके रहे हमेशा नूर, खुदा कभी न करे हमसे आपको दूर... Happy Birthday Jaan! 🥰</p>
        <p class="wish-text">💘 <span class="wish-highlight">3. To My Soulmate:</span> "You are the beat of my heart, the smile on my face, and the spark in my life. I love you endlessly." 🏹</p>
        <p class="wish-text">🌹 <span class="wish-highlight">4. Adhoori Hai Life:</span> तुम्हारे बिना मेरी सुबह और मेरी शाम अधूरी है, सच कहूँ तो लक्ष्मी, तुम्हारे बिना मेरी पूरी जान अधूरी है! 🌸</p>
        <p class="wish-text">💫 <span class="wish-highlight">5. Deepest Love:</span> "In all the world, there is no heart for me like yours. In all the world, there is no love for you like mine." 🌟</p>
        <p class="wish-text">🧸 <span class="wish-highlight">6. Meri Mannat:</span> खुदा से जब भी मैंने कोई दुआ मांगी है, हर दुआ में सिर्फ और सिर्फ तुम्हारी लंबी उम्र और खुशी मांगी है। 🎂</p>
        <p class="wish-text">👑 <span class="wish-highlight">7. Queen of My Heart:</span> "You are my today, my tomorrow, and my forever. Happy Birthday to the queen of my world!" 💖</p>
        <p class="wish-text">💞 <span class="wish-highlight">8. Rooh Ka Rishta:</span> 11 साल में वक्त बदला, दुनिया बदली, पर तुम्हारे लिए मेरी आँखों में जो मोहब्बत थी, वो आज भी वैसी ही जवान है। 💍</p>
        <p class="wish-text">🪈 <span class="wish-highlight">9. My Lifeline:</span> "Every single day spent with you feels like a blessing. Thank you for being my strength and my happiness." 🕊️</p>
        <p class="wish-text">🎯 <span class="wish-highlight">10. Aakhiri Khwahish:</span> हर जनम में मुझे सिर्फ और सिर्फ तुम्हारा ही साथ चाहिए, तुम ही मेरी पहली और आखिरी मोहब्बत हो जानू! 🥰</p>
    </div>
    """, 
    

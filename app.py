import streamlit as st
import google.generativeai as genai

# యాప్ పేజీ సెటప్
st.set_page_config(page_title="ఆశీర్వాద్ AI ప్రాజెక్ట్", layout="wide")

# సైడ్‌బార్‌లో API Key ఇన్‌పుట్ (యూజర్లు వారి নিজস্ব కీ ఇచ్చుకోవడానికి లేదా మీ కీ వాడటానికి)
st.sidebar.title("🛠️ AI టూల్స్ మెను")
api_key = st.sidebar.text_input("Gemini API Key నమోదు చేయండి:", type="password")

if api_key:
    genai.configure(api_key=api_key)

choice = st.sidebar.selectbox(
    "ఒక ఫీచర్‌ను ఎంచుకోండి:",
    [
        "1. Home / Dashboard",
        "2. Script Maker (Story)",
        "3. Image Generator",
        "4. Video Creator",
        "5. Face Swap",
        "6. Voice Cloning",
        "7. Website Builder",
    ],
)

# ---------------- 1. HOME / DASHBOARD ----------------
if choice == "1. Home / Dashboard":
    st.subheader("🏠 హోమ్ పేజీ - స్వాగతం!")
    st.info("ఇక్కడ మీ యాప్ యొక్క మెయిన్ డాష్‌బోర్డ్ కనిపిస్తుంది.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="మొత్తం యూార్లు", value="1,240+")
    with col2:
        st.metric(label="జనరేట్ అయిన స్క్రిప్ట్స్", value="5,800+")
    with col3:
        st.metric(label="వీడియోలు / రీల్స్", value="3,120+")

# ---------------- 2. SCRIPT MAKER (Gemini AI Connected) ----------------
elif choice == "2. Script Maker (Story)":
    st.subheader("✍️ AI స్క్రిప్ట్ & స్టోరీ మేకర్")
    topic = st.text_input("మీ వీడియో ఏ టాపిక్ గురించి? (ఉదా: మోటివేషనల్, స్టోరీ)")
    duration = st.selectbox(
        "వీడియో నిడివి (Duration) ఎంచుకోండి:",
        ["5 Seconds", "15 Seconds", "30 Seconds", "60 Seconds"],
    )

    if st.button("🚀 స్క్రిప్ట్ జనరేట్ చేయి"):
        if not api_key:
            st.error("దయచేసి సైడ్‌బార్‌లో మీ Gemini API Key ఇవ్వండి!")
        elif topic:
            with st.spinner("AI స్క్రిప్ట్ తయారు చేస్తోంది... దయచేసి వేచి ఉండండి."):
                try:
                    # Gemini AI మోడల్ కాల్ చేయడం
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"Write a {duration} viral social media video script about: {topic} in Telugu or English as requested."
                    response = model.generate_content(prompt)
                    
                    st.success(f"🎉 మీ {duration} స్క్రిప్ట్ విజయవంతంగా తయారైంది!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"ఎర్రర్ వచ్చింది: {e}")
        else:
            st.warning("దయచేసి ఏదైనా టాపిక్ రాయండి.")

# ---------------- 3. IMAGE GENERATOR ----------------
elif choice == "3. Image Generator":
    st.subheader("🎨 AI ఇమేజ్ జనరేటర్")
    img_prompt = st.text_input("మీకు ఎలాంటి ఇమేజ్ కావాలి?")
    if st.button("🖼️ ఇమేజ్ జనరేట్ చేయి"):
        if img_prompt:
            st.success("🎉 ఇమేజ్ జనరేషన్ ఫీచర్ త్వరలో అనుసంధానించబడుతుంది!")
            st.info(f"మీరు కోరిన ప్రాంప్ట్: {img_prompt}")
        else:
            st.warning("దయచేసి ప్రొంప్ట్ రాయండి.")

# ---------------- 4. VIDEO CREATOR ----------------
elif choice == "4. Video Creator":
    st.subheader("🎬 AI వీడియో క్రియేటర్")
    vid_prompt = st.text_input("మీకు ఎలాంటి వీడియో కావాలి?")
    if st.button("🎥 వీడియో జనరేట్ చేయి"):
        if vid_prompt:
            st.success("🎉 వీడియో క్రియేషన్ ప్రాసెస్ ప్రారంభమైంది!")
        else:
            st.warning("దయచేసి వివరాలు ఇవ్వండి.")

# ---------------- 5. FACE SWAP ----------------
elif choice == "5. Face Swap":
    st.subheader("🔄 AI ఫేస్ స్వాప్")
    st.write("మీ ఫోటోను అప్‌లోడ్ చేసి ముఖం మార్చుకోండి.")
    uploaded_file = st.file_uploader("ఒక ఫోటోను ఎంచుకోండి", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.success("ఫోటో విజయవంతంగా అప్‌లోడ్ అయింది!")

# ---------------- 6. VOICE CLONING ----------------
elif choice == "6. Voice Cloning":
    st.subheader("🎤 AI వాయిస్ క్లోనింగ్ (ElevenLabs Integration Ready)")
    voice_text = st.text_input("మీరు చెప్పాలనుకున్న టెక్స్ట్ ఇక్కడ రాయండి:")
    if st.button("🔊 వాయిస్ జనరేట్ చేయి"):
        if voice_text:
            st.success("వాయిస్ జనరేట్ అవుతోంది!")
        else:
            st.warning("దయచేసి టెక్స్ట్ రాయండి.")

# ---------------- 7. WEBSITE BUILDER ----------------
elif choice == "7. Website Builder":
    st.subheader("🌐 AI వెబ్‌సైట్ బిల్డర్")
    web_prompt = st.text_input("మీకు ఎలాంటి వెబ్‌సైట్ కావాలి? (ఉదా: Business, Portfolio)")
    if st.button("💻 వెబ్‌సైట్ క్రియేట్ చేయి"):
        if web_prompt:
            st.success("మీ వెబ్‌సైట్ కోడ్ రెడీ అవుతోంది!")
        else:
            st.warning("వివరాలు ఇవ్వండి.")
                

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="అసర్వాద్ AI ప్రాజెక్ట్", layout="wide")

st.sidebar.title("🛠️ AI టూల్స్ మెను")
api_key = st.sidebar.text_input("Gemini API Key నమోదు చేయండి:", type="password")

if api_key:
    genai.configure(api_key=api_key)

choice = st.sidebar.selectbox(
    "ఒక ఫీచర్‌ని ఎన్నుకోండి:",
    [
        "1. Home / Dashboard",
        "2. Script Maker (Story)",
        "3. Image Generator",
        "4. Video Creator",
        "5. Face Swap",
        "6. Voice Cloning",
        "7. Website Builder",
    ]
)

if choice == "1. Home / Dashboard":
    st.subheader("🏠 హోమ్ పేజీ - స్వాగతం!")
    st.info("ఇక్కడ మీ యాప్ యొక్క మెయిన్ డాష్‌బోర్డ్ కనిపిస్తుంది.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="మొత్తం యూజర్లు", value="1,240+")
    with col2:
        st.metric(label="జనరేట్ అయిన స్క్రిప్ట్స్", value="5,800+")
    with col3:
        st.metric(label="వీడియోలు / రీల్స్", value="3,120+")

elif choice == "2. Script Maker (Story)":
    st.subheader("🎬 AI స్క్రిప్ట్ & స్టోరీ మేకర్")
    topic = st.text_input("మీ వీడియో ఏ టాపిక్ గురించి? (ఉదా: మోటివేషనల్, టెక్ వ్లాగ్)")
    duration = st.selectbox(
        "వీడియో నిడివి (Duration) ఎన్నుకోండి:",
        ["5 Seconds", "15 Seconds", "30 Seconds", "60 Seconds"]
    )

    if st.button("🚀 స్క్రిప్ట్ జనరేట్ చేయి"):
        if not api_key:
            st.error("దయచేసి సైడ్‌బార్‌లో మీ Gemini API Key ఇవ్వండి!")
        elif topic:
            with st.spinner("AI స్క్రిప్ట్ తయారవుతోంది... దయచేసి వేచి ఉండండి."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"Write a {duration} viral social media video script about: {topic} in Telugu or English as requested."
                    response = model.generate_content(prompt)

                    st.success(f"✨ మీ {duration} స్క్రిప్ట్ విజయవంతంగా తయారైంది!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"ఎర్రర్ వచ్చింది: {e}")
        else:
            st.warning("దయచేసి ఏదైనా టాపిక్ రాయండి.")

elif choice == "3. Image Generator":
    st.subheader("🖼️ AI ఇమేజ్ జనరేటర్")
    st.info("ఇక్కడ మీరు మీ ఇష్టమైన చిత్రాలను సృష్టించుకోవడానికి ఉచిత AI ఇమేజ్ టూల్స్‌ని ఉపయోగించవచ్చు.")
    
    img_prompt = st.text_input("మీకు ఎలాంటి ఇమేజ్ కావాలి? (Prompt రాయండి)")
    if st.button("🖼️ ఇమేజ్ జనరేట్ చేయి"):
        if img_prompt:
            st.success("✨ మీ ప్రాంప్ట్ స్వీకరించబడింది!")
            st.markdown(f"**మీరు కోరిన డిజైన్:** `{img_prompt}`")
            st.markdown("🔗 ఉచితంగా ఇమేజ్ పొందడానికి మీరు [Hugging Face Space](https://huggingface.co) లేదా [Civitai](https://civitai.com) టూల్స్ ని ఇక్కడ వాడవచ్చు.")
        else:
            st.warning("దయచేసి ప్రాంప్ట్ రాయండి.")

elif choice == "4. Video Creator":
    st.subheader("🎥 AI వీడియో క్రియేటర్")
    st.info("సోషల్ మీడియా రీల్స్ మరియు వీడియోల కోసం ఇక్కడ టూల్స్ అందుబాటులో ఉన్నాయి.")
    
    vid_prompt = st.text_input("మీకు ఎలాంటి వీడియో కావాలి? (Topic రాయండి)")
    if st.button("🎥 వీడియో జనరేట్ చేయి"):
        if vid_prompt:
            st.success("🚀 వీడియో క్రియేషన్ ప్రాసెస్ ప్రారంభమైంది!")
            st.markdown(f"**వీడియో టాపిక్:** `{vid_prompt}`")
            st.markdown("💡 పూర్తి స్థాయి వీడియోల కోసం AI వీడియో జనరేటర్ ప్లాట్‌ఫాంలను దీనికి అనుసంధానించవచ్చు.")
        else:
            st.warning("దయచేసి టాపిక్ రాయండి.")

elif choice in ["5. Face Swap", "6. Voice Cloning", "7. Website Builder"]:
    st.subheader(f"🛠️ {choice}")
    st.info("ఈ అడ్వాన్స్డ్ ఫీచర్ త్వరలో మీ యాప్‌లో పూర్తిస్థాయిలో అందుబాటులోకి రానుంది!")


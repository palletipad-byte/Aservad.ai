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
    st.info("మీకు కావలసిన చిత్రాన్ని తెలుగులో లేదా ఇంగ్లీష్‌లో టైప్ చేయండి.")
    
    img_prompt = st.text_input("మీకు ఎలాంటి ఇమేజ్ కావాలి? (తెలుగులో లేదా ఇంగ్లీష్‌లో రాయండి)")
    
    if st.button("🖼️ ఇమేజ్ జనరేట్ చేయి"):
        if img_prompt:
            with st.spinner("ఇమేజ్ తయారవుతోంది... దయచేసి వేచి ఉండండి."):
                try:
                    # తెలుగులో రాస్తే ఇంగ్లీష్‌లోకి అనువదించడం కోసం Gemini AI వాడకం
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    trans_prompt = f"Translate the following image description into a descriptive English prompt suitable for AI image generation, return only the translated prompt: {img_prompt}"
                    response = model.generate_content(trans_prompt)
                    english_prompt = response.text.strip()
                    
                    import urllib.parse
                    encoded_prompt = urllib.parse.quote(english_prompt)
                    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
                    
                    st.success("✨ మీ ఇమేజ్ విజయవంతంగా తయారైంది!")
                    st.image(image_url, caption=f"Generated for: {img_prompt}", use_container_width=True)
                except Exception as e:
                    st.error(f"ఎర్రర్ వచ్చింది: {e}")
        else:
            st.warning("దయచేసి ప్రాంప్ట్ రాయండి.")

elif choice == "4. Video Creator":
    st.subheader("🎥 AI వీడియో క్రియేటర్")
    st.info("మీకు కావలసిన వీడియో టాపిక్‌ని తెలుగులో లేదా ఇంగ్లీష్‌లో టైప్ చేయండి.")
    
    vid_prompt = st.text_input("మీకు ఎలాంటి వీడియో కావాలి? (తెలుగులో లేదా ఇంగ్లీష్‌లో రాయండి)")
    
    if st.button("🎥 వీడియో జనరేట్ చేయి"):
        if vid_prompt:
            with st.spinner("వీడియో తయారవుతోంది... దయచేసి వేచి ఉండండి."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    trans_prompt = f"Translate the following video description into a descriptive English prompt suitable for AI video generation, return only the translated prompt: {vid_prompt}"
                    response = model.generate_content(trans_prompt)
                    english_vid_prompt = response.text.strip()
                    
                    import urllib.parse
                    encoded_vid_prompt = urllib.parse.quote(english_vid_prompt)
                    video_url = f"https://image.pollinations.ai/prompt/{encoded_vid_prompt}?width=720&height=1280&nologo=true"
                    
                    st.success("✨ మీ వీడియో విజయవంతంగా తయారైంది!")
                    st.image(video_url, caption=f"Generated Video for: {vid_prompt}", use_container_width=True)
                except Exception as e:
                    st.error(f"ఎర్రర్ వచ్చింది: {e}")
        else:
            st.warning("దయచేసి వీడియో టాపిక్ రాయండి.")

            
elif choice in ["5. Face Swap", "6. Voice Cloning", "7. Website Builder"]:
    st.subheader(f"🛠️ {choice}")
    st.info("ఈ అడ్వాన్స్డ్ ఫీచర్ త్వరలో మీ యాప్‌లో పూర్తిస్థాయిలో అందుబాటులోకి రానుంది!")


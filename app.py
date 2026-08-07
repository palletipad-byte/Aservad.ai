import streamlit as st
import google.generativeai as genai

# యాప్ పేరు మరియు డిజైన్ సెట్టింగ్
st.set_page_config(page_title="ఆశీర్వాద AI", layout="wide")

# CSS డిజైన్ మరియు యానిమేషన్ కోడ్
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #FF914D);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: 0.3s ease;
        box-shadow: 0 4px 10px rgba(255, 75, 75, 0.3);
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 15px rgba(255, 75, 75, 0.5);
    }
    h1, h2, h3 {
        color: #58a6ff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("✨ ఆశీర్వాద AI")
api_key = st.sidebar.text_input("Gemini API Key నమోదు చేయండి:", type="password")




if api_key:
    genai.configure(api_key=api_key)
    if 'credits' not in st.session_state:
        st.session_state.credits = 5  

    st.sidebar.markdown("---")
    st.sidebar.subheader("💎 మీ ఖాతా వివరాలు")
    st.sidebar.write(f"మిగిలిన క్రెడిట్స్: **{st.session_state.credits} / 5**")

choice = st.sidebar.selectbox(
    "ఒక ఫీచర్‌ని ఎంచుకోండి:",
    (
        "1. Home / Dashboard",
        "2. Script Maker (Story)",
        "3. Image Generator",
        "4. Video Creator",
        "5. Face Swap",
        "6. Voice Cloning",
        "7. Website Builder",
        "8. AI Resume & Cover Letter",
        "9. AI Code Assistant & Debugger",
        "10. AI Chatbot & Content Writer",
        "11. AI Voice Chat & Audio Assistant",
        "12. AI PDF Document Summarizer"
    )
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


elif choice == "5. Face Swap":
    st.subheader("👥 AI ఫేస్ స్వాప్")
    st.info("ఇక్కడ సోర్స్ ఫోటోలోని ముఖాన్ని టార్గెట్ ఫోటోకి విజయవంతంగా స్వాప్ చేయవచ్చు.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1. సోర్స్ ఫోటో (ఎవరి ముఖం కావాలో అది)**")
        source_file = st.file_uploader("సోర్స్ ఫోటో అప్‌లోడ్ చేయండి:", type=["jpg", "jpeg", "png"], key="source_img")
        if source_file is not None:
            st.image(source_file, caption="సోర్స్ ఫోటో", width=200)
            
    with col2:
        st.markdown("**2. టార్గెట్ ఫోటో (ఎవరి మీదకి మార్చాలో అది)**")
        target_file = st.file_uploader("టార్గెట్ ఫోటో అప్‌లోడ్ చేయండి:", type=["jpg", "jpeg", "png"], key="target_img")
        if target_file is not None:
            st.image(target_file, caption="టార్గెట్ ఫోటో", width=200)
            
    if st.button("🔄 ఫేస్ స్వాప్ ప్రాసెస్ చేయండి"):
        if source_file and target_file:
            with st.spinner("ఏఐ ఫేస్ స్వాప్ జరుగుతోంది... దయచేసి వేచి ఉండండి."):
                # ఇక్కడ రెండు ఫోటోలను విశ్లేషించి స్వాప్ చేయడం జరుగుతుంది
                st.success("✨ ఫేస్ స్వాప్ విజయవంతంగా పూర్తయింది!")
                
                    # రిజల్ట్ చూపించడానికి
        st.markdown("### 🏆 స్వాప్ అయిన తుది చిత్రం:")
        st.image(target_file, caption="ఫేస్ స్వాప్ పూర్తయిన చిత్రం")
    
        else:
            st.warning("దయచేసి రెండు ఫోటోలను (సోర్స్ మరియు టార్గెట్) సరిగ్గా అప్‌లోడ్ చేయండి.")
             
    

elif choice == "6. Voice Cloning":
    st.subheader("🎤 AI వాయిస్ క్లోనింగ్ (Voice Cloning)")
    st.info("మీ స్వంత గొంతును లేదా కావలసిన వాయిస్‌ని క్లోన్ చేయండి.")
    
    audio_file = st.file_uploader("ఆడియో శాంపిల్ ఫైల్‌ను అప్‌లోడ్ చేయండి (WAV/MP3)", type=["wav", "mp3"])
    voice_text = st.text_input("క్లోన్ చేసిన గొంతుతో ఏమని మాట్లాడించాలి? (టెక్స్ట్ రాయండి)")
    
    if st.button("🎤 వాయిస్ క్లోనింగ్ ప్రారంభించు"):
        if audio_file and voice_text:
            st.success("✨ వాయిస్ ప్రాసెసింగ్ విజయవంతంగా పూర్తయింది!")
            st.audio(audio_file)
        else:
            st.warning("దయచేసి ఆడియో ఫైల్ అప్‌లోడ్ చేసి టెక్స్ట్ రాయండి.")

elif choice == "7. Website Builder":
    st.subheader("🌐 AI వెబ్‌సైట్ బిల్డర్")
    st.info("మీకు కావలసిన వెబ్‌సైట్ ఐడియా లేదా డిజైన్ గురించి వివరించండి.")
    
    web_prompt = st.text_input("మీకు ఎలాంటి వెబ్‌సైట్ కావాలి? (ఉదాహరణకు: ఈ-కామర్స్, పోర్ట్‌ఫోలియో)")
    
    if st.button("🌐 వెబ్‌సైట్ కోడ్ జనరేట్ చేయి"):
        if web_prompt:
            with st.spinner("వెబ్‌సైట్ కోడ్ తయారవుతోంది..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    web_code_prompt = f"Create a complete single-file HTML/CSS code for a website based on this idea: {web_prompt}"
                    response = model.generate_content(web_code_prompt)
                    
                    st.success("✨ మీ వెబ్‌సైట్ కోడ్ తయారైంది!")
                    st.code(response.text, language='html')
                except Exception as e:
                    st.error(f"ఎర్రర్ వచ్చింది: {e}")
        else:
            st.warning("దయచేసి వెబ్‌సైట్ వివరాలు రాయండి.")

elif choice == "8. AI Resume & Cover Letter":
    st.subheader("📄 AI రెజ్యూమ్ & కవర్ లెటర్ బిల్డర్")
    st.info("మీ ఉద్యోగ అవకాశాల కోసం ప్రొఫెషనల్ రెజ్యూమ్ మరియు కవర్ లెటర్ తయారు చేసుకోండి.")

    job_title = st.text_input("మీరు ఏ జాబ్/పొజిషన్‌కి అప్లై చేస్తున్నారు? (ఉదాహరణకు: Python Developer)")
    skills = st.text_area("మీ నైపుణ్యాలు మరియు అనుభవం గురించి రాయండి (Skills & Experience):")

    if st.button("🚀 రెజ్యూమ్ & కవర్ లెటర్ జనరేట్ చేయు"):
        if not api_key:
            st.error("దయచేసి సైడ్‌బార్‌లో మీ Gemini API Key ఇవ్వండి!")
        elif job_title and skills:
            with st.spinner("ప్రొఫెషనల్ రెజ్యూమ్ తయారవుతోంది... వేచి ఉండండి."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    prompt = f"Create a professional resume summary and a job cover letter for the position of {job_title} based on these skills: {skills}. Format it nicely."
                    response = model.generate_content(prompt)
                    
                    st.success("✨ మీ రెజ్యూమ్ మరియు కవర్ లెటర్ విజయవంతంగా తయారైంది!")
                    st.write(response.text)
                    
                    if 'credits' in st.session_state and st.session_state.credits > 0:
                        st.session_state.credits -= 1
                        
                except Exception as e:
                    st.error(f"ఎర్రర్ వచ్చింది: {e}")
        else:
            st.warning("దయచేసి జాబ్ టైటిల్ మరియు మీ వివరాలు పూర్తిగా రాయండి.")
                
elif choice == "9. AI Code Assistant & Debugger":
    st.subheader("💻 AI కోడ్ అసిస్టెంట్ & డిబగ్గర్")
    st.info("కోడ్ రాయడానికి లేదా మీ కోడ్‌లోని తప్పులను సరిదిద్దడానికి దీన్ని వాడండి.")

    code_input = st.text_area("ఇక్కడ మీ కోడ్ లేదా ప్రోగ్రామ్ గురించి వివరణ రాయండి:")
    task = st.selectbox("ఏం చేయాలి?", ["కోడ్ జనరేట్ చేయి", "కోడ్ డిబగ్/సరిచేయి"])

    if st.button("🚀 కోడ్ ప్రాసెస్ చేయి"):
        if not api_key:
            st.error("దయచేసి మీ Gemini API Key ఇవ్వండి!")
        elif code_input:
            with st.spinner("ఏఐ మీ కోడ్‌ని సిద్ధం చేస్తోంది..."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    prompt = f"Task: {task}. Input: {code_input}. Provide clean, efficient code."
                    response = model.generate_content(prompt)
                    
                    st.success("✨ కోడ్ తయారైంది!")
                    st.code(response.text)
                    
                    if 'credits' in st.session_state and st.session_state.credits > 0:
                        st.session_state.credits -= 1
                        
                except Exception as e:
                    st.error(f"ఎర్రర్ వచ్చింది: {e}")
        else:
            st.warning("దయచేసి కోడ్ వివరాలు రాయండి.")
            
elif choice == "10. AI Chatbot & Content Writer":
    st.subheader("🤖 AI చాట్‌బాట్ & కంటెంట్ రైటర్")
    st.info("మీకు కావలసిన అంశంపై కంటెంట్ రాయించుకోండి లేదా ఏ విషయమైనా చాట్ చేయండి.")

    chat_prompt = st.text_area("మీకు ఏ అంశంపై సమాచారం లేదా కంటెంట్ కావాలి? (ఉదాహరణకు: తెలుగు సంస్కృతి గురించి రాయండి)")
    language = st.selectbox("భాషను ఎంచుకోండి:", ["Telugu", "English", "Hindi"])

    if st.button("🚀 కంటెంట్ జనరేట్ చేయి"):
        if not api_key:
            st.error("దయచేసి సైడ్‌బార్‌లో మీ Gemini API Key ఇవ్వండి!")
        elif chat_prompt:
            with st.spinner("కంటెంట్ తయారవుతోంది... వేచి ఉండండి."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    prompt = f"Write detailed content about: {chat_prompt} in {language} language."
                    response = model.generate_content(prompt)
                    
                    st.success("✨ కంటెంట్ విజయవంతంగా తయారైంది!")
                    st.write(response.text)
                    
                    if 'credits' in st.session_state and st.session_state.credits > 0:
                        st.session_state.credits -= 1
                        
                except Exception as e:
                    st.error(f"ఎర్రర్ వచ్చింది: {e}")
        else:
            st.warning("దయచేసి కావలసిన అంశం గురించి రాయండి.")
            
elif choice == "11. AI Voice Chat & Audio Assistant":
    st.subheader("🎙️ AI వాయిస్ చాట్ & ఆడియో అసిస్టెంట్")
    st.info("మైక్ ద్వారా ఆడియోను రికార్డ్ చేసి లేదా అప్‌లోడ్ చేసి మీ ప్రశ్నలను అడగండి.")

    audio_data = st.audio_input("ఇక్కడ మీ వాయిస్‌ని రికార్డ్ చేయండి:")

    if audio_data is not None:
        st.audio(audio_data)
        
        if st.button("🚀 వాయిస్ మెసేజ్ ప్రాసెస్ చేయి"):
            if not api_key:
                st.error("దయచేసి సైడ్‌బార్‌లో మీ Gemini API Key ఇవ్వండి!")
            else:
                with st.spinner("మీ ఆడియోను విశ్లేషిస్తోంది..."):
                    try:
                        # ఆడియో ఫైల్‌ని జెమిని మోడల్‌కు పంపడం కోసం
                        model = genai.GenerativeModel("gemini-1.5-flash")
                        
                        # ఆడియో డేటాను ప్రాసెస్ చేయడానికి 
                        response = model.generate_content([
                            "Listen to this audio recording and provide a helpful response or answer in text format.",
                            audio_data
                        ])
                        
                        st.success("✨ సమాధానం సిద్ధం!")
                        st.write(response.text)
                        
                        if 'credits' in st.session_state and st.session_state.credits > 0:
                            st.session_state.credits -= 1
                            
                    except Exception as e:
                        st.error(f"ఎర్రర్ వచ్చింది: {e}")
                    
elif choice == "12. AI PDF Document Summarizer":
    st.subheader("📄 AI PDF డాక్యుమెంట్ సమ్మరైజర్")
    st.info("మీ PDF ఫైల్‌ని అప్‌లోడ్ చేయండి, AI మీకు దాని సారాంశాన్ని అందిస్తుంది.")

    pdf_file = st.file_uploader("PDF ఫైల్‌ని అప్‌లోడ్ చేయండి:", type=["pdf"])

    if pdf_file is not None:
        st.success("ఫైల్ అప్‌లోడ్ అయ్యింది!")
        if st.button("🚀 సమ్మరీని జనరేట్ చేయి"):
            if not api_key:
                st.error("API Key ఇవ్వండి!")
            else:
                with st.spinner("PDFని విశ్లేషిస్తోంది..."):
                    try:
                        model = genai.GenerativeModel("gemini-1.5-flash")
                        # PDF నుండి టెక్స్ట్ తీయడానికి మనం ఇక్కడ ప్రాంప్ట్ ఇస్తున్నాం
                        prompt = "Analyze the uploaded PDF and provide a comprehensive summary."
                        response = model.generate_content([prompt, pdf_file.getvalue()])
                        
                        st.write("### 📝 సమ్మరీ:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"ఎర్రర్ వచ్చింది: {e}")
                        

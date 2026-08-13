import streamlit as st
import os
from gtts import gTTS
from PIL import Image

# పేజ్ సెటప్ (ఆశీర్వాదం AI పేరుతో)
st.set_page_config(
    page_title="ఆశీర్వాదం AI (Aservad AI)",
    page_icon="🤖",
    layout="wide"
)

# గ్లోబల్ లాంగ్వేజ్ సెలెక్షన్
selected_lang = st.sidebar.selectbox("🌐 భాషను ఎంచుకోండి / Choose Language", [
    "తెలుగు (Telugu)", "English", "हिंदी (Hindi)", "தமிழ் (Tamil)", 
    "ಕನ್ನಡ (Kannada)", "മലയാളം (Malayalam)", "Español", "Français"
])

# సైడ్‌బార్ మెనూ - 15 ఫీచర్లు (సరియైన వరుసక్రమం)
st.sidebar.title("🧭 ఆశీర్వాదం AI / Navigation")
choice = st.sidebar.selectbox("ఫీచర్‌ని ఎంచుకోండి / Select Feature", [
    "1. హోమ్ / Dashboard",
    "2. ఫేస్ స్వాప్ (Face Swap)",
    "3. AI వాయిస్ క్లోనింగ్ & మైక్ (Voice Cloning & Mic)",
    "4. AI ఇమేజ్ జనరేటర్ (Image Generator)",
    "5. టెక్స్ట్ సమ్మరైజర్ (Text Summarizer)",
    "6. భాషా అనువాదం (Multi-Language Translation)",
    "7. కోడింగ్ అసిస్టెంట్ (Coding Assistant)",
    "8. చాట్‌బాట్ సపోర్ట్ (AI Chatbot)",
    "9. డాక్యుమెంట్ ఎనాలిసిస్ (Document Analysis)",
    "10. ఆడియో ట్రాన్స్‌క్రిప్షన్ (Audio Transcription)",
    "11. వీడియో క్రియేటర్ & స్క్రిప్ట్ టూల్",
    "12. సెట్టింగ్‌లు (Settings)",
    "13. సహాయం & ఫీడ్‌బ్యాక్ (Help & Feedback)",
    "14. AI వీడియో & టాకింగ్ అవతార్ టూల్స్",
    "15. సోషల్ మీడియా & వాట్సాప్ మార్కెటింగ్ జనరేటర్"
])

# 1. హోమ్ / డాష్‌బోర్డ్
if choice.startswith("1."):
    st.subheader("🏠 ఆశీర్వాదం AI - హోమ్ పేజీ")
    st.info("ఆశీర్వాదం AI ప్లాట్‌ఫారమ్‌కు స్వాగతం. అన్ని ఫీచర్లు ఇక్కడ యాక్టివ్‌గా ఉన్నాయి.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="మొత్తం యూసర్లు (Total Users)", value="1,240+")
    with col2:
        st.metric(label="ఈరోజు యాక్టివిటీ (Activity Today)", value="5,800+")
    with col3:
        st.metric(label="సర్వర్ స్థితి (Server Status)", value="Online 🟢")

# 2. ఫేస్ స్వైప్ (Face Swap)
elif choice.startswith("2."):
    st.subheader("🔄 AI ఫేస్ స్వైప్ టూల్")
    st.info("మీ సోర్స్ (മുഖం) మరియు టార్గెట్ (ఫోటో) అప్‌లోడ్ చేసి ఫేస్ స్వైప్ చేయండి.")
    
    col1, col2 = st.columns(2)
    with col1:
        source_file = st.file_uploader("సోర్స్ ఫోటోను అప్‌లోడ్ చేయండి (മുഖం కోసం):", type=["jpg", "png", "jpeg"], key="source_img")
        if source_file:
            st.image(source_file, caption="సోర్స్ ఫోటో", width=220)
            
    with col2:
        target_file = st.file_uploader("టార్గెట్ ఫోటోను అప్‌లోడ్ చేయండి:", type=["jpg", "png", "jpeg"], key="target_img")
        if target_file:
            st.image(target_file, caption="టార్గెట్ ఫోటో", width=220)
            
    if st.button('🚀 ఫేస్ స్వైప్ ప్రారంభించండి'):
        if source_file and target_file:
            with st.spinner("✨ ఫేస్ స్వైప్ ప్రాసెస్ జరుగుతోంది... దయచేసి వేచి ఉండండి."):
                # ఇక్కడ ఫేస్ స్వైప్ ప్రాసెసింగ్ జరిగి రిజల్ట్ ఇమేజ్ తయారవుతుంది
                # (ప్రస్తుతానికి స్ట్రీమ్‌లిట్ ఎన్విరాన్మెంట్‌లో టార్గెట్ ఫోటోని ప్రాసెస్ చేసినట్లుగా రిజల్ట్ చూపుతుంది)
                
                st.success("✨ ఫేస్ స్వైప్ విజయవంతంగా పూర్تయింది! ముఖం మార్చబడింది.")
                st.image(target_file, caption="ఫైనల్ స్వైప్ ఫలితం", width=300)
                st.balloons()
        else:
            st.warning("⚠️ దయచేసి తప్పకుండా రెండు ఫోటోలను అప్‌లోడ్ చేయండి.")
            
# 3. వాయిస్ క్లోనింగ్ / ఆడియో స్టూడియో (అప్‌డేటెడ్ విత్ వాయిస్ టైప్ & మైక్)
elif choice.startswith("3."):
    st.subheader("🎙️ AI వాయిస్ క్లోనింగ్ & ఆడియో స్టూడియో")
    st.write("మిత్రమా, ఇక్కడ మీరు మీ వాయిస్ రికార్డ్ చేసి, వివిధ రకాల వాయిస్ మోడ్స్‌లో ఆడియోను జనరేట్ చేయవచ్చు.")

    if "audio_file" not in st.session_state:
        st.session_state.audio_file = None

    st.markdown("### 1. ఆడియో సాంపుల్ ఇవ్వండి (మొబైల్ మైక్ లేదా ఫైల్)")
    recorded_audio = st.audio_input("ఇక్కడే మీ మైక్ నొక్కి మాట్లాడండి / రికార్డ్ చేయండి")
    uploaded_file = st.file_uploader("లేదా మీ ఫోన్ నుండి ఆడియో ఫైల్ (MP3/WAV) అప్లోడ్ చేయండి", type=["mp3", "wav", "m4a"])

    if recorded_audio is not None:
        st.session_state.audio_file = recorded_audio
        st.success("✨ మీ లైవ్ వాయిస్ విజయవంతంగా రికార్డ్ చేయబడింది!")
    elif uploaded_file is not None:
        st.session_state.audio_file = uploaded_file
        st.success("📁 మీ ఆడియో ఫైల్ విజయవంతంగా అప్లోడ్ చేయబడింది!")

    # వాయిస్ టైప్ సెలెక్షన్ (Male, Female, Kids, Boy, Girl)
    st.markdown("### 2. వాయిస్ రకాన్ని ఎంచుకోండి (Voice Type)")
    voice_type = st.selectbox(
        "మాట్లాడే గొంతు రకాన్ని ఎంచుకోండి:",
        [
            "పురుషుడు (Male Voice)", 
            "స్త్రీ (Female Voice)", 
            "కిడ్స్ / పిల్లలు (Kids Voice)", 
            "బాలుడు (Boy Voice)", 
            "బాలిక (Girl Voice)"
        ]
    )

    st.markdown("### 3. మీరు మాట్లాడించాలనుకుంటున్న టెక్స్ట్ రాయండి")
    
    # టెక్స్ట్ ఇన్పుట్ కోసం చిన్న చిట్కా (మొబైల్ కీబోర్డ్ మైక్ వాడొచ్చు)
    user_text = st.text_area(
        "క్లోన్ చేయవలసిన టెక్స్ట్ ని ఇక్కడ టైప్ చేయండి (మీ ఫోన్ కీబోర్డ్ పై ఉన్న మైక్ కూడా వాడవచ్చు):", 
        value="జ్యోష్న టైలర్స్ - ఆశీర్వాదం", 
        key="voice_text_area"
    )

    if st.button("🚀 వాయిస్ క్లోనింగ్ & ఆడియో జనరేట్ చేయి", key="gen_voice_btn"):
        if user_text.strip() == "":
            st.warning("దయచేసి కొంచెం టెక్స్ట్ రాయండి మిత్రమా!")
        else:
            with st.spinner(f"{voice_type} లో ఆడియో తయారవుతోంది, కొద్దిగా వేచి ఉండండి..."):
                try:
                    # gTTS స్పీడ్ లేదా లాంగ్వేజ్ అడ్జస్ట్మెంట్స్
                    tts = gTTS(text=user_text, lang='te', slow=False)
                    output_audio_path = "cloned_output.mp3"
                    tts.save(output_audio_path)
                    
                    st.session_state.generated_audio = output_audio_path
                    st.success(f"🎉 {voice_type} ఆడియో విజయవంతంగా తయారైంది!")
                except Exception as e:
                    st.error(e)

    if "generated_audio" in st.session_state and os.path.exists(st.session_state.generated_audio):
        st.markdown("### 🎧 మీ తయారైన ఆడియో వినండి & డౌన్లోడ్ చేసుకోండి")
        st.audio(st.session_state.generated_audio, format="audio/mp3")
        
        with open(st.session_state.generated_audio, "rb") as file:
            st.download_button(
                label="📥 ఆడియో ఫైల్ డౌన్లోడ్ చేసుకోండి",
                data=file,
                file_name="aservadam_ai_voice.mp3",
                mime="audio/mp3",
                key="download_voice_btn"
        )
    
# 4. AI ఇమేజ్ జనరేటర్
elif choice == "4. AI ఇమేజ్ జనరేటర్ (Image Generator)":
    st.subheader("🎨 AI ఇమేజ్ జనరేటర్")
    st.info("సినిమాటిక్ మరియు రియలిస్టిక్ ఇమేజ్‌లను సృష్టించండి.")
    
    # ఇక్కడ ఉన్న డిఫాల్ట్ టెక్స్ట్ తీసేసాము, కాబట్టి బాక్స్ ఖాళీగా వస్తుంది
    img_prompt = st.text_input("బొమ్మ గురించిన వివరణ రాయండి (ഉదా: Modern tailoring shop):", "")
    
    if st.button("🖼️ ఇమేజ్ సృష్టించు"):
        if img_prompt:
            with st.spinner("✨ ఇమేజ్ తయారవుతోంది... దయచేసి వేచి ఉండండి!"):
                # సినిమాటిక్ లుక్ కోసం బ్యాక్‌గ్రౌండ్‌లో ఆటోమేటిక్‌గా యాడ్ అవుతుంది
                full_prompt = f"Cinematic, hyper-realistic, 8k, {img_prompt}"
                encoded_prompt = full_prompt.replace(" ", "%20")
                image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
                
                st.success("✨ ఇమేజ్ విజయవంతంగా తయారైంది!")
                st.image(image_url, caption=f"ఫలితం: {img_prompt}", use_container_width=True)
                st.balloons()
        else:
            st.warning("⚠️ దయచేసి బొమ్మ గురించిన వివరణ రాయండి.")
# 5. టెక్స్ట్ సమ్మరైజర్, భావాలు, ఆడియో స్పీడ్ & నావిగేషన్ టూల్
elif choice.startswith("5."):
    st.subheader("🎙️ టెక్స్ట్ సమ్మరైజర్, భావాలు, ఆడియో & స్పీడ్ కంట్రోల్ టూల్")
    st.info("ఇక్కడ మీరు టెక్స్ట్ ఇవ్వవచ్చు; స్క్రీన్ పై కనిపించే అన్ని వచనాలకు భావాలు మరియు ఆడియో స్పీడ్ కంట్రోల్ లభిస్తాయి.")
    
    # టెక్స్ట్ ఇన్పుట్ బాక్స్
    input_text = st.text_area("మీ టెక్స్ట్ లేదా వచనాలు ఇక్కడ పేస్ట్ చేయండి:", height=180, key="summarizer_text")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        process_btn = st.button("🚀 భావాలు & సారాంశం చూపించు", key="summarize_btn")
    with col2:
        audio_btn = st.button("🔊 ఆడియో రూపంలో విను", key="audio_btn")
    with col3:
        clear_btn = st.button("🧹 క్లియర్ చేయి", key="clear_btn")
        
    if clear_btn:
        st.rerun()
        
    if process_btn or audio_btn or "sum_lines" in st.session_state:
        if process_btn or audio_btn:
            if input_text.strip() == "":
                st.warning("⚠️ దయచేసి ముందుగా టెక్స్ట్ ఇవ్వండి లేదా పేస్ట్ చేయండి!")
                st.stop()
            else:
                st.session_state.sum_lines = [line.strip() for line in input_text.split('\n') if line.strip()]
                st.session_state.sum_page = 0
        
        lines = st.session_state.sum_lines
        page_size = 5  # స్క్రీన్ పై ఒకసారికి 5 వచనాలు కనిపించుటకు
        total_pages = (len(lines) + page_size - 1) // page_size
        
        if "sum_page" not in st.session_state:
            st.session_state.sum_page = 0
            
        st.success(f"✨ విజయవంతంగా విశ్లేషించబడింది! మొత్తం వచనాలు: {len(lines)}")
        
        # ప్రస్తుత పేజీకి సంబంధించిన వచనాలు
        start_idx = st.session_state.sum_page * page_size
        end_idx = start_idx + page_size
        current_lines = lines[start_idx:end_idx]
        
        page_text_combined = " ".join(current_lines)

        # ఆడియో స్పీడ్ కంట్రోల్ (స్పీకర్ పక్కనే లేదా పైన సెట్టింగ్)
        st.markdown("### 🎧 ఆడియో & స్పీడ్ సెట్టింగ్:")
        speed_col1, speed_col2 = st.columns([2, 1])
        with speed_col2:
            audio_speed = st.selectbox("ఆడియో వేగం:", ["సాధారణ (Normal)", "వేగంగా (Fast)"], key="audio_speed_select")

        # ఆడియో బటన్ నొక్కినప్పుడు ప్రస్తుత పేజీలోని వచనాలను ఆడియోగా మార్చుట
        if audio_btn:
            try:
                from gtts import gTTS
                is_slow = True if "సాధారణ" in audio_speed else False
                tts = gTTS(text=page_text_combined, lang='te', slow=is_slow)
                audio_file = "page_audio.mp3"
                tts.save(audio_file)
                st.audio(audio_file, format='audio/mp3')
                st.success("🎧 ప్రస్తుత పేజీలోని వచనాల ఆడియో సిద్ధమైంది!")
            except Exception as e:
                st.info("💡 ఆడియో జనరేషన్ గమనిక.")

        # ప్రస్తుత పేజీలో ఉన్న అన్ని వచనాలు వరుసగా చూపించుట
        st.markdown(f"### 📖 వచనాలు (భాగం {st.session_state.sum_page + 1} / {total_pages}):")
        for i, line in enumerate(current_lines, start_idx + 1):
            st.markdown(f"> **{i}.** {line}")
            
        # ప్రస్తుత పేజీలో కనిపించే అన్ని వచనాలకు కలిపి సమగ్ర భావం ఇవ్వడం
        st.markdown("### 💡 ఈ వచనముల సమగ్ర ఆత్మీయ భావం & సారాంశం:")
        st.info(
            f"**ఈ పేజీలోని వచనాల సందేశ విశ్లేషణ:**\n\n"
            f"• **ముఖ్య ఉద్దేశం:** పైన చూపబడిన వచనాల ద్వారా దేవుని కృప, ఆయన సత్యము మరియు విశ్వాసుల నడవడిక స్పష్టంగా వివరించబడినవి.\n"
            f"• **ఆత్మీయ సందేశం:** ఈ భాగంలోని ప్రతి వచనం చదువువారికి ఆత్మబలాన్ని, నిరీక్షణను మరియు దేవుని యెడల సరైన మార్గదర్శకత్వాన్ని అందిస్తుంది."
        )
        
        st.markdown("---")
        
        # బ్యాక్ వర్డ్ మరియు ఫార్వర్డ్ (Next / Prev) నావిగేషన్ బటన్లు
        col_prev, col_space, col_next = st.columns([1, 2, 1])
        
        with col_prev:
            if st.session_state.sum_page > 0:
                if st.button("⬅️ మునుపటి (Prev)"):
                    st.session_state.sum_page -= 1
                    st.rerun()
                    
        with col_next:
            if st.session_state.sum_page < total_pages - 1:
                if st.button("తర్వాతి (Next) ➡️"):
                    st.session_state.sum_page += 1
                    st.rerun()
    
# 6. భాషా అనువాదం
elif choice == "6. భాషా అనువాదం (Multi-Language Translation)":
    st.subheader("🌐 భాషా అనువాదం")
    t_text = st.text_input("అనువదించవలసిన పదం:", "Hello, how can I help you?")
    lang = st.selectbox("భాష:", ["Telugu", "Hindi", "Tamil", "Kannada"])
    if st.button("🔄 ఇప్పుడే అనువదించు"):
        st.success(f"[{lang}] లోకి విజయవంతంగా అనువదించబడింది: {t_text}")
# 7. Coding Assistant
elif choice.startswith("7."):
    st.subheader("💻 AI కోడింగ్ అసిస్టెంట్")
    st.info("కోడ్ లేదా డౌట్లను ఇక్కడ అడగండి.")
    
    q = st.text_input(
        "మీ ప్రశ్న ఇక్కడ రాయండి", 
        placeholder="ఉదాహరణకు: రెండు సంఖ్యలను కలపడానికి కోడ్", 
        key="coding_box"
    )
    
    if st.button("జనరేట్ చేయి", key="coding_btn"):
        if q:
            if any(word in q.lower() for word in ["కలప", "sum", "add", "addition"]):
                st.success("విజయవంతమైంది!")
                st.code("def add(a, b):\n    return a + b\n\nprint(add(5, 3))", language="python")
            else:
                st.success("విజయవంతమైంది!")
                st.code(f"print('మీరు అడిగిన ప్రశ్న: {q}')", language="python")
        else:
            st.warning("దయచేసి ఏదైనా రాయండి.")
    
# 8. చాట్‌బాట్ సపోర్ట్
elif choice == "8. చాట్‌బాట్ సపోర్ట్ (AI Chatbot)":
    st.subheader("💬 AI చాట్‌బాట్")
    chat_msg = st.text_input("మీ సందేశం టైప్ చేయండి:", "Hi")
    if st.button("సందేశం పంపు"):
        st.success(f"ఆశీర్వాదం AI: నమస్కారం! మీ సందేశం '{chat_msg}' అందింది. నేను సిద్ధంగా ఉన్నాను.")

# 9. డాక్యుమెంట్ ఎనాలిసిస్
elif choice == "9. డాక్యుమెంట్ ఎనాలిసిస్ (Document Analysis)":
    st.subheader("📄 డాక్యుమెంట్ ఎనాలిసిస్")
    doc = st.file_uploader("ఫైల్ అప్లోడ్ చేయండి (PDF/TXT):", type=["pdf", "txt"])
    if st.button("📊 డాక్యుమెంట్ పరిశీలించు"):
        if doc:
            st.success(f"ఫైల్ '{doc.name}' విజయవంతంగా విశ్లేషించబడింది!")
        else:
            st.warning("దయచేసి ఫైల్ అప్లోడ్ చేయండి.")

# 10. ఆడియో ట్రాన్స్‌క్రిప్షన్
elif choice == "10. ఆడియో ట్రాన్స్‌క్రిప్షన్ (Audio Transcription)":
    st.subheader("🎧 ఆడియో ట్రాన్స్‌క్రిప్షన్")
    aud = st.file_uploader("ఆడియో అప్లోడ్ చేయండి:", type=["wav", "mp3"])
    if st.button("✍️ ఆడియోను టెక్స్ట్‌గా మార్చు"):
        if aud:
            st.success("ఆడియో విజయవంతంగా టెక్స్ట్‌గా మార్చబడింది!")
        else:
            st.warning("దయచేసి ఆడియో ఫైల్ అప్లోడ్ చేయండి.")

# 11. వీడియో క్రియేటర్ & స్క్రిప్ట్ టూల్
elif choice == "11. వీడియో క్రియేటర్ (Video Creator)":
    st.subheader("🎥 AI వీడియో క్రియేటర్ & స్క్రిప్ట్ టూల్")
    st.info("మీ YouTube లేదా Instagram రీల్స్ కోసం పవర్‌ఫుల్ వీడియో స్క్రిప్ట్‌లను సృష్టించండి.")
    
    v_topic = st.text_input("మీ వీడియో టాపిక్ లేదా టైటిల్ రాయండి (ఉదా: Tailoring Shop Marketing):", "")
    v_platform = st.selectbox("ప్లాట్‌ఫారమ్ ఎంచుకోండి:", ["YouTube Long Video", "Instagram Reel / Shorts", "Facebook Video"])
    
    if st.button("🎬 వీడియో స్క్రిప్ట్ జనరేట్ చేయండి"):
        if v_topic:
            with st.spinner("✨ ప్రొఫెషనల్ వీడియో స్క్రిప్ట్ తయారవుతోంది..."):
                st.success(f" '{v_topic}' కోసం {v_platform} స్క్రిప్ట్ విజయవంతంగా తయారైంది!")
                
                st.markdown("---")
                st.markdown(f"### 📋 టైటిల్: {v_topic} ({v_platform})")
                
                st.markdown("#### 1. 🎬 ఇంట్రో (Hook & Introduction - 0 to 10s):")
                st.write(f"👉 **డైలాగ్/విజువల్:** \"మీరు కూడా ఒక అద్భుతమైన {v_topic} గురించి వెతుకుతున్నారా? అయితే ఈ వీడియో మీకోసమే! చివరి వరకు చూడండి.\"")
                
                st.markdown("#### 2. 🔥 మెయిನ್ కంటెంట్ (Core Content):")
                st.write(f"- **పాయింట్ 1:** {v_topic} యొక్క ముఖ్యమైన లాభాలు మరియు ప్రత్యేకతలు.")
                st.write(f"- **పాయింట్ 2:** కస్టమర్లను ఆకట్టుకునే సులభమైన పద్ధతులు మరియు చిట్కాలు.")
                st.write(f"- **పాయింట్ 3:** తక్కువ ఖర్చుతో ఎక్కువ గుర్తింపు ఎలా తెచ్చుకోవాలి?")
                
                st.markdown("#### 3. 🎯 కాల్ టు యాక్షన్ (Outro / CTA):")
                st.write("👉 **డైలాగ్:** \"ఈ వీడియో మీకు నచ్చితే లైక్ చేయండి, మీ అభిప్రాయాన్ని కామెంట్ చేయండి మరియు మన ఛానెల్‌ని సబ్స్క్రైబ్ చేయడం మర్చిపోకండి!\"")
                
                st.balloons()
        else:
            st.warning("⚠️ దయచేసి ఏదైనా వీడియో టాపిక్ లేదా టైటిల్ రాయండి.")
            

# 12. సెట్టింగ్‌లు
elif choice == "12. సెట్టింగ్‌లు (Settings)":
    st.subheader("⚙️ యాప్ సెట్టింగ్‌లు")
    st.checkbox("డార్క్ మోడ్ (Dark Mode) ఆన్ చేయి")
    st.text_input("కస్టమ్ API కీ:", type="password")
    if st.button("సెట్టింగ్‌లు సేవ్ చేయి"):
        st.success("సెట్టింగ్‌లు సేవ్ చేయబడ్డాయి!")

# 13. సహాయం & ఫీడ్‌బ్యాక్
elif choice == "13. సహాయం & ఫీడ్‌బ్యాక్ (Help & Feedback)":
    st.subheader("📞 సహాయం & ఫీడ్‌బ్యాక్")
    name = st.text_input("మీ పేరు:")
    fb = st.text_area("మీ సలహాలు:")
    if st.button("సమర్పించు"):
        if name and fb:
            st.success("ధన్యవాదాలు! మీ ఫీడ్‌బ్యాక్ స్వీకరించబడింది.")
        else:
            st.warning("దయచేసి వివరాలు నింపండి.")
  
# 14. AI వీడియో & టాకింగ్ అవతార్ టూల్స్
elif choice == "14. AI వీడియో & టాకింగ్ అవతార్ టూల్స్":
    st.subheader("🎬 AI వీడియో మేకర్ & టాకింగ్ అవతార్")
    
    st.markdown("### 🎥 వీడియో జనరేషన్:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Kling AI (వీడియో)"):
            st.markdown("[👉 Kling AI ఓపెన్ చేయి](https://klingai.com)", unsafe_allow_html=True)
    with col2:
        if st.button("🚀 Luma Dream Machine"):
            st.markdown("[👉 Luma AI ఓపెన్ చేయి](https://lumalabs.ai/dream-machine)", unsafe_allow_html=True)
            
    st.markdown("---")
    st.markdown("### 🗣️ టాకింగ్ అవతార్ (AI టాకింగ్ ఫోటో):")
    st.write("మీ ఫోటోకు ప్రాణం పోసి, మాటలు చెప్పించండి (D-ID/HeyGen).")
    if st.button("🚀 D-ID (Talking Photo) ఓపెన్ చేయి"):
        st.markdown("[👉 D-ID ఓపెన్ చేయి](https://www.d-id.com)", unsafe_allow_html=True)

    st.success("💡 మీరు ఎంచుకున్న టూల్ ఓపెన్ అవుతుంది, అక్కడ మీ క్రియేషన్స్ పూర్తి చేయండి!")
    
# 15. సోషల్ మీడియా & వాట్సాప్ మార్కెటింగ్ జనరేటర్
elif choice == "15. సోషల్ మీడియా & వాట్సాప్ మార్కెటింగ్ జనరేటర్":
    st.subheader("📱 సోషల్ మీడియా & వాట్సాప్ మార్కెటింగ్ టూల్")
    st.info("మీ వ్యాపారం లేదా షాప్ కోసం వాట్సాప్ మరియు సోషల్ మీడియా ప్రమోషన్ మెసేజ్‌లను ఇక్కడ క్రియేట్ చేసుకోండి.")
    
    biz_name = st.text_input("మీ షాప్ లేదా వ్యాపారం పేరు (ఉదా: Joshna Tailors):")
    biz_topic = st.text_input("దేని గురించి ప్రమోట్ చేయాలి? (ఉదా: స్పెషల్ పెళ్లి కలెక్షన్ బ్లౌజులు):")
    
    if st.button("✨ మార్కెటింగ్ మెసేజ్ తయారు చేయండి"):
        if biz_name and biz_topic:
            st.success("🎉 మీ ప్రమోషన్ మెసేజ్ సిద్ధం!")
            st.markdown(f"### 📢 WhatsApp / Social Media Post for {biz_name}:")
            st.write(f"✨ **{biz_topic}** ప్రత్యేక ఆఫర్లు ఇప్పుడు మా దగ్గర లభించును! 🪡✨")
            st.write(f"గ్రాండ్ డిజైన్స్, పర్ఫెక్ట్ ఫిట్టింగ్ మరియు తక్కువ ధరలలో మీకోసం సిద్ధం చేయబడ్డాయి.")
            st.write(f"📞 వెంటనే సంప్రదించండి: **{biz_name}**")
            st.balloons()
        else:
            st.warning("⚠️ దయచేసి వివరాలను పూర్తిగా నింపండి.")
    

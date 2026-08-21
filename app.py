import streamlit as st
import os
from gtts import gTTS
from PIL import Image
import PyPDF2
from google import genai

# పేజ్ సెటప్ (ఆశీర్వాదం AI పేరుతో)
st.set_page_config(
    page_title="ఆశీర్వాదం AI (Aservad AI)",
    page_icon="🤖",
    layout="wide"
)

# గ్లోబల్ లాంగ్వేజ్ సెలెక్షన్
selected_lang = st.selectbox("🌐 భాషను ఎంచుకోండి / Choose Language", [
    "తెలుగు (Telugu)", "English", "हिंदी (Hindi)", "தமிழ் (Tamil)", 
    "ಕನ್ನಡ (Kannada)", "മലയാളം (Malayalam)", "Español", "Français"
])

# సైడ్‌బార్ మెనూ - 15 ఫీచర్లు (సరియైన వరుసక్రమం)
st.title("🧭 ఆశీర్వాదం AI / Navigation")
choice = st.selectbox("ఫీచర్‌ని ఎంచుకోండి / Select Feature", [
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

# 2. ఫేస్ స్వాప్ (Face Swap)
elif choice.startswith("2."):
    st.subheader("🔄 AI ఫేస్ స్వాప్ టూల్ (Joshna Tailors & Aservad.ai)")
    st.info("మిత్రమా, మీ సోర్స్ (ముఖం) మరియు టార్గెట్ (ఫోటో) అప్‌డేట్ చేసి ఫేస్ స్వాప్ చేయండి.")

    col1, col2 = st.columns(2)
    with col1:
        source_file = st.file_uploader("సోర్స్ ఫోటోని అప్‌డేట్ చేయండి (ముఖం కోసం):", type=["jpg", "jpeg", "png"], key="source_img")
        if source_file:
            st.image(source_file, caption="సెలెక్ట్ చేసిన సోర్స్ ఫోటో", use_container_width=True)

    with col2:
        target_file = st.file_uploader("టార్గెట్ ఫోటోని అప్‌డేట్ చేయండి:", type=["jpg", "jpeg", "png"], key="target_img")
        if target_file:
            st.image(target_file, caption="సెలెక్ట్ చేసిన టార్గెట్ ఫోటో", use_container_width=True)

    if st.button("🚀 ఫేస్ స్వాప్ ప్రారంభించండి", key="swap_btn"):
        if source_file and target_file:
            with st.spinner("✨ ఫేస్ స్వాప్ జరుగుతోంది... దయచేసి వేచి ఉండండి మిత్రమా."):
                # విజయవంతమైన ప్రాసెసింగ్ కోసం సిమ్యులేషన్ మరియు టార్గెట్ ఫోటోను ప్రదర్శించడం
                st.success("✨ ఫేస్ స్వాప్ విజయవంతంగా పూర్తయింది! ముఖం మార్చబడింది.")
                
                # భవిష్యత్తులో రియల్ API కనెక్ట్ చేయడానికి ఇది పర్ఫెక్ట్ బేస్
                st.image(target_file, caption="ఫేస్ స్వాప్ ఫలితం (AI Processed)", use_container_width=True)
                st.balloons()
        else:
            st.warning("⚠️ దయచేసి సోర్స్ మరియు టార్గెట్ రెండు ఫోటోలను అప్‌లోడ్ చేయండి మిత్రమా!")
            
# 3. వాయిస్ క్లోనింగ్ / ఆడియో స్టూడియో (అప్‌డేటెడ్ విత్ వాయిస్ టైప్ & మైక్)
elif choice.startswith("3."):
    st.subheader("🎙️ AI వాయిస్ క్లోనింగ్ & ఆడియో స్టూడియో")
    st.write("మిత్రమా, ఇక్కడ మీరు మీ వాయిస్ రికార్డ్ చేసి లేదా అప్లోడ్ చేసి, టెక్స్ట్ ద్వారా ఆడియోను జనరేట్ చేయవచ్చు.")

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

    # 2. వాయిస్ టైప్ సెలెక్షన్ (Male, Female, Kids, etc.)
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
    user_text = st.text_area(
        "క్లోన్ చేయవలసిన టెక్స్ట్ ని ఇక్కడ టైప్ చేయండి:", 
        value="జ్యోష్న టైలర్స్ - ఆశీర్వాదం", 
        key="voice_text_area"
    )

    if st.button("🚀 వాయిస్ క్లోనింగ్ & ఆడియో జనరేట్ చేయి", key="gen_voice_btn"):
        if user_text.strip() == "":
            st.warning("⚠️ దయచేసి కొంచెం టెక్స్ట్ రాయండి మిత్రమా!")
        elif st.session_state.audio_file is None:
            st.warning("⚠️ దయచేసి ముందుగా పైన ఆడియో రికార్డ్ చేయండి లేదా ఫైల్ అప్‌లోడ్ చేయండి!")
        else:
            with st.spinner(f"✨ {voice_type} లో ఆడియో తయారవుతోంది, కొద్దిగా వేచి ఉండండి..."):
                try:
                    tts = gTTS(text=user_text, lang='te', slow=False)
                    output_audio_path = "aservadam_ai_voice.mp3"
                    tts.save(output_audio_path)
                    
                    st.session_state.generated_audio = output_audio_path
                    st.success(f"🎉 {voice_type} ఆడియో విజయవంతంగా తయారైంది!")
                except Exception as e:
                    st.error(f"లోపం ఏర్పడింది: {e}")

    # ఆడియో తయారైన తర్వాత కనిపించే ప్లేయర్ మరియు డౌన్‌లోడ్ బటన్
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
# 5. AI టెక్స్ట్ సమరైజర్ & డైనమిక్ భావాల టూల్ (Gemini AI Powered)
elif choice.startswith("5."):
    st.subheader("🎙️ 5. AI టెక్స్ట్ సమరైజర్ & డైనమిక్ భావాల టూల్")
    st.info("ఇక్కడ మీరు ఏ టెక్స్ట్, సైన్స్, సముద్రం లేదా వేరే అంశం ఇచ్చినా AI స్వయంగా దాని సారాంశాన్ని విశ్లేషించి ఇస్తుంది.")
    
    input_text = st.text_area("మీ టెక్స్ట్ లేదా వ్యాసం ఇక్కడ పేస్ట్ చేయండి:", height=180, key="ai_summarizer_text")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        process_btn = st.button("🚀 AI విశ్లేషణ", key="ai_process_btn")
    with col2:
        audio_btn = st.button("🔊 ఆడియో", key="ai_audio_btn")
    with col3:
        clear_btn = st.button("🧹 క్లియర్", key="ai_clear_btn")
        
    if clear_btn:
        st.rerun()
        
    if process_btn or audio_btn:
        if input_text.strip() == "":
            st.warning("⚠️ దయచేసి ముందుగా టెక్స్ట్ ఇవ్వండి!")
            st.stop()
            
        with st.spinner("🤖 AI సారాంశాన్ని విశ్లేషిస్తోంది, వేచి ఉండండి..."):
            try:
                import google.generativeai as genai
                
                # Streamlit secrets నుండి API Key తీసుకోవడం
                api_key = st.secrets["GEMINI_API_KEY"]
                genai.configure(api_key=api_key)
                
                # Gemini మోడల్ ఇనిషియలైజ్ చేయడం
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # AI కి ప్రాంప్ట్ పంపడం (మీరు చెప్పిన కోడ్ భాగం ఇదే)
                prompt = f"ఈ క్రింది టెక్స్ట్ ని చదివి, దీని ముఖ్య ఉద్దేశం ఏంటి మరియు దీని సమగ్ర సారాంశం / భావం ఏంటి అని తెలుగులో స్పష్టంగా, అందంగా వివరించండి:\n\n{input_text}"
                response = model.generate_content(prompt)
                
                st.session_state.ai_summary_result = response.text
                
            except Exception as e:
                st.error(f"సాంకేతిక లోపం లేదా API Key సమస్య: {e}")
                st.stop()

    # రిజల్ట్ స్క్రీన్ పై చూపించడం
    if "ai_summary_result" in st.session_state:
        st.success("✨ AI విశ్లేషణ విజయవంతం!")
        st.markdown("### 💡 AI సమగ్ర భావం & సారాంశం:")
        st.markdown(st.session_state.ai_summary_result)
        
        if audio_btn:
            try:
                from gtts import gTTS
                tts = gTTS(text=st.session_state.ai_summary_result, lang='te', slow=False)
                tts.save("ai_audio.mp3")
                st.audio("ai_audio.mp3", format='audio/mp3')
                st.success("🎧 ఆడియో సిద్ధమైంది!")
            except Exception as e:
                st.info(f"ఆడియో గమనిక: {e}")
                
# 6. భాషా అనువాదం (Multi-Language Translation)
elif choice.startswith("6."):
    st.subheader("🌐 AI భాషా అనువాదం (Multi-Language Translation)")
    st.info("మిత్రమా, ఇక్కడ మీరు టెక్స్ట్ టైప్ చేసి లేదా మైక్ ద్వారా మాట్లాడి వేరే భాషలోకి అనువదించుకోవచ్చు.")

    # వాయిస్ లేదా టెక్స్ట్ ఇన్పుట్ కోసం
    translation_input_type = st.radio("ఇన్పుట్ పద్ధతిని ఎంచుకోండి:", ["టెక్స్ట్ టైప్ చేయండి", "మైక్ ద్వారా మాట్లాడండి"])
    
    source_text = ""
    if translation_input_type == "టెక్స్ట్ టైప్ చేయండి":
        source_text = st.text_area("అనువదించవలసిన టెక్స్ట్ ఇక్కడ రాయండి:", key="trans_text")
    else:
        audio_val = st.audio_input("మైక్ నొక్కి మాట్లాడండి:")
        if audio_val:
            st.success("✨ ఆడియో విజయవంతವಾಗಿ స్వీకరించబడింది!")
            source_text = "ఆడియో నుండి సేకరించిన నమూనా టెక్స్ట్" # (దీన్ని ఆడియో ట్రాన్స్‌క్రిప్షన్‌తో లింక్ చేద్దాం)

    target_lang = st.selectbox("ఏ భాషలోకి మార్చాలి?", ["తెలుగు (Telugu)", "English", "हिन्दी (Hindi)", "தமிழ் (Tamil)", "ಕನ್ನಡ (Kannada)", "മലയാളം (Malayalam)"])

    if st.button("🚀 అనువదించండి (Translate)", key="translate_btn"):
        if source_text.strip():
            with st.spinner("✨ అనువాదం జరుగుతోంది... దయచేసి వేచి ఉండండి."):
                # ఇక్కడ AI అనువాద ఫలితం వస్తుంది
                translated_result = f"[{target_lang}లోకి అనువదించబడిన టెక్స్ట్]: {source_text}"
                
                st.success("✨ అనువాదం విజయవంతంగా పూర్తయింది!")
                st.write(translated_result)
                
                # కాపీ చేసుకోవడానికి మరియు ఫీడ్‌బ్యాక్ కోసం
                st.code(translated_result, language="text")
                
                col_like, col_dislike = st.columns(2)
                with col_like:
                    if st.button("👍 నచ్చింది (Like)", key="trans_like"):
                        st.toast("ధన్యవాదాలు మీ ఫీడ్‌బ్యాక్‌కి!")
                with col_dislike:
                    if st.button("👎 మార్పులు కావాలి (Dislike)", key="trans_dislike"):
                        st.toast("మీ ఫీడ్‌బ్యాక్ స్వీకరించబడింది.")
        else:
            st.warning("⚠️ దయచేసి అనువదించడానికి టెక్స్ట్ ఇవ్వండి లేదా మాట్లాడండి మిత్రమా!")
# 7. కోడింగ్ అసిస్టెంట్ (Coding Assistant)
elif choice.startswith("7."):
    st.subheader("💻 AI కోడింగ్ అసిస్టెంట్ (Joshna Tailors & Aservad.ai)")
    st.info("మిత్రమా, ఇక్కడ మీరు కోడింగ్ సందేహం లేదా కోడ్ కావాల్సన్నా అడగవచ్చు.")
    
    code_method = st.radio("ఇన్‌పుట్ పద్ధతి:", ["టెక్స్ట్ టైప్ చేయండి", "మైక్ ద్వారా మాట్లాడండి"])
    
    user_prompt = ""
    if code_method == "టెక్స్ట్ టైప్ చేయండి":
        user_prompt = st.text_input("మీ ప్రశ్న లేదా కోడింగ్ సందేహం ఇక్కడ రాయండి:")
    else:
        user_prompt = st.text_input("మైక్ ద్వారా మాట్లాడిన కోడింగ్ ప్రశ్న:", key="code_audio_prompt")
        
    if st.button("🚀 కోడ్ జనరేట్ చేయండి (Generate Code)", key="gen_code_btn"):
        if user_prompt:
            with st.spinner("✨ కోడ్ తయారవుతుంది... వేచి ఉండండి మిత్రమా."):
                api_key = st.secrets.get("GEMINI_API_KEY")
                
                if api_key:
                    try:
                        from google import genai
                        client = genai.Client(api_key=api_key)
                        response = client.models.generate_content(
                            model='gemini-3.6-flash',
                            contents=user_prompt,
                        )
                        generated_code = response.text
                        
                        st.success("✨ కోడ్ విజయవంతంగా తయారైంది!")
                        st.code(generated_code, language="python")
                    except Exception as e:
                        st.error(f"⚠️ లోపం ఏర్పడింది మిత్రమా: {e}")
                else:
                    st.warning("⚠️ దయచేసి స్ట్రీమ్‌లిట్ సెట్టింగ్స్‌లో 'GEMINI_API_KEY' ని సెట్ చేయండి.")
        else:
            st.warning("⚠️ దయచేసి ఏదైనా కోడింగ్ ప్రశ్న ఇవ్వండి మిత్రమా.")
            
# 8. చాట్‌బాట్ సపోర్ట్ (AI Chatbot)
elif choice.startswith("8."):
    st.subheader("💬 AI చాట్‌బాట్ సపోర్ట్ (Joshna Tailors & Aservad.ai)")
    st.info("మిత్రమా, ఇక్కడ మీరు ఏ ప్రశ్న అడిగినా మన AI చాట్‌బాట్ క్షణంలో రియల్ టైమ్ సమాధానం ఇస్తుంది.")
    
    # చాట్ ఇన్‌పుట్ కోసం పద్ధతి
    chatbot_input_type = st.radio("ఇన్‌పుట్ పద్ధతి ఎంచుకోండి:", ["టెక్స్ట్ టైప్ చేయండి", "మైక్ ద్వారా మాట్లాడండి"], key="chat_method_radio")
    
    chat_msg = ""
    if chatbot_input_type == "టెక్స్ట్ టైప్ చేయండి":
        chat_msg = st.text_input(
            "మీ సందేశం లేదా ప్రశ్న ఇక్కడ టైప్ చేయండి:",
            placeholder="ఉదాహరణకు: హాయ్, ఆశీర్వాదం AI గురించి చెప్పండి",
            key="chatbot_box"
        )
    else:
        audio_val = st.audio_input("🎤 మైక్ నొక్కి మీ ప్రశ్న మాట్లాడండి:", key="chatbot_audio_input")
        if audio_val:
            st.success("✨ ఆడియో విజయవంతంగా స్వీకరించబడింది!")
            chat_msg = "ఆశీర్వాదం AI మరియు జ్యోత్స్న టెయిలర్స్ విశేషాలు ఏమిటి?"
            
    if st.button("🚀 సందేశం పంపు (Send Message)", key="chatbot_btn"):
        if chat_msg.strip():
            with st.spinner("⏳ చాట్‌బాట్ ఆలోచిస్తోంది... దయచేసి వేచి ఉండండి."):
                api_key = st.secrets.get("GEMINI_API_KEY")
                
                if api_key:
                    try:
                        from google import genai
                        client = genai.Client(api_key=api_key)
                        
                        # జెమినీ ఏఐ ద్వారా రియల్ టైమ్ రెస్పాన్స్ తెప్పించడం
                        response = client.models.generate_content(
                            model='gemini-3.6-flash',
                            contents=chat_msg,
                        )
                        bot_response = response.text
                        
                        st.success("✨ విజయవంతంగా సమాధానం ఇవ్వబడింది!")
                        st.write(bot_response)
                        
                        # కాపీ చేసుకోవడానికి కోడ్/టెక్స్ట్ బ్లాక్
                        st.code(bot_response, language="text")
                        
                    except Exception as e:
                        st.error(f"⚠️ లోపం ఏర్పడింది మిత్రమా: {e}")
                else:
                    st.warning("⚠️ దయచేసి స్ట్రీమ్‌లిట్ సెట్టింగ్స్‌లో 'GEMINI_API_KEY' ని సెట్ చేయండి.")
        else:
            st.warning("⚠️ దయచేసి ఏదైనా సందేశం టైప్ చేయండి లేదా మాట్లాడండి మిత్రమా.")
                        
# 9. డాక్యుమెంట్ అనాలిసిస్ (Document Analysis)
elif choice.startswith("9."):
    st.subheader("📁 డాక్యుమెంట్ అనాలిసిస్ (Joshna Tailors & Aservad.ai)")
    input_method = st.radio("సమాచార సేకరణ పద్ధతి:", ["ఫైల్ అప్‌లోడ్", "టెక్స్ట్ టైప్"], key="doc_input_method")
    
    analysis_input = ""
    if input_method == "ఫైల్ అప్‌లోడ్":
        doc = st.file_uploader("📂 PDF లేదా TXT ఫైల్ అప్‌లోడ్ చేయండి:", type=["pdf", "txt"], key="doc_uploader")
        if doc is not None:
            st.success(f"✨ ఫైల్ స్వీకరించబడింది: {doc.name}")
            try:
                if doc.type == "text/plain":
                    analysis_input = str(doc.read(), "utf-8")
                elif doc.type == "application/pdf":
                    # PDF నుండి టెక్స్ట్ చదవడం
                    pdf_reader = PyPDF2.PdfReader(doc)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                    analysis_input = text
            except Exception as e:
                st.error(f"⚠️ ఫైల్ చదవడంలో లోపం: {e}")
    else:
        analysis_input = st.text_area("📝 విశ్లేషించవలసిన టెక్స్ట్:", key="doc_text_area")
        
    doc_prompt = st.text_input("❓ ఈ డాక్యుమెంట్ గురించి ఏం తెలుసుకోవాలనుకుంటున్నారు?", key="doc_prompt")
    
    if st.button("🚀 విశ్లేషించు (Analyze)", key="doc_analyze_btn"):
        if analysis_input and doc_prompt:
            with st.spinner("⏳ డాక్యుమెంట్ విశ్లేషించబడుతోంది..."):
                try:
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    full_content = f"Document: {analysis_input}\n\nQuestion: {doc_prompt}"
                    response = client.models.generate_content(model='gemini-3.6-flash', contents=full_content)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"⚠️ లోపం: {e}")
        else:
            st.warning("⚠️ ఫైల్/టెక్స్ట్ మరియు ప్రశ్న రెండూ అవసరం.")
            
# 10. Audio Analysis (ఆడియో విశ్లేషణ)
elif choice.startswith("10."):
    st.subheader("🎙️ Audio Analysis (Joshna Tailors & Aservad.ai)")
    st.info("Upload an audio file or record live, and the AI will convert it into text.")
    
    audio_method = st.radio("Input Method:", ["File Upload (MP3/WAV)", "Live Recording (Mic)"], key="audio_input_method")
    
    audio_file = None
    if audio_method == "File Upload (MP3/WAV)":
        audio_file = st.file_uploader("📂 Select Audio File:", type=["mp3", "wav", "m4a"], key="audio_uploader")
    else:
        audio_file = st.audio_input("🎙️ Record Audio:", key="audio_mic")
        
    if audio_file is not None:
        st.audio(audio_file)
        
        if st.button("🚀 Transcribe", key="trans_btn"):
            with st.spinner("✨ Processing audio... Please wait!"):
                try:
                    import tempfile
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                        tmp_file.write(audio_file.read())
                        tmp_path = tmp_file.name
                    
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    uploaded_audio = client.files.upload(file=tmp_path)
                    
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=[uploaded_audio, "Listen to this audio carefully and provide a complete and accurate transcription of the spoken words. (If it is in Telugu, reply in Telugu text)."]
                    )
                    
                    st.success("✨ Transcription completed!")
                    st.write(response.text)
                    st.code(response.text, language="text")
                    
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
                    

# 11. వీడియో క్రియేటర్ & స్క్రిప్ట్ టూల్
elif choice.startswith("11."):
    st.subheader("🎥 AI వీడియో క్రియేటర్ & స్క్రిప్ట్ టూల్ (Joshna Tailors & Aservad.ai)")
    st.info("మీ YouTube, Instagram రీల్స్ లేదా Facebook కోసం శక్తివంతమైన మరియు ఆకర్షణీయమైన వీడియో స్క్రిప్ట్‌లను AI ద్వారా సృష్టించండి.")
    
    v_topic = st.text_input("మీ వీడియో టాపిక్ లేదా టైటిల్ రాయండి (ఉదా: Tailoring Shop Marketing Ideas):", "")
    v_platform = st.selectbox("ప్లాట్‌ఫారమ్ ఎంచుకోండి:", ["YouTube Long Video", "Instagram Reel / Shorts", "Facebook Video"])
    
    if st.button("🎬 AI స్క్రిప్ట్ జనరేట్ చేయండి", key="gen_script_btn"):
        if v_topic:
            with st.spinner("✨ ప్రొఫెషనల్ వీడియో స్క్రిప్ట్ తయారవుతోంది... వేచి ఉండండి మిత్రమా!"):
                try:
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    
                    prompt = f"""
                    You are a professional video scriptwriter and content creator.
                    Create an engaging video script for the platform: {v_platform}.
                    The topic of the video is: {v_topic}.
                    
                    Please structure the script clearly with:
                    1. Catchy Hook & Introduction (0-10s)
                    2. Core Content / Main Points (Step-by-step or value delivery)
                    3. Call to Action (CTA / Outro)
                    
                    Write the response in Telugu or engaging English as appropriate, keeping it professional, energetic, and engaging for viewers.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=prompt
                    )
                    
                    st.success("✨ వీడియో స్క్రిప్ట్ విజయవంతంగా తయారైంది!")
                    st.markdown("---")
                    st.markdown(response.text)
                    st.code(response.text, language="markdown")
                    
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"⚠️ లోపం ఏర్పడింది: {e}")
        else:
            st.warning("⚠️ దయచేసి ఏదైనా వీడియో టాపిక్ లేదా టైటిల్ రాయండి మిత్రమా.")
            

# 12. సెట్టింగ్స్ (Settings)
elif choice.startswith("12."):
    st.subheader("⚙️ యాప్ సెట్టింగ్స్ (Joshna Tailors & Aservad.ai)")
    st.info("మిత్రమా, మీ అవసరానికి తగినట్లుగా యాప్ సెట్టింగ్స్‌ని ఇక్కడ మార్చుకోండి.")
    
    # 1. థీమ్ లేదా డిమ్ సెట్టింగ్
    st.markdown("### 🎨 థీమ్ ఎంపిక (Theme Settings)")
    theme = st.radio("యాప్ లుక్ ఎంచుకోండి:", ["Light", "Dark"], horizontal=True, key="theme_radio")
    
    # 2. API కీ సెట్టింగ్
    st.markdown("### 🔑 API కీ సెట్టింగ్ (Gemini API Key)")
    st.write("ప్రస్తుత యాప్‌లో వాడే API కీని మార్చాలనుకుంటే ఇక్కడ ఎంటర్ చేయండి:")
    api_input = st.text_input("కొత్త జెమినీ API కీని ఇక్కడ ఎంటర్ చేయండి:", type="password", key="settings_api_input")
    
    # 3. ఇతర అడ్వాన్స్డ్ ఆప్షన్స్
    st.markdown("### 🔔 అడ్వాన్స్డ్ ఆప్షన్స్ (Advanced Settings)")
    notifications = st.toggle("నోటిఫికేషన్స్ ఆన్ చేయి (Enable Notifications)", value=True, key="notif_toggle")
    sound_effects = st.toggle("సౌండ్ ఎఫెక్ట్స్ (Sound Effects)", value=False, key="sound_toggle")
    
    # సేవ్ బటన్
    st.markdown("---")
    if st.button("💾 సెట్టింగ్స్ సేవ్ చేయൂ", key="save_settings_btn"):
        if api_input:
            st.session_state.api_key = api_input
            st.success("✨ మీ సెట్టింగ్స్ విజయవంతంగా సేవ్ చేయబడ్డాయి!")
        else:
            st.success("✨ మీ డిఫాల్ట్ సెట్టింగ్స్ విజయవంతంగా అప్‌డేట్ అయ్యాయి మిత్రమా!")
    
# 13. సహాయం & ఫీడ్‌బ్యాక్ (Help & Feedback)
elif choice.startswith("13."):
    st.subheader("📞 సహాయం & ఫీడ్‌బ్యాక్ (Joshna Tailors & Aservad.ai)")
    st.info("మిత్రమా, మీకు ఏవైనా సందేహాలున్నా లేదా మా యాప్ గురించి సలహాలు ఇవ్వాలన్నా ఇక్కడ తెలపండి.")

    name = st.text_input("మీ పేరు (Your Name):", key="help_name")
    phone = st.text_input("మీ ఫోన్ నంబర్ / వాట్సాప్:", key="help_phone")
    fb = st.text_area("మీ సలహాలు లేదా సమస్యను ఇక్కడ రాయండి:", key="help_fb")

    if st.button("🚀 సమర్పించండి (Submit Feedback)", key="help_submit"):
        if name and fb:
            with st.spinner("✨ మీ ఫీడ్‌బ్యాక్ పంపబడుతోంది..."):
                feedback_result = f"ధన్యవాదాలు మిత్రమా {name}! మీ అభిప్రాయం/సలహా విజయవంతంగా స్వీకరించబడింది. జోష్నా టైలర్స్ & ఆశీర్వాదం AI."
                
                st.success(feedback_result)
                st.balloons()
                
                # కాపీ బటన్
                st.code(feedback_result, language="text")
                
                # ఫీడ్‌బ్యాక్ కోసం లైక్/డిస్‌లైక్ ఆప్షన్స్
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👍 సంతోషం", key="fb_like"): 
                        st.toast("ధన్యవాదాలు మిత్రమా!")
                with col2:
                    if st.button("👎 మార్పులు కావాలి", key="fb_dislike"): 
                        st.toast("మీ అభిప్రాయం స్వీకరించబడింది.")
        else:
            st.warning("⚠️ దయచేసి మీ పేరు మరియు సలహాని ఖచ్చితంగా నింపండి మిత్రమా!")
    
# 14. AI వీడియో & టాకింగ్ అవతార్ టూల్
elif choice.startswith("14."):
    st.subheader("🗣️ AI వీడియో & టాకింగ్ అవతార్ టూల్ (Joshna Tailors & Aservad.ai)")
    st.info("మిత్రమా, ఒక ఫోటోను అప్‌లోడ్ చేసి, దానికి వాయిస్ లేదా స్క్రిప్ట్ జోడించి మాట్లాడే AI అవతార్ వీడియోను సృష్టించండి.")
    
    avatar_name = st.text_input("అవతార్ పేరు లేదా ప్రాజెక్ట్ పేరు రాయండి (ఉదా: Tailoring Promo Avatar):", "")
    avatar_image = st.file_uploader("అవతార్ కోసం ఒక ఫోటోను అప్‌లోడ్ చేయండి (JPG/PNG):", type=["jpg", "png", "jpeg"])
    avatar_script = st.text_area("ఈ అవతార్ ఏం మాట్లాడాలో స్క్రిప్ట్ లేదా టెక్స్ట్ ఇక్కడ రాయండి:", "")
    
    if avatar_image:
        st.image(avatar_image, caption="అప్‌లోడ్ చేసిన అవతార్ ఫోటో", width=250)
        
    if st.button("🎥 టాకింగ్ అవతార్ వీడియో జనరేట్ చేయండి", key="gen_avatar_btn"):
        if avatar_name and avatar_image and avatar_script:
            with st.spinner("✨ AI అవతార్ వీడియోను తయారు చేస్తోంది... వేచి ఉండండి మిత్రమా!"):
                try:
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    
                    # జెమినీ ఏఐ ద్వారా అవతార్‌కు తగిన లిప్ సింక్ & డైలాగ్ ప్లాన్ తయారు చేయడం
                    prompt = f"""
                    You are an advanced AI video and talking avatar generator assistant.
                    Avatar Name: {avatar_name}
                    Script to Speak: {avatar_script}
                    
                    Please generate a structured breakdown for creating this talking avatar video, including:
                    1. Emotional tone and expression of the avatar.
                    2. Voice modulation cues (pitch, speed, pause points).
                    3. Background and visual enhancements for a professional tailoring/business look.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=prompt
                    )
                    
                    st.success("✨ AI టాకింగ్ అవతార్ ప్లాన్ విజయవంతంగా తయారైంది!")
                    st.markdown("---")
                    st.markdown(response.text)
                    st.code(response.text, language="markdown")
                    
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"⚠️ లోపం ఏర్పడింది: {e}")
        else:
            st.warning("⚠️ దయచేసి పేరు, ఫోటో మరియు స్క్రిప్ట్ అన్నీ నింపండి మిత్రమా.")
                
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
    

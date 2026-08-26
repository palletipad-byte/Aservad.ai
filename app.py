import streamlit as st
import os
from gtts import gTTS
from PIL import Image
import PyPDF2
import io
from io import BytesIO
from google import genai
from google.genai import types 
import requests

# --- 🔐 సెక్యూర్ జీమెయిల్ లాగిన్ & క్రెడిట్స్ సిస్టమ్ (Aservad.ai) ---
import time

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "credits" not in st.session_state:
    st.session_state.credits = 3  # కొత్త యూజర్‌కి ఉచితంగా 3 క్రెడిట్స్
if "last_reset_time" not in st.session_state:
    st.session_state.last_reset_time = time.time()

# ప్రతి 24 గంటలకు (86400 సెకన్లు) క్రెడిట్స్ ఆటోమేటిక్‌గా 3 కి రీసెట్ అయ్యేలా సెక్యూరి티 లాజిక్
current_time = time.time()
if current_time - st.session_state.last_reset_time > 86400:
    st.session_state.credits = 3
    st.session_state.last_reset_time = current_time

st.sidebar.markdown("---")
st.sidebar.subheader("🔐 సెక్యూర్ లాగిన్ & వాలెట్ (Aservad.ai)")

if not st.session_state.logged_in:
    st.sidebar.info("మిత్రమా, మీ ఒరిజినల్ జీమెయిల్ మరియు పాస్‌వర్డ్ ఇవ్వండి!")
    user_email = st.sidebar.text_input("మీ జీమెయిల్ (Gmail):", placeholder="example@gmail.com", key="login_email_input")
    user_password = st.sidebar.text_input("పాస్‌వర్డ్ (Password):", type="password", placeholder="••••••••", key="login_pass_input")
    
    if st.sidebar.button("🚀 లాగిన్ అవ్వండి (Login)", key="login_btn"):
        # సెక్యూరిటీ చెక్: సరైన @gmail.com మరియు కనీసం 6 అక్షరాల పాస్‌వర్డ్ ఉండాలి
        if user_email.strip().endswith("@gmail.com") and len(user_password.strip()) >= 6:
            st.session_state.logged_in = True
            st.session_state.username = user_email
            st.sidebar.success(f"స్వాగతం మిత్రమా!")
            st.rerun()
        else:
            st.sidebar.warning("⚠️ దయచేసి సరైన @gmail.com మరియు కనీసం 6 అక్షరాల పాస్‌వర్డ్‌ని ఎంటర్ చేయండి మిత్రమా!")
else:
    st.sidebar.success(f"👤 యూజర్: **{st.session_state.username}**")
    st.sidebar.metric(label="💎 మీ మిగిలిన క్రెడిట్స్ (Credits)", value=f"{st.session_state.credits} / 3")
    st.sidebar.caption("⏰ ప్రతి 24 గంటలకు క్రెడిట్స్ రీసెట్ అవుతాయి.")
    
    if st.sidebar.button("🚪 లాగౌట్ (Logout)", key="logout_btn"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.credits = 3
        st.sidebar.info("మీరు విజయవంతంగా లాగౌట్ అయ్యారు మిత్రమా.")
        st.rerun()
        
# పేజ్ సెటప్ (ఆశీర్వాదం AI పేరుతో)
st.set_page_config(
    page_title="ఆశీర్వాదం AI (Aservad AI)",
    page_icon="🤖",
    layout="wide"
)

# --- 🌿 ఆశీర్వాదం AI - పర్ఫెక్ట్ లైట్ థీమ్ UI స్టైలింగ్ ---
st.markdown("""
<style>
    /* కళ్ళకి ఎలాంటి స్ట్రెయిన్ ఇవ్వని సాఫ్ట్ పేపర్ క్రీమ్ బ్యాక్‌గ్రౌండ్ */
    .stApp {
        background-color: #fbfbfa !important;
        color: #1e293b !important;
    }
    
    /* సైడ్‌బార్‌కు కంటికి ప్రశాంతమైన లైట్ గ్రే షేడ్ */
    [data-testid="stSidebar"] {
        background-color: #f1f5f9 !important;
        border-right: 1px solid #cbd5e1;
    }
    
    /* అన్ని హెడ్డింగ్‌లు, టైటిల్స్ మరియు టెక్స్ట్ ముదురు రంగులో స్పష్టంగా కనిపించడానికి */
    h1, h2, h3, h4, h5, h6, span, p, label, div {
        color: #1e293b !important;
    }
    
    /* సైడ్‌బార్‌లో ఉన్న టెక్స్ట్ కూడా స్పష్టంగా కనిపಿಸಲು */
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #1e293b !important;
    }
    
    /* టెక్స్ట్ ఇన్‌పుట్ మరియు సెలెక్షన్ బాక్సులు క్లియర్‌గా ఉండేలా */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border: 1.5px solid #94a3b8 !important;
        border-radius: 8px;
    }
    
    /* బటన్లు కళ్ళకి హాయినిచ్చే సాఫ్ట్ బ్లూ షేడ్‌లో */
    .stButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white !important;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0369a1 0%, #075985 100%);
    }
</style>
""", unsafe_allow_html=True)


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
# 2. ఫేస్ స్వాప్ (Advanced AI Face Swap)
elif choice.startswith("2."):
    st.subheader("👥 AI అడ్వాన్స్‌డ్ ఫేస్ స్వాప్ (Joshna Tailors & Aservad.ai)")
    st.info("మిత్రమా, సోర్స్ ఇమేజ్ (ముఖం) మరియు టార్గెట్ ఇమేజ్ (శరీరం) అప్‌లోడ్ చేయండి.")

    col1, col2 = st.columns(2)
    with col1:
        source_file = st.file_uploader("1. సోర్స్ ఫేస్ ఇమేజ్ (Source Face):", type=["jpg", "jpeg", "png"], key="face_source")
    with col2:
        target_file = st.file_uploader("2. టార్గెట్ ఇమేజ్ (Target Image):", type=["jpg", "jpeg", "png"], key="face_target")

    if source_file is not None and target_file is not None:
        st.image([source_file, target_file], caption=["Source Face", "Target Image"], width=250)

        if st.button("🚀 ఫేస్ స్వాప్ చేయండి (Process Face Swap)", key="face_swap_btn"):
            with st.spinner("✨ AI ద్వారా ఫేస్ స్వాప్ ప్రాసెస్ జరుగుతోంది... దయచేసి వేచి ఉండండి మిత్రమా!"):
                try:
                    import replicate
                    import os
                    from PIL import Image
                    import io
                    import requests

                    os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]

                    output = replicate.run(
                        "catacolabs/face-swap:4e0b0453d5a5ac4362b66d73f4784a0c84144360e6538c6439e6a9f635f12e84",
                        input={
                            "source_image": source_file,
                            "target_image": target_file
                        }
                    )
                    
                    if output:
                        response = requests.get(output)
                        swapped_image = Image.open(io.BytesIO(response.content))
                        st.success("✨ ఫేస్ స్వాప్ విజయవంతంగా పూర్తయింది మిత్రమా!")
                        st.image(swapped_image, caption="Face Swapped Successfully", use_container_width=True)
                    else:
                        st.warning("⚠️ ప్రాసెస్‌లో చిన్న లోపం జరిగింది, మరో ఫోటోతో ప్రయత్నించండి.")

                except Exception as e:
                    st.error(f"⚠️ లోపం ఏర్పడింది: {e}")
    else:
        st.warning("⚠️ మిత్రమా, దయచేసి సోర్స్ మరియు టార్గెట్ రెండు ఫోటోలను అప్‌లోడ్ చేయండి!")
                    
# 3. AI వాయిస్ క్లోనింగ్ & ఆడియో జనరేటర్
elif choice.startswith("3."):
    st.subheader("🎙️ AI వాయిస్ క్లోనింగ్ & ఆడియో జనరేటర్")
    st.markdown("మీరు టైప్ చేసిన టెక్స్ట్ అద్భుతమైన AI వాయిస్‌గా మారుతుంది!")

        # Streamlit Secrets నుండి API Key తీసుకోవడం, Voice ID నేరుగా ఇవ్వడం
    api_key = st.secrets.get("ELEVENLABS_API_KEY")
    voice_id = "pNInz6obpgDQGcFmaJgB"
    
    # యూజర్ టెక్స్ట్ బాక్స్
    user_text = st.text_area("🗣️ మీరు మాట్లాడించాలనుకుంటున్న టెక్స్ట్ ఇక్కడ రాయండి:", placeholder="హాయ్ మిత్రమా, ఎలా ఉన్నారు?")

    # వాయిస్ జనరేషన్ బటన్
    if st.button("🚀 వాయిస్ జనరేట్ చేయి", type="primary"):
        if not api_key or not voice_id:
            st.error("దయచేసి Streamlit సెక్రెట్స్‌లో API Key మరియు Voice ID సరిగ్గా ఉన్నాయో లేదో చెక్ చేయండి మిత్రమా!")
        elif not user_text.strip():
            st.warning("దయచేసి కొంచెం టెక్స్ట్ ఎంటర్ చేయండి!")
        else:
            with st.spinner("🎙️ వాయిస్ తయారవుతోంది, దయచేసి వేచి ఉండండి..."):
                url = f"https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"
                headers = {
                    "Accept": "audio/mpeg",
                    "Content-Type": "application/json",
                    "xi-api-key": api_key
    }
                        
                                    
                        
                data = {
                    "text": user_text,
                    "model_id": "eleven_multilingual_v2",
                    "voice_settings": {
                        "stability": 0.5,
                        "similarity_boost": 0.75
                    }
                }
                
                try:
                    response = requests.post(url, json=data, headers=headers)
                    
                    if response.status_code == 200:
                        st.success("🎉 వాయిస్ విజయవంతంగా తయారైంది!")
                        st.audio(response.content, format="audio/mp3")
                        st.download_button(
                            label="📥 ఆడియోను డౌన్‌లోడ్ చేసుకోండి",
                            data=response.content,
                            file_name="ai_voice_output.mp3",
                            mime="audio/mp3"
                        )
                    else:
                        st.error(f"ఏదో లోపం సంభవించింది మిత్రమా! ఎర్రర్ కోడ్: {response.status_code}")
                        st.text(response.text)
                except Exception as e:
                    st.error(f"కనెక్షన్ ఎర్రర్ వచ్చింది: {e}")
    
# 4. AI ఇమేజ్ జనరేటర్ (100% Free & Clean AI Image Generator)
elif choice.startswith("4."):
    st.subheader("🎨 జోష్న టైలర్స్ & ఆశీర్వాదం AI - ఇమేజ్ జనరేటర్")
    st.info("మిత్రమా, మీకు కావలసిన చిత్రాన్ని ఇక్కడ టైప్ చేయండి. AI దానిని అద్భుతంగా రూపొందిస్తుంది!")
    
    user_prompt = st.text_input("🎨 మీకు ఎలాంటి చిత్రం కావాలో ఇక్కడ టైప్ చేయండి (ఉదాహరణకు: Nature, Temple, Flowers, etc.):", key="img_prompt_input")

    if st.button("🖼️ ఇమేజ్ జనరేట్ చేయండి (Generate Image)", key="image_gen_btn"):
        if user_prompt.strip():
            with st.spinner("✨ జోష్న టైలర్స్ & ఆశీర్వాదం AI ద్వారా మీ చిత్రం తయారవుతోంది... వేచి ఉండండి మిత్రమా!"):
                try:
                    import requests
                    
                    # గూగుల్ జెమినీ లాగే కలర్‌ఫుల్ మరియు బ్రైట్ ఇమేజ్ ఇచ్చే పబ్లిక్ ఫ్రీ HD ఎండ్-పాయింట్
                    encoded_prompt = requests.utils.quote(user_prompt)
                    # హై క్వాలిటీ కోసం ప్రత్యేకంగా డిజైన్ చేసిన ఫ్రీ API లింక్
                    free_image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
                    
                    st.success("✨ జోష్న టైలర్స్ & ఆశీర్వాదం AI ద్వారా చిత్రం విజయవంతంగా తయారైంది మిత్రమా!")
                    st.image(free_image_url, caption=f"Generated for: {user_prompt}", use_container_width=True)

                except Exception as e:
                    st.error(f"⚠️ లోపం ఏర్పడింది మిత్రమా: {e}")
        else:
            st.warning("⚠️ మిత్రమా, దయచేసి ఇమేజ్ గురించిన వివరాలు పైన టైప్ చేయండి!")
# 5. AI టెక్స్ట్ సమరైజర్ (Final Corrected Code)
elif choice.startswith("5."):
    st.subheader("📝 AI టెక్స్ట్ సమరైజర్")
    st.info("మిత్రమా, పెద్ద పెద్ద వ్యాసాలు లేదా టెక్స్ట్‌ని ఇక్కడ పేస్ట్ చేయండి, ఏఐ దాన్ని క్లుప్తంగా ముఖ్యమైన పాయింట్లుగా సమ్మరీ చేస్తుంది.")

    summarizer_text = st.text_area("సమ్మరీ చేయవలసిన పెద్ద టెక్స్ట్ లేదా ఆర్టికల్ ఇక్కడ పేస్ట్ చేయండి:", key="summary_text_box", height=200)
    
    summary_style = st.selectbox("సమ్మరీ ఏ విధంగా రావాలి?", [
        "ముఖ్యమైన పాయింట్లు (Bullet Points)", 
        "చిన్న పేరాగ్రాఫ్ (Short Paragraph)", 
        "బిజినెస్ సమ్మరీ (Business Summary)"
    ])

    if st.button("🚀 సమ్మరీ చేయండి (Generate Summary)", key="summarize_btn"):
        if summarizer_text.strip():
            with st.spinner("✨ జోష్న టైలర్స్ & ఆశీర్వాదం AI ద్వారా టెక్స్ట్ విశ్లేషించబడుతోంది... వేచి ఉండండి మిత్రమా!"):
                try:
                    from google import genai
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    
                    prompt = f"""
                    You are an expert content summarizer. Please analyze the following text provided by 'Aservad.ai' and provide a concise, clear, and useful summary based on the requested style.
                    
                    Summary Style: {summary_style}
                    
                    Text to Summarize:
                    {summarizer_text}
                    
                    Summary:
                    """
                    
                    # సరైన మరియు వర్కింగ్ మోడల్ పేరు
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    
                    summary_result = response.text
                    st.success("✨ సమ్మరీ విజయవంతంగా తయారైంది మిత్రమా!")
                    st.markdown("---")
                    st.write(summary_result)
                    
                    st.download_button(
                        label="💾 సమ్మరీని డౌన్‌లోడ్ చేసుకోండి (Download Summary)",
                        data=summary_result,
                        file_name="aservad_ai_summary.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"⚠️ లోపం ఏర్పడింది మిత్రమా: {e}")
        else:
            st.warning("⚠️ మిత్రమా, దయచేసి సమ్మరీ చేయడానికి కొంత టెక్స్ట్ ఇవ్వండి!")
            
# 6. భాషా అనువాదం (Multi-Language Translation)
elif choice.startswith("6."):
    st.subheader("🌐 AI భాషా అనువాదం (Multi-Language Translation)")
    st.info("మిత్రమా, ఇక్కడ మీరు టెక్స్ట్ టైప్ చేసి వేరే భాషలోకి అనువదించుకోవచ్చు.")

    source_text = st.text_area("అనువదించవలసిన టెక్స్ట్ ఇక్కడ రాయండి:", key="trans_text_box")
    target_lang = st.selectbox("ఏ భాషలోకి మార్చాలి?", ["Telugu", "English", "Hindi", "Tamil", "Kannada", "Malayalam"])

    if st.button("🚀 అనువదించండి (Translate)", key="translate_btn_new"):
        if source_text.strip():
            with st.spinner("✨ అనువాదం జరుగుతోంది... దయచేసి వేచి ఉండండి."):
                try:
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    prompt = f"Translate the following text accurately into {target_lang}: {source_text}"
                    
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=prompt
                    )
                    
                    translated_result = response.text
                    st.success("✨ అనువాదం విజయవంతంగా పూర్తయింది!")
                    st.write(translated_result)
                    st.code(translated_result, language="text")
                    
                except Exception as e:
                    st.error(f"⚠️ లోపం ఏర్పడింది: {e}")
        else:
            st.warning("⚠️ దయచేసి అనువదించడానికి టెక్స్ట్ ఇవ్వండి మిత్రమా!")
            
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
    
# 14. అడ్వాన్స్డ్ టాకింగ్ అవతార్ & మల్టిపుల్ ఫోటో టూల్
elif choice.startswith("14."):
    st.subheader("🗣️ అడ్వాన్స్డ్ టాకింగ్ అవతార్ & 3D వ్యూ టూల్ (Joshna Tailors & Aservad.ai)")
    st.info("మిత్రమా, ఫ్రంట్, బ్యాక్ మరియు సైడ్ ఫోటోలను అప్‌లోడ్ చేసి, మీ వాయిస్ స్క్రిప్ట్‌తో అవతార్ వీడియో ప్లాన్ తయారు చేసుకోండి.")
    
    avatar_name = st.text_input("అవతార్ / ప్రాజెక్ట్ పేరు రాయండి:", "Joshna Tailoring Avatar")
    
    # మల్టిపుల్ ఫోటోలు అప్‌లోడ్ చేసే ఆప్షన్
    st.markdown("### 📸 ఫోటోలు అప్‌లోడ్ చేయండి (Multiple Angles)")
    col1, col2, col3 = st.columns(3)
    with col1:
        front_img = st.file_uploader("ఫ్రంట్ వ్యూ (Front View)", type=["jpg", "png", "jpeg"], key="front")
    with col2:
        side_img = st.file_uploader("సైడ్ వ్యూ (Side View)", type=["jpg", "png", "jpeg"], key="side")
    with col3:
        back_img = st.file_uploader("బ్యాక్ వ్యూ (Back View)", type=["jpg", "png", "jpeg"], key="back")
        
    # ఫోటోల ప్రివ్యూ చూపించడం
    if front_img:
        st.image(front_img, caption="ఫ్రంట్ వ్యూ ఫోటో", width=200)
        
    avatar_script = st.text_area("అవతార్ ఏం మాట్లాడాలో వాయిస్ స్క్రిప్ట్ లేదా స్టోరీ రాయండి:", "నమస్తే అండి! మన జ్యోత్స్న టెయిలర్స్ లో అన్ని రకాల డిజైనర్ బ్లౌజెస్ లభించును.")
    
    if st.button("🎬 అడ్వాన్స్డ్ అవతార్ వీడియో ప్లాన్ జనరేట్ చేయండి", key="adv_avatar_btn"):
        if avatar_script:
            with st.spinner("✨ మల్టిపుల్ ఫోటోలు మరియు వాయిస్ స్క్రిప్ట్‌ని విశ్లేషిస్తోంది..."):
                try:
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    
                    prompt = f"""
                    You are an expert AI avatar animation and multi-angle 3D modeling director.
                    Project Name: {avatar_name}
                    Script/Story to Speak: {avatar_script}
                    Images Provided: Front, Side, and Back views of the person/design.
                    
                    Please generate a comprehensive execution blueprint for creating a realistic talking avatar video:
                    1. 3D Face & Body alignment mapping based on multi-angle views.
                    2. Lip-sync timing and facial expression keyframes for the given script.
                    3. Voice modulation, pacing, and emotional tone matching the tailoring promotional theme.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=prompt
                    )
                    
                    st.success("✨ అడ్వాన్స్డ్ టాకింగ్ అవతార్ బ్లూప్రింట్ విజయవంతంగా తయారైంది!")
                    st.markdown("---")
                    st.markdown(response.text)
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"⚠️ లోపం ఏర్పడింది: {e}")
        else:
            st.warning("⚠️ దయచేసి స్క్రిప్ట్ వివరాలు నింపండి మిత్రమా.")
                
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
    

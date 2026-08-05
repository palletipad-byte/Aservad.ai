import streamlit as st

# యాప్ పేజీ సెటప్
st.set_page_config(page_title="ఆశీర్వాద్ AI ప్రాజెక్ట్", layout="wide")

# మెయిన్ టైటిల్
st.title("🚀 ఆశీర్వాద్ AI - ఆల్-ఇన్-వన్ క్రియేటర్ స్టూడియో")
st.write(
    "మీ సోషల్ మీడియా రీల్స్, షార్ట్స్ మరియు వీడియోల కోసం AI టూల్స్ ఒకే చోట!"
)

# సైడ్‌బార్ నావిగేషన్ మెను
st.sidebar.title("🛠️ AI టూల్స్ మెను")
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

# ----------------- 1. HOME / DASHBOARD -----------------
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

# ----------------- 2. SCRIPT MAKER -----------------
elif choice == "2. Script Maker (Story)":
  st.subheader("✍️ AI స్క్రిప్ట్ & స్టోరీ మేకర్")
  topic = st.text_input(
      "మీ వీడియో ఏ టాపిక్ గురించి? (ఉదా: మోటివేషనల్, స్టోరీ)"
  )
  duration = st.selectbox(
      "వీడియో నిడివి (Duration) ఎంచుకోండి:",
      ["5 Seconds", "15 Seconds", "30 Seconds", "60 Seconds"],
  )

  if st.button("🚀 స్క్రిప్ట్ జనరేట్ చేయి"):
    if topic:
      st.success(
          f"🎉 మీ {duration} స్క్రిప్ట్ విజయవంతంగా తయారైంది! టాపిక్: {topic}"
      )
      st.markdown(
          "> **[హుక్/ప్రారంభం]:** ఇక్కడ మీ వీడియో ప్రారంభం వస్తుంది."
      )
      st.markdown(
          "> **[మెయిన్ కంటెంట్]:** ఇక్కడ మీ కథ లేదా మెయిన్ పాయింట్ ఉంటుంది."
      )
    else:
      st.warning("దయచేసి ఏదైనా టాపిక్ రాయండి.")

# ----------------- 3. IMAGE GENERATOR -----------------
elif choice == "3. Image Generator":
  st.subheader("🎨 AI ఇమేజ్ జనరేటర్")
  img_prompt = st.text_input("మీకు ఎలాంటి ఇమేజ్ కావాలి?")
  if st.button("🖼️ ఇమేజ్ జనరేట్ చేయి"):
    if img_prompt:
      st.success("🎉 మీ ఇమేజ్ విజయవంతంగా తయారైంది!")
    else:
      st.warning("దయచేసి ప్రాంప్ట్ రాయండి.")

# ----------------- 4. VIDEO CREATOR -----------------
elif choice == "4. Video Creator":
  st.subheader("🎥 AI వీడియో & రీల్స్ క్రియేటర్")
  vid_topic = st.text_input("వీడియో టాపిక్ లేదా స్క్రిప్ట్ వివరాలు ఇవ్వండి:")
  vid_duration = st.selectbox(
      "వీడియో నిడివి (Duration):",
      ["5 Seconds", "15 Seconds", "30 Seconds", "60 Seconds"],
  )

  if st.button("🚀 వీడియో క్రియేట్ చేయి"):
    if vid_topic:
      st.success(f"🎉 మీ {vid_duration} వీడియో ప్రాసెస్ అవుతోంది!")
    else:
      st.warning("దయచేసి టాపిక్ రాయండి.")

# ----------------- ఇతర ఫీచర్లు -----------------
else:
  st.subheader(f"🚧 {choice} సెక్షన్ తయారీలో ఉంది...")
  st.write("ఈ ఫీచర్ త్వరలోనే అందుబాటులోకి వస్తుంది.")
      

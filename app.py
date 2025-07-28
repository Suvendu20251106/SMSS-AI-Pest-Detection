import streamlit as st
from PIL import Image
import random

# Bengali translations
translations = {
    "en": {
        "title": "Smart Multi-crop Surveillance System (SMSS)",
        "upload": "Upload a thermal drone image",
        "detect": "Detect Pests",
        "result": "Detection Result",
        "no_pest": "No pests detected",
        "pest_found": "Pest detected in this crop!",
        "crop_type": "Crop Type: ",
        "solution": "Suggested Action: ",
    },
    "bn": {
        "title": "স্মার্ট মাল্টি-ফসল নজরদারি সিস্টেম (SMSS)",
        "upload": "থার্মাল ড্রোন ছবি আপলোড করুন",
        "detect": "পোকা শনাক্ত করুন",
        "result": "ফলাফল",
        "no_pest": "কোন পোকা পাওয়া যায়নি",
        "pest_found": "এই ফসলে পোকা শনাক্ত হয়েছে!",
        "crop_type": "ফসলের ধরণ: ",
        "solution": "পরামর্শকৃত পদক্ষেপ: ",
    }
}

# Language switch
lang = st.sidebar.radio("Language / ভাষা", ["English", "বাংলা"])
lang_code = "en" if lang == "English" else "bn"
tr = translations[lang_code]

# UI
st.title(tr["title"])
uploaded_file = st.file_uploader(tr["upload"], type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Thermal Image", use_column_width=True)

    if st.button(tr["detect"]):
        st.subheader(tr["result"])
        # Simulate detection
        pest_detected = random.choice([True, False])
        crop = random.choice(["Wheat", "Rice", "Maize", "Apple"])
        solution = {
            "Wheat": "Use Neem spray",
            "Rice": "Apply Trichoderma",
            "Maize": "Check for armyworm, use biological control",
            "Apple": "Use pheromone traps",
        }

        if pest_detected:
            st.error(tr["pest_found"])
            st.markdown(f"**{tr['crop_type']}** {crop}")
            st.markdown(f"**{tr['solution']}** {solution[crop]}")
        else:
            st.success(tr["no_pest"])

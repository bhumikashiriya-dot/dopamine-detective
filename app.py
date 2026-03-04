import streamlit as st
import time
import random

# --- Advanced Cyber-Noir Styling ---
st.set_page_config(page_title="Dopamine Detective v2.0", page_icon="🕵️‍♂️")

st.markdown("""
    <style>
    .main { background-color: #050505; color: #00ff41; }
    .stTextArea textarea { color: #00ff41 !important; background-color: #111 !important; border: 1px solid #00ff41 !important; font-size: 1.2rem; }
    .stButton>button { border: 2px solid #00ff41; background: black; color: #00ff41; font-family: 'Courier New'; }
    .stProgressBar > div > div > div > div { background-color: #00ff41; }
    .status-box { padding: 20px; border: 1px solid #00ff41; border-radius: 10px; background: #0a0a0a; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- Persistence Layer ---
if 'history' not in st.session_state:
    st.session_state.history = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# --- Sidebar: The "Rap Sheet" ---
with st.sidebar:
    st.title("📂 CRIMINAL DATABASE")
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history[-5:])):
            st.text(f"Entry {len(st.session_state.history)-i}: {entry}")
    else:
        st.write("No prior convictions... yet.")

st.title("🕵️‍♂️ DOPAMINE DETECTIVE v2.0")
st.write("---")

# --- Smart Input ---
st.write("### NEURAL INTERFACE")
user_input = st.text_area("EXPLAIN YOUR INTENT:", placeholder="The Detective is listening...", on_change=None)

if st.button("EXECUTE DEEP SCAN"):
    if not user_input:
        st.error("I can't read an empty mind, kid. Type something.")
    else:
        # Calculate Typing Speed (Fatigue Detection)
        end_time = time.time()
        time_taken = end_time - st.session_state.start_time
        char_speed = len(user_input) / max(time_taken, 1)

        with st.status("🧠 Deep Neural Analysis in Progress...", expanded=True) as status:
            time.sleep(1)
            st.write("Filtering out algorithm-induced noise...")
            time.sleep(1)
            st.write("Measuring impulsivity levels...")
            time.sleep(0.5)
            status.update(label="ANALYSIS COMPLETE", state="complete", expanded=False)

        # --- Context-Aware Logic ---
        # We classify words by "Safe" vs "Trap"
        trap_keywords = ['scroll', 'reel', 'tiktok', 'shorts', 'bored', 'insta', 'fb', 'random']
        safe_keywords = ['how to', 'learn', 'recipe', 'fix', 'tutorial', 'study', 'research', 'work']
        
        trap_count = sum(1 for w in trap_keywords if w in user_input.lower())
        safe_count = sum(1 for w in safe_keywords if w in user_input.lower())
        
        # Smart Scoring Formula
        rot_score = 20 # Baseline
        rot_score += (trap_count * 30)
        rot_score -= (safe_count * 20)
        
        # Add "Fatigue" penalty if they typed too fast (meaning they are impulsive)
        if char_speed > 15: 
            rot_score += 15
            fatigue_msg = "🚨 IMPULSIVITY DETECTED: You typed that too fast. Your thumb is itching for a scroll."
        else:
            fatigue_msg = "✅ Motor control stable."

        rot_score = max(min(rot_score + random.randint(-5, 5), 100), 0)

        # --- Verdict Layout ---
        st.markdown(f'<div class="status-box">', unsafe_allow_html=True)
        st.write(f"### VERDICT: {rot_score}% BRAIN ROT")
        st.write(fatigue_msg)
        
        if rot_score > 40:
            st.session_state.history.append(f"FAILED ({rot_score}%)")
            st.error("DETECTIVE'S ORDER: Put the device down. You are hunting for a dopamine ghost.")
            st.write("**REALITY CHECK:** Name 3 things in the room you are currently in. Look at them. Breathe.")
            st.snow()
        else:
            st.session_state.history.append(f"PASSED ({rot_score}%)")
            st.success("CLEAN INTENT DETECTED. Proceed with surgical precision.")
            st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)

# Reset timer for next entry
st.session_state.start_time = time.time()
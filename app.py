
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# ------------------ ฟังก์ชัน ------------------ #

def load_data():
    df = pd.read_csv("lottery_data.csv")
    df["รางวัลที่ 1"] = df["รางวัลที่ 1"].astype(str).str.zfill(6)
    return df

def analyze_frequency(df):
    freq = {i: [0]*10 for i in range(6)}  # ตำแหน่งหลัก 0-5 (ซ้าย -> ขวา)
    for number in df["รางวัลที่ 1"]:
        for i, digit in enumerate(number):
            freq[i][int(digit)] += 1
    return freq

def plot_frequency(freq):
    for i in range(6):
        plt.figure()
        plt.bar(range(10), freq[i])
        plt.title(f"ความถี่ของหลักที่ {i+1} (จากซ้ายไปขวา)")
        plt.xlabel("เลข")
        plt.ylabel("จำนวนครั้งที่ออก")
        st.pyplot(plt)

def generate_number(freq):
    number = ""
    for i in range(6):
        weights = freq[i]
        total = sum(weights)
        probs = [w/total for w in weights]
        number += str(random.choices(range(10), weights=probs)[0])
    return number

# ------------------ ส่วนของ Streamlit App ------------------ #

st.title("🔢 โปรแกรมเดาสลากกินแบ่งรัฐบาล (รางวัลที่ 1)")

df = load_data()

with st.expander("📊 วิเคราะห์ความถี่เลขแต่ละหลัก"):
    freq = analyze_frequency(df)
    plot_frequency(freq)

if st.button("🎲 เดาเลขรางวัลที่ 1 จากสถิติ"):
    freq = analyze_frequency(df)
    guessed = generate_number(freq)
    st.success(f"เลขที่คาดว่าอาจออกคือ: 🎉 {guessed}")

st.markdown("---")
st.caption("จัดทำโดยครูคอมพิวเตอร์เพื่อการเรียนรู้ทางสถิติ ไม่รับประกันผลลัพธ์ในการเสี่ยงโชค")

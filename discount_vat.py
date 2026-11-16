 import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้าลดราคารวม VAT 7%")


price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
percent = st.number_input("กรอกส่วนลด (เปอร์เซ็น):", min_value=0.0 , value=0.0)

discount = price * (percent/100)
vat = (price - discount) * 0.07
net_price = (price - discount) + vat

st.header(f"• ราคาสินค้า: {price:.2f} บาท")
st.header(f"• เปอร์เซนส่วนลด: {percent:.2f} %")
st.header(f"• ส่วนลด: {discount:.2f} บาท")
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นาย ศุภกันต์ ม่วงทอง เลขที่ 24  ม.4/5")

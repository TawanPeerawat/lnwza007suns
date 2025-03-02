import streamlit as st
from database import UserDatabase

# สร้างอินสแตนซ์ของฐานข้อมูล
db = UserDatabase()

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Login System", page_icon="🔐", layout="centered")

# UI สำหรับ Login
st.title("🔐 ระบบเข้าสู่ระบบ")

# ฟอร์ม Login
with st.form("login_form"):
    username = st.text_input("👤 ชื่อผู้ใช้", placeholder="กรอกชื่อผู้ใช้ของคุณ")
    password = st.text_input("🔑 รหัสผ่าน", type="password", placeholder="กรอกรหัสผ่านของคุณ")
    login_button = st.form_submit_button("เข้าสู่ระบบ")

# ตรวจสอบการเข้าสู่ระบบ
if login_button:
    if db.login(username, password):
        st.success(f"✅ เข้าสู่ระบบสำเร็จ! ยินดีต้อนรับ {username}")
    else:
        st.error("❌ ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

# ฟอร์มสำหรับสมัครสมาชิก
st.subheader("📝 ยังไม่มีบัญชี? สมัครสมาชิกเลย!")
with st.form("register_form"):
    new_username = st.text_input("👤 สร้างชื่อผู้ใช้", placeholder="ตั้งชื่อผู้ใช้ของคุณ")
    new_email = st.text_input("📧 อีเมล", placeholder="กรอกอีเมลของคุณ")
    new_password = st.text_input("🔑 ตั้งรหัสผ่าน", type="password", placeholder="ตั้งรหัสผ่านของคุณ")
    register_button = st.form_submit_button("สมัครสมาชิก")

# ตรวจสอบการสมัครสมาชิก
if register_button:
    result = db.register(new_username, new_password, new_email)
    if "สำเร็จ" in result:
        st.success(result)
    else:
        st.error(result)

# ปิดการเชื่อมต่อฐานข้อมูล
db.close_connection()

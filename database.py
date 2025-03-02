from database import UserDatabase

# เชื่อมต่อฐานข้อมูล
db = UserDatabase()

# ลงทะเบียนผู้ใช้ใหม่
print(db.register("ploy_user", "password123", "ploy@example.com"))
print(db.register("john_doe", "securepass", "john@example.com"))

# ลองเข้าสู่ระบบ
if db.login("ploy_user", "password123"):
    print("✅ เข้าสู่ระบบสำเร็จ!")
else:
    print("❌ ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

# ดูรายชื่อผู้ใช้ทั้งหมด
print("\n📋 รายชื่อผู้ใช้ในระบบ:")
for user in db.view_users():
    print(user)

# อัปเดตรหัสผ่าน
print(db.update_password("john_doe", "newpass456"))

# ลบผู้ใช้
print(db.delete_user("ploy_user"))

# ปิดการเชื่อมต่อฐานข้อมูล
db.close_connection()

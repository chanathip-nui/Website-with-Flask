# App Play
App Play เป็นเว็บแอปพลิเคชันจำลองหน้าร้านค้าดิจิทัล สไตล์ Google Play สำหรับแสดงรายการแอปพลิเคชัน เกม ภาพยนตร์ และหนังสือ พัฒนาด้วย **Python Flask** พร้อมระบบตรวจสอบสิทธิ์ผู้ใช้งาน

จัดทำโดย นายชนาธิป นุ้ยสี 6810110566

## ฟีเจอร์หลัก

* **หน้าร้านค้าแยกหมวดหมู่**: แสดงรายการสินค้าแยกตาม Apps, Games, Movies และ Books
* **ระบบสมาชิก (Authentication)**: 
    * สมัครสมาชิกและเข้ารหัสผ่านอย่างปลอดภัย (Password Hashing)
    * เข้าสู่ระบบ / ออกจากระบบ (จัดการ Session ด้วย Flask-Login)
* **ระบบสิทธิ์ผู้ใช้งาน (Authorization)**: 
    * แบ่งผู้ใช้เป็นระดับ `admin` และ `user` 
    * มี Custom Decorator (`@roles_required`) สำหรับป้องกันการเข้าถึงหน้าเว็บที่ไม่ได้รับอนุญาต
* **ระบบหลังบ้าน (Admin Dashboard)**: หน้าตารางจัดการผู้ใช้งานสำหรับ Admin เพื่อแก้ไข Role ของผู้ใช้แต่ละคน
* **UI/UX**: ออกแบบส่วนแสดงผลด้วย Tailwind CSS และใช้งานไอคอนจาก Phosphor Icons

## Installation & Setup

**1. สร้างและเปิดใช้งาน Virtual Environment**

```python -m venv venv```

```venv\Scripts\activate```

**2. ติดตั้ง Dependencies**

```pip install -r requirements.txt```

**3. ตั้งค่าตัวแปรสภาพแวดล้อม (Environment Variables)**

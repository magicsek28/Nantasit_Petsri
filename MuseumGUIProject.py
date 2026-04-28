"""นันทสิทธิ์ เพชรศรี 6606611025 เลขที่ 34 
ได้ทำการใช้ Widget ดังต่อไปนี้
1. Label
2. Text
3.Radiobutton
4. Frame
5. Button
6. Scorbar
7.Entry
ได้ทำการใช้ Advance อย่างเช่น import ttk เข้ามาเพื่อใช้ในการปรับแต่งตัว combobox เพื่อให้ตัว dropdownlist ดีขึ้น
ได้ใช้ตัวย่อขนาดหน้าต่างอย่าง iconify ในหน้าต่างหน้าแรก ได้มีการใช้พวก anchor side 
เพื่อกำหนดการวางตำแหน่งของปุ่มต่างๆ ใช้ activecolorbackground เพื่อให้กดตอนเลือก radiobutton ขึ้นสีขึ้นมา

สิ่งที่แตกต่างจากในชีตเรียนอย่างเช่น :
การนำ state=readonly มาใช้ร่วมกับ ตัวโค้ด combo_time เพื่อเป็นการป้องกันไม่ให้ผู้ใช้พิมพ์ค่าเอง
ได้นำ relx=1.0 กำหนดขอบขวาสุดและ x=-50 ให้ขยับซ้าย50px เพื่อเป็นการกำหนดตำแหน่งของปุ่ม
ได้ทำการใช้ตัว protocal เพื่อดักจับขณะที่ผู้ใช้จะทำการกดปิดหน้าต่าง

หลักการทำงานของโปรแกรม
- หน้าแรกเป็นหน้า Welcome และปุ่มเข้าสู่หน้าจองบัตร
- เมื่อกดปุ่ม จะเปิดหน้าต่างใหม่ (Toplevel) สำหรับทำรายการจอง
- ผู้ใช้กรอกชื่อ เลือกประเภทบัตร เลือกรอบเวลา และจำนวนบัตร
- โปรแกรมจะคำนวณราคารวมแบบอัตโนมัติ
- เมื่อกดยืนยัน ระบบจะตรวจสอบข้อมูล และแสดงใบเสร็จผ่าน messagebox
- ในหน้าต่างใหม่ เมื่อกดกากบาทจะมีแจ้งเตือนว่าต้องการปิดใช่หรือไม่"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
#สร้างคลาสเก็บข้อมูล สร้างข้อมูล
class MuseumTicketApp:
    def __init__(self, base):
        self.base = base
        self.base.title("Reservation Magic System")
        self.base.resizable(True, True) #ทำให้มันปรับขนาดได้ทั้งแนวนอนและแนวตั้ง
        self.base.configure(bg='#f0f0f0')
        
        self.customer_name = tk.StringVar() #ตัวเก็บชื่อลูกค้า
        self.ticket_type = tk.StringVar(value="Adult") #ตัวเก็บประเภทลูกค้า
        self.timeslot = tk.StringVar(value="รอบเช้า (09:00-12:00)") #ตัวเก็บรอบเวลาเข้า
        self.quantity = tk.IntVar(value=1) #ตัวเก็บจำนวนตั๋ว
        self.total_price = tk.DoubleVar(value=0.0) #ตัวเก็บราคารวมทั้งหมด
        self.prices = {
            "Adult": 200,
            "Child": 0,
            "Foreigner": 500
        } #ตัวเก็บราคาขายตั๋ว
    
    def create_widgets(self):
        main = tk.Frame(self.base)
        main.pack()
        self.entry_name = tk.Entry(main, textvariable=self.customer_name)
        self.entry_name.pack()
        #สร้างปุ่มตัวเลือกประเภทคน
        tk.Radiobutton(main, text="Adult", variable=self.ticket_type,
                   value="Adult", command=self.calculate_price).pack()

        tk.Radiobutton(main, text="Child", variable=self.ticket_type,
                   value="Child", command=self.calculate_price).pack()

        tk.Radiobutton(main, text="Foreigner", variable=self.ticket_type,
                   value="Foreigner", command=self.calculate_price).pack()
        #ตัวเลือกจำนวนบัตรที่จะซื้อ
        tk.Spinbox(main, from_=1, to=10,
               textvariable=self.quantity,
               command=self.calculate_price).pack()
        #ทำให้มันแสดงราคาตอนที่ยังไม่กดเลือกประเภทคนซื้อว่า0บาท
        self.label_total_price = tk.Label(main, text="ราคารวม: 0 บาท")
        self.label_total_price.pack()
        #สร้างปุ่มกดคำนวณราคา
        tk.Button(main, text="ยืนยัน", command=self.confirm_booking).pack()
    
    def calculate_price(self):
        """คำนวณราคารวมตามประเภทและจำนวน"""
        customer_type = self.ticket_type.get()
        qty = self.quantity.get() 
        price_per_unit = self.prices.get(customer_type, 0)
        total = price_per_unit * qty
        self.total_price.set(total)
        #ทำให้มันแสดงราคาบน label
        price_text = f"ราคารวม: {total:,.0f} บาท (อัตรา {price_per_unit} บาท/ใบ)"
        self.label_total_price.config(text=price_text)
        
    def confirm_booking(self):
        """ยืนยันการจอง/ซื้อ และแสดงข้อมูลใน messagebox"""
        #ตรวจสอบข้อมูลว่าถูกไหมมีชื่อหรือเปล่าถ้าไม่มีชื่อให้ขึ้นแจ้งเตือน
        name = self.customer_name.get().strip()
        if name == "":
            messagebox.showwarning("ข้อมูลไม่สมบูรณ์", "กรุณากรอกชื่อผู้เข้าชม")
            return
        
        #ตรวจสอบจำนวนต้องมีการซื้ออย่างน้อย1ใบ
        qty = self.quantity.get()
        if qty < 1:
            messagebox.showwarning("จำนวนไม่ถูกต้อง", "กรุณาเลือกจำนวนบัตรอย่างน้อย 1 ใบ")
            return
        
        #ถ้าเกิดยังไม่มีการคำนวณราคาให้คำนวณค่าเริ่มต้นก่อนว่า0บาท
        if self.total_price.get() == 0.0:
            self.calculate_price()
        
        #ให้ขึ้นสรุปข้อมูลในการซื้อตั๋ว
        ticket_type_th = {
            "Adult": "ผู้ใหญ่",
            "Child": "เด็ก",
            "Foreigner": "ชาวต่างชาติ"
        }
        summary = f"=== ใบเสร็จการซื้อบัตรพิพิธภัณฑ์ ===\n\n"
        summary += f"ชื่อผู้เข้าชม: {name}\n"
        summary += f"ประเภทบัตร: {ticket_type_th[self.ticket_type.get()]}\n"
        summary += f"รอบเวลา: {self.timeslot.get()}\n"  # แก้เป็น timeslot
        summary += f"จำนวน: {qty} ใบ\n"
        summary += f"ราคารวม: {self.total_price.get():,.0f} บาท\n"
        summary += f"\nขอบคุณที่ใช้บริการ"
        #ขึ้นแจ้งเตือนว่าสำเร็จ
        messagebox.showinfo("ยืนยันการซื้อบัตร", summary)

#เริ่มต้นหน้าต่างแรก        
base = tk.Tk()
base.geometry("570x650")
base.title("Welcome to Magic-Museum")
#สร้างตัวกดย่อขยาย
def minimize():
    base.iconify()
header_frame = tk.Frame(base, bg='#2c3e50', height=100)
header_frame.pack(fill=tk.X, pady=(0, 10))
header_frame.pack_propagate(False)
title_label = tk.Label(header_frame, text="🏛️Magic-Museum🏛️",font=('Arial', 20, 'bold'), fg='white', bg='#2c3e50')
title_label.pack(pady=20)
subtitle_label = tk.Label(header_frame, text="🎫ระบบจองบัตรเข้าชมล่วงหน้า🎫",font=('Arial', 10), fg='#ecf0f1', bg='#2c3e50')
subtitle_label.pack()
#ตัวปุ่มกดย่อขยาย
button_minimize = tk.Button(header_frame, text="—", command=minimize,bg='#2c3e50', fg='white', bd=0, font=('Arial', 12))
button_minimize.place(relx=1.0, rely=0.0, x=-50, y=5)  #ไว้ด้านขวาบนปุ่มย่อ

content_frame = tk.Frame(base, bg="#cfe8e8")
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
title_label2= tk.Label(content_frame, text="รายละเอียดการจอง",font=("Arial",18,'bold'),fg= "black").pack(pady=20)

def reservation_windows(): #สร้างหน้าวินโดว์ใหม่
    top1 = tk.Toplevel()
    top1.title("Reservation System")
    top1.geometry("590x650")
    #สร้างตัวแจ้งเตือนว่าไม่จองตั๋วแล้วจิงอ่อ
    def on_close():
        warningclose = messagebox.askyesno("แจ้งเตือน","คุณแน่ใจใช่ไหมที่จะไม่จองตั๋วแล้ว แล้วออกจากหน้านี้???")
        if warningclose:
            top1.destroy()
        
    top1.protocol("WM_DELETE_WINDOW", on_close)
    #สร้างheaderในหน้าต่างใหม่
    header_frame = tk.Frame(top1, bg='#2c3e50', height=100)
    header_frame.pack(fill=tk.X, pady=(0, 10))
    header_frame.pack_propagate(False)
    title_label = tk.Label(header_frame, text="🏛️Magic-Museum🏛️",font=('Arial', 20, 'bold'), fg='white', bg='#2c3e50')
    title_label.pack(pady=20)
    subtitle_label = tk.Label(header_frame, text="🎫ระบบจองบัตรเข้าชมล่วงหน้า🎫",font=('Arial', 10), fg='#ecf0f1', bg='#2c3e50')
    subtitle_label.pack()

    content_frame = tk.Frame(top1, bg='#f0f0f0')
    content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    app = MuseumTicketApp(top1)  #สร้างตัวลูกเพื่อดึงฟังก์ชั่นในคลาสแม่ออกมาใช้นอกคลาส

    frame_name = tk.Frame(content_frame, bg='#f0f0f0')
    frame_name.pack(fill=tk.X, pady=5)
    #สร้างตัวเขียนชื่อ
    label_name = tk.Label(frame_name, text="ชื่อนามสกุล:", font=('Helvetica', 12), bg='#f0f0f0', width=15, anchor='w')
    label_name.pack(side=tk.LEFT, padx=5)
    entry_name = tk.Entry(frame_name, textvariable=app.customer_name, font=('Helvetica',12), width=30, bg="white", relief=tk.GROOVE)
    entry_name.pack(side=tk.LEFT, padx=5)

    frame_type = tk.Frame(content_frame, bg='#f0f0f0')
    frame_type.pack(fill=tk.X, pady=10)
    #สร้างปุ่มกดเลือกประเภทบัตร
    label_type = tk.Label(frame_type, text="ประเภทบัตร:", font=('Helvetica', 12), bg='#f0f0f0', width=15, anchor='w')
    label_type.pack(side=tk.LEFT, padx=5)
    rb_frame = tk.Frame(frame_type, bg='#f0f0f0')
    rb_frame.pack(side=tk.LEFT, padx=5)
    
    #ตัวปุ่มกดประเภทลูกค้า
    rb_adult = tk.Radiobutton(rb_frame,text="ผู้ใหญ่ (200 บาท)",variable=app.ticket_type,value="Adult",command=app.calculate_price,activebackground="#2980b9"
)
    rb_child = tk.Radiobutton(
    rb_frame,
    text="เด็ก (0 บาท)",
    variable=app.ticket_type,
    value="Child",
    command=app.calculate_price,
activebackground="#2980b9")
    rb_foreigner = tk.Radiobutton(
    rb_frame,
    text="ชาวต่างชาติ (500 บาท)",
    variable=app.ticket_type,
    value="Foreigner",
    command=app.calculate_price,activebackground="#2980b9"
)   
    #แปะปุ่ม
    rb_adult.pack(side=tk.LEFT, padx=10)
    rb_child.pack(side=tk.LEFT, padx=10)
    rb_foreigner.pack(side=tk.LEFT, padx=10)

    frame_time = tk.Frame(content_frame, bg='#f0f0f0')
    frame_time.pack(fill=tk.X, pady=5)
    #สร้างตัวเลือกช่วงเวลา
    label_time = tk.Label(frame_time, text="รอบเวลา:", font=('Helvetica', 12), bg='#f0f0f0', width=15, anchor='w')
    label_time.pack(side=tk.LEFT,padx=5)
    time_options = ["รอบเช้า (09:00-12:00)", "รอบบ่าย (13:00-16:00)"]

    combo_time = ttk.Combobox(frame_time, textvariable=app.timeslot, values=time_options, state="readonly", font=('Helvetica', 10), width=30)
    combo_time.pack(side=tk.LEFT,padx=5)
    
    frame_qty = tk.Frame(content_frame, bg='#f0f0f0')
    frame_qty.pack(fill=tk.X, pady=5)
    #สร้างปุ่มกดเพิ่มจำนวนบัตร
    label_qty = tk.Label(frame_qty, text="จำนวนบัตร:", font=('Helvetica', 12),bg='#f0f0f0', width=15, anchor='w')
    label_qty.pack(side=tk.LEFT, padx=5)
    spin_qty = tk.Spinbox(frame_qty,from_=1,to=10,textvariable=app.quantity,width=10,font=('Helvetica', 10),command=app.calculate_price)
    spin_qty.pack(side=tk.LEFT, padx=5)
    #ใช้appดึงฟังก์ชั่นในคลาสออกมาใช้
    app.label_total_price = tk.Label(content_frame, text="ราคารวม: 0 บาท",font=('Arial', 14, 'bold'), fg='#27ae60', bg='#f0f0f0')
    app.label_total_price.pack(pady=5)
    #ปุ่มกดยืนยัน
    button_confirm = tk.Button(content_frame, text="ยืนยันการซื้อบัตร", font=('Arial', 12, 'bold'),bg='#2ecc71', fg='white', padx=15, pady=8,command=app.confirm_booking)
    button_confirm.pack(pady=10)
#สิ้นสุดการสร้างในหน้าต่างอีกอัน

#สร้างปุ่มกดหน้าแรกเพื่อลิ้งค์ไปหน้าที่สอง  
but = tk.Button(content_frame, text="กดปุ่มเพื่อเข้าสู่หน้าการจอง", command=reservation_windows,fg='#f0f0f0',bg="#3498db",font=("Helvetica", 16),width=25,height=2)
but.pack(side=tk.BOTTOM,padx=20, pady=10, anchor="center")
#สร้างกล่องเฟรมเพื่อแปะสกอบาร์ให้ข้อมูล
box = tk.Frame(content_frame, bg="white", bd=2, relief="ridge")
box.pack(padx=40, pady=10, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(box)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(box, wrap="word", yscrollcommand=scrollbar.set, font=("Arial", 14), padx=15, pady=15)
text.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=text.yview)
content = """🏛️ ยินดีต้อนรับสู่ Magic-Museum!

✨ เตรียมตัวให้พร้อมสำหรับประสบการณ์สุดพิเศษ!
ไม่ว่าจะมากับ 👨‍👩‍👧‍👦 ครอบครัว, 👫 คู่รัก หรือ 🎒 กลุ่มเพื่อน
สถานที่ของเราพร้อมต้อนรับทุกท่านเสมอ

📸 โซนถ่ายรูป  🎭 โซนกิจกรรม  🛋️ พื้นที่พักผ่อน

━━━━━━━━━━━━━━━━━━━━━━━━━
🎫 อัตราค่าบริการบัตรเข้าชม
━━━━━━━━━━━━━━━━━━━━━━━━━

🧒 เด็ก (ส่วนสูงไม่เกิน 150 ซม.)  →  ฟรี! 🎉
🧑 ผู้ใหญ่ชาวไทย (18 ปีขึ้นไป)   →  200 บาท
🌍 ชาวต่างชาติ                     →  500 บาท

━━━━━━━━━━━━━━━━━━━━━━━━━
📋 หมายเหตุสำหรับการจอง
━━━━━━━━━━━━━━━━━━━━━━━━━

🪪 เตรียมบัตรประชาชน หรือ 📘 พาสปอร์ต
📏 เด็กที่เข้าฟรีมีจุดวัดส่วนสูง
📧 ระบบจะส่ง E-Ticket หลังจองเสร็จ
❌ ไม่สามารถยกเลิกหรือคืนเงินได้

⏰ รอบเข้าชม
🌅 รอบเช้า  09:00 - 12:00 น.
☀️ รอบบ่าย  13:00 - 16:00 น.

━━━━━━━━━━━━━━━━━━━━━━━━━
🙏 ขอบคุณที่เลือกใช้บริการ Magic-Museum
"""
text.insert("1.0", content)
text.config(state="disabled")

base.mainloop()
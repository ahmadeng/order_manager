📦 Order Manager & Sales Analysis
سیستم مدیریت و تحلیل سفارش‌ها با استفاده از Python و Pandas.
این پروژه داده‌های سفارش‌ها را از فایل JSON می‌خواند، تحلیل می‌کند و خروجی حرفه‌ای Excel تولید می‌کند.

🚀 قابلیت‌ها
خواندن سفارش‌ها از فایل JSON

محاسبه مبلغ کل هر سفارش (total = price * quantity)

گزارش کامل فروش (مجموع، میانگین، بیشترین، کمترین)

فیلتر سفارش‌ها بر اساس نام مشتری

فیلتر سفارش‌ها بر اساس حداقل مبلغ

خروجی Excel با فرمت استاندارد

ساختاردهی حرفه‌ای کد (main + utils)

📁 ساختار پروژه
Code
order_manager/
│
├── main.py
├── utils.py
├── orders.json
├── requirements.txt
└── README.md
📊 نمونه داده (orders.json)
json
[
    {"order_id": 101, "customer": "Ali", "product": "گوشی A55", "price": 25900000, "quantity": 2},
    {"order_id": 102, "customer": "Sara", "product": "Redmi Note 13", "price": 14500000, "quantity": 1},
    {"order_id": 103, "customer": "Mehdi", "product": "iPhone 13", "price": 45000000, "quantity": 1}
]
▶️ اجرای پروژه
1) نصب کتابخانه‌ها
Code
pip install -r requirements.txt
2) اجرای برنامه
Code
python main.py
📤 خروجی‌ها
orders_report.xlsx → گزارش کامل سفارش‌ها

فیلترهای قابل چاپ داخل ترمینال

🛠 تکنولوژی‌ها
Python

Pandas

JSON

Excel (openpyxl)

📌 نکات توسعه
فیلتر مشتری بدون حساسیت به حروف (case-insensitive)

امکان افزودن فیلترهای جدید (بازه قیمت، محصول، تعداد)

آماده برای توسعه به نسخه‌های حرفه‌ای‌تر (نمودار، PDF، Flask، دیتابیس)
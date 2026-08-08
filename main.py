from utils import load_orders, analyze_orders, export_excel, filter_by_customer, filter_by_price

def main():
    data = load_orders()
    df = analyze_orders(data)

    while True:
        print("\n1. فیلتر بر اساس مشتری")
        print("2. فیلتر بر اساس حداقل مبلغ سفارش")
        print("3. خروجی Excel")
        print("4. خروج")

        choice = input("انتخاب: ")

        if choice == "1":
            name = input("نام مشتری: ")
            result = filter_by_customer(df, name)
            print(result)

        elif choice == "2":
            min_price = int(input("حداقل مبلغ: "))
            result = filter_by_price(df, min_price)
            print(result)

        elif choice == "3":
            export_excel(df)

        elif choice == "4":
            break

        else:
            print("گزینه نامعتبر")

if __name__ == "__main__":
    main()

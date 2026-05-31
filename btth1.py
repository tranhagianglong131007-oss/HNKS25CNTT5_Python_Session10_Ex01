cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:

    print("""
    ------ SHOPEE CART MANAGEMENT SYSTEM ------
    1. Xem chi tiết giỏ hàng & Tính tổng tiền
    2. Thêm sản phẩm mới / Cộng dồn số lượng
    3. Cập nhật số lượng sản phẩm
    4. Xóa sản phẩm khỏi giỏ hàng
    5. Thoát chương trình
""")

    choice = input("Mời bạn nhập lựa chọn (1-5): ")

    match choice:

        case "1":

            total_quantity = 0
            total_price = 0

            print("STT | Mã SP | Tên sản phẩm | SL | Đơn giá | Thành tiền")

            for index, item in enumerate(cart_items, start=1):

                product_id = item[0]
                product_name = item[1]
                quantity = item[2]
                price = item[3]

                line_total = quantity * price

                total_quantity += quantity
                total_price += line_total

                print(f"{index} | {product_id} | {product_name} |{quantity} | {price:,}đ | {line_total:,}đ")

            print(f"Tổng số lượng sản phẩm: {total_quantity}")
            print(f"Tổng tiền thanh toán: {total_price:,}đ")

        case "2":

            new_id = input("Nhập mã sản phẩm mới: ").upper()

            flag = True

            for item in cart_items:

                if new_id == item[0]:

                    print("Sản phẩm đã tồn tại")

                    while True:

                        add_quantity = input("Nhập số lượng sản phẩm: ")

                        if add_quantity.isdigit() and int(add_quantity) > 0:

                            item[2] += int(add_quantity)
                            print("Đã cộng dồn số lượng thành công")
                            break

                        else:
                            print("Số lượng phải lớn hơn 0")

                    flag = False
                    break

            if flag == 1:

                print("Sản phẩm chưa tồn tại")

                new_product = input("Nhập tên sản phẩm mới: ")

                while True:

                    new_quantity = input("Nhập số lượng sản phẩm mới: ")

                    if new_quantity.isdigit() and int(new_quantity) > 0:

                        new_quantity = int(new_quantity)
                        break

                    else:
                        print("Số lượng phải lớn hơn 0")

                while True:

                    new_price = input("Nhập đơn giá sản phẩm: ")

                    if new_price.isdigit() and int(new_price) > 0:

                        new_price = int(new_price)
                        break

                    else:
                        print("Đơn giá phải lớn hơn 0")

                cart_items.append(
                    [new_id, new_product, new_quantity, new_price]
                )

                print("Thêm sản phẩm thành công")

        case "3":

            update_id = input("Nhập mã sản phẩm cần cập nhật: ").upper()

            found = False

            for item in cart_items:

                if update_id == item[0]:
                    found = True

                    while True:

                        new_quantity = input("Nhập số lượng mới: ")

                        if new_quantity.isdigit() and int(new_quantity) > 0:

                            item[2] = int(new_quantity)

                            print("Cập nhật thành công")
                            break

                        else:
                            print("Số lượng phải lớn hơn 0")
                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng")

        case "4":

            delete_id = input("Nhập mã sản phẩm cần xóa: ").upper()

            found = False

            for index, item in enumerate(cart_items):

                if delete_id == item[0]:

                    cart_items.pop(index)
                    print("Xóa sản phẩm thành công")

                    found = True
                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng")

        case "5":

            print("Cảm ơn bạn đã sử dụng chương trình!")
            break

"""  
input:
    lựa chọn menu
    thông tin sản phẩm khi thêm
    cart_item
output:
    Hiển thị thông tin giỏ hàng
    Thông báo hệ thống khi thêm vào báo lỗi khi nhập sai dữ liệu
"""
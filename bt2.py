playlist = []

while True:
    print("""
============================================
HỆ THỐNG QUẢN LÝ DANH SÁCH PHÁT NHẠC
============================================
1. Thêm bài hát vào danh sách phát
2. Xem danh sách phát
3. Xóa bài hát khỏi danh sách
4. Sắp xếp và Trích xuất danh sách
5. Thoát chương trình
=============================================""")
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    if choice == '1':
        print("\n--- THÊM BÀI HÁT ---")
        song_name = input("Nhập tên bài hát: ").strip()
        if song_name == "":
            print("Tên bài hát không được để trống!")
            continue

        print("1. Thêm vào cuối danh sách")
        print("2. Chèn vào vị trí bất kỳ (Index)")
        sub_choice = input("Chọn cách thêm (1-2): ").strip()

        if sub_choice == '1':
            playlist.append(song_name)
            print(f"Đã thêm bài hát '{song_name}' vào cuối danh sách.")
            print(f"Số lượng bài hát hiện tại: {len(playlist)}")
        
        elif sub_choice == '2':
            index_str = input(f"Nhập vị trí muốn chèn (0 đến {len(playlist)}): ").strip()
            
            if not index_str.isdigit():
                print("Vị trí không hợp lệ. Vui lòng nhập số nguyên dương!")
            else:
                idx = int(index_str)
                if idx < 0 or idx > len(playlist): 
                    print("Vị trí không hợp lệ.")
                else:
                    playlist.insert(idx, song_name)
                    print(f"Đã chèn bài hát '{song_name}' vào vị trí {idx}.")
                    print(f"Số lượng bài hát hiện tại: {len(playlist)}")
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")

    elif choice == '2':
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n--- PLAYLIST CỦA BẠN ---")
        for i, song in enumerate(playlist, start=1):
            print(f"{i}. {song}")
        print("------------------------")

    elif choice == '3':
        if len(playlist) == 0:
            print("🛑 Danh sách phát hiện đang trống!")
            continue

        print("\n--- XÓA BÀI HÁT ---")
        print("1. Xóa theo tên bài hát")
        print("2. Xóa theo vị trí (STT)")
        sub_choice = input("Chọn cách xóa (1-2): ").strip()

        if sub_choice == '1':
            delete_name = input("Nhập tên bài hát muốn xóa: ").strip()
            
            found = False
            for song in playlist:
                if song.lower() == delete_name.lower():
                    playlist.remove(song)
                    print(f"Đã xóa bài hát [{song}] khỏi danh sách.")
                    found = True
                    break 
            
            if not found:
                print("Không tìm thấy bài hát trong danh sách phát.")

        elif sub_choice == '2':
            print("Danh sách bài hát hiện tại:")
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")
                
            stt_str = input("Nhập số thứ tự (STT) bài hát muốn xóa: ").strip()
            
            if not stt_str.isdigit():
                print("Vị trí không hợp lệ. Vui lòng nhập số nguyên!")
            else:
                stt = int(stt_str)
                idx = stt - 1
                if idx < 0 or idx >= len(playlist):
                    print("Vị trí không hợp lệ.")
                else:
                    removed_song = playlist.pop(idx)
                    print(f"Đã xóa bài hát [{removed_song}] khỏi danh sách.")
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")

    elif choice == '4':
        if len(playlist) == 0:
            print(" Danh sách phát hiện đang trống!")
            continue

        print("\n--- SẮP XẾP & TRÍCH XUẤT ---")
        print("1. Sắp xếp danh sách theo bảng chữ cái (A-Z)")
        print("2. Nghe thử 3 bài hát đầu tiên")
        sub_choice = input("Chọn chức năng (1-2): ").strip()

        if sub_choice == '1':
            playlist.sort()
            print("Đã sắp xếp lại danh sách phát theo thứ tự chữ cái từ A-Z.")
        elif sub_choice == '2':
            print("\n--- 3 BÀI HÁT ĐẦU TIÊN ---")
            sample_songs = playlist[:3]
            for i, song in enumerate(sample_songs, start=1):
                print(f"{i}. {song}")
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")

    elif choice == '5':
        print("\nCảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên từ 1 đến 5")

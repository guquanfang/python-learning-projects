from records import add_records,view_records,total_time_record,longest_time_record,sort_record
def main():
    print("=== Learning Progress Tracker ===\n")
    while True:
        print("1.Add learning record")
        print("2.View all records")
        print("3.View total study time")
        print("4.View longest study session")
        print("5.Sort records by duration")
        print("0.exit")
        choice = input("Choose an option:")
        if choice == "1":
            add_records()
        elif choice == "2":
            view_records()
        elif choice == "3":
            total_time_record()
        elif choice == "4":
            longest_time_record()
        elif choice == "5":
            sort_record()
        elif choice == "0":
            break
        else:
            print("无效输入，重新输入")
            
if __name__ == "__main__":
    main()
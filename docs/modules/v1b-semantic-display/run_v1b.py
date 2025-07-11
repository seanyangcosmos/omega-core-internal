from controller.v1b_output_block import run_v1b_pipeline

if __name__ == "__main__":
    print("🚀 Sean Yang Core V1-B 語義互動 CLI 啟動")
    while True:
        user_input = input("請輸入語句（輸入 exit 結束）：")
        if user_input.lower() == "exit":
            print("👋 再見！")
            break
        result = run_v1b_pipeline(user_input)
        print(result)

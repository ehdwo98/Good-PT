import os

def eraseTmpFile():
    tmp_folder_path = "tmp/" 

    try:
        file_list = os.listdir(tmp_folder_path)

        for file_name in file_list:
            file_path = os.path.join(tmp_folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{file_path} 파일이 삭제되었습니다.")

        print("모든 파일 삭제가 완료되었습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")


import os
from posixpath import realpath
import dropbox
from dropbox.files import FileStatus_validator, WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        

        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root, fileName)

                relative_path = os.path.realpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = "sl.A0GSshrguygzlKzsDQcSLt20gmZmghd2ufoRA-NxltBIypmTEJLyRulPwOLqezU9pZ6SlDtQq5iEuieEQRwvbzO5kU-h8wmqTbbhSUnauAKRoU6i2brXd0d4pEYfA1gtnkaYkzA"
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer:-"))
    file_to = input("Enter the full path to upload to dropbox:-")

    TransferData.upload_files(file_from,file_to)
    print('File has been moved!!!!')

main()




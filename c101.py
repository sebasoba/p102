import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '_2nZMuGmAuMAAAAAAAAAAVNnqdUJBW0Q1o4yRM-cnW4KWGehbl-0fSjATIiLAMsY'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:")
    file_to = input("Enter the full path to upload the dropbox:")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()
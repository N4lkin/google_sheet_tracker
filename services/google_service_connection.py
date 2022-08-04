import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

from main.utils import path_to_file
from config import Settings

file = path_to_file(Settings.CREDENTIALS_FILE)
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    file,
    [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build("sheets", "v4", http=httpAuth)

# Для работы с апи Google Sheets - необходимо делать вызовы через переменную service

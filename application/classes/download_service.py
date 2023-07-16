"""
    This file contains the DownloadService class, which is responsible
    for downloading health records for the logged-in user
    in the requested format.
"""

# Imports
import os


# DownloadService Class
class DownloadService:

    def download(self):
        """Downloads the health records for the logged-in user in the requested format"""
        # Get logged-in user's id
        user_id = self.__login_service.get_loggedin_user_id()

        # Get logged-in user's uuid
        uuid = self.__login_service.get_loggedin_user_uuid()

        # Retrieve health records and record items from the database
        record_items = self.__db_manager.do_select(
            'SELECT * FROM record_items WHERE uuid = ?', (uuid,))

        # If no records found, inform the user
        if len(record_items) == 0:
            print('No records found for the logged-in user.')
            return

        else:
            # Prepare the records
            prepared_records = self.prepare_records_as_txt(record_items)

            # Generate the file name and file path
            file_name = f"user_{user_id}_health_records.txt"
            file_path = self.get_download_path(file_name)

            # Write the prepared records to the file
            with open(file_path, 'w') as file:
                file.write(prepared_records)

            print("Health records downloaded successfully.")

    def prepare_records_as_txt(self, record_items):
        """Prepare health records in txt format"""
        text_records = "Health Records:\n\n"
        text_records += "Record Items:\n"
        for record_item in record_items:
            text_records += f"Created at: {record_item['created_at']}\n"
            text_records += f"Complaints: {record_item['complains']}\n"
            text_records += f"Height: {record_item['height']}\n"
            text_records += f"Weight: {record_item['weight']}\n"
            text_records += f"Blood Pressure: {record_item['blood_pressure']}\n"
            text_records += "\n"
            text_records += "\n"
        return text_records

    def get_download_path(self, file_name):
        """Returns the path to the Downloads folder"""
        download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
        file_path = os.path.join(download_dir, file_name)
        return file_path

    def connect_db_manager(self, db_manager):
        """Connects the db manager"""
        self.__db_manager = db_manager

    def connect_logger(self, logger):
        """Connects the logger"""
        self.__logger = logger

    def connect_login_service(self, login_service):
        """Connects the login service"""
        self.__login_service = login_service

    def connect_encryption_service(self, encryption_service):
        """Connects the encryption service"""
        self.__encryption_service = encryption_service

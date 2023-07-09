"""
    This file contains the DownloadService class, which is responsible for downloading health records
    for the logged-in user in the requested format.
"""

# Imports
from fpdf import FPDF
import os
import pyAesCrypt
from classes.dbmanager import DBManager

# DownloadService Class
class DownloadService:
    
    def download(self, user_id, format, password):
        """Downloads health records for logged-in user in requested format"""
        # Create an instance of the DatabaseManager
        dbman = DBManager()
        records = dbman.do_select('SELECT * FROM records WHERE user_id = ?', (user_id,))

        # If no records found, inform user
        if len(records) == 0:
            print('No records found for this user.')

            # Create Logger to log unsuccessful download of health records
        else:
            # If records are found, prepare in the specified format
            if format == 'pdf':
                prepared_records = self.prepare_records_as_pdf(records)
                file_extension = 'pdf'
            elif format == 'txt':
                prepared_records = self.prepare_records_as_txt(records)
                file_extension = 'txt'
            else:
                raise ValueError("Invalid format specified. Please choose either 'txt' or 'pdf'.")
            
            # Generate file name and file path
            file_name = f"user_{user_id}_health_records.{file_extension}"
            file_path = self.get_download_path(file_name)

            # Write the prepared records to file
            with open(file_path, 'w') as file:
                file.write(prepared_records)
            
            # Encrypt the file with the user's password
            self.encrypt_file(file_path, password)

            # Set appropriate headers and content type for downloading
            headers = {
                "Content-Disposition": f"attachment; filename={file_name}",
                "Content-Type": "application/octet-stream",
            }

            # Return the file path and headers
            return {
                "file": file_path + '.aes',
                "headers": headers
            }
        
        # Create Logger and log successful download of health records
    
    def prepare_records_as_txt(self, records):
        """Prepares records in txt format"""
        # Connect to the database
        dbman = DBManager()
        # Prepare health records in text format
        # Iterate over the records and retrieve associated record items
        text_records = "Health Records:\n\n"
        for record in records:
            record_items = dbman.do_select('SELECT * FROM record_items WHERE record_id = ?', (record["id"],))
            text_records += f"Record ID: {record['id']}\n"
            text_records += f"Date: {record['created_at']}\n"
            text_records += f"Record Items:\n"
            for record_item in record_items:
                text_records += f"Complaints: {record_item['complains']}\n"
                text_records += f"Height: {record_item['height']}\n"
                text_records += f"Weight: {record_item['weight']}\n"
                text_records += f"Blood Pressure: {record_item['blood_pressure']}\n"
                text_records += "\n"
            text_records += "\n"
        return text_records
    
    def prepare_records_as_pdf(self, records):
        """Prepare health records in pdf format"""
        # Connect to the database
        dbman = DBManager()
        # Prepare health records in pdf format
        # Iterate over the records and retrieve associated record items
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "Health Records", ln=True)
        pdf.ln(10)
        for record in records:
            record_items = dbman.do_select('SELECT * FROM record_items WHERE record_id = ?', (record["id"],))
            pdf.cell(0, 10, f"Record ID: {record['id']}", ln=True)
            pdf.cell(0, 10, f"Date: {record['created_at']}", ln=True)
            pdf.cell(0, 10, "Record Items:", ln=True)
            for record_item in record_items:
                pdf.cell(0, 10, f"Complaints: {record_item['complains']}", ln=True)
                pdf.cell(0, 10, f"Height: {record_item['height']}", ln=True)
                pdf.cell(0, 10, f"Weight: {record_item['weight']}", ln=True)
                pdf.cell(0, 10, f"Blood Pressure: {record_item['blood_pressure']}", ln=True)
            pdf.ln(10)
        pdf_output_path = self.get_download_path('health_records.pdf')
        pdf.output(pdf_output_path)
        return pdf_output_path
    
    def get_download_path(self, file_name):
        """Get the download path for the specified file based on the user's operating system"""
        # Get the download path
        download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
        file_path = os.path.join(download_dir, file_name)
        return file_path
    
    def encrypt_file(self, file_path, password):
        """Encrypt the file using AES encryption"""
        encrypted_file_path = file_path + '.aes'
        bufferSize = 64 * 1024 # 64kb
        pyAesCrypt.encryptFile(file_path, encrypted_file_path, password, bufferSize)
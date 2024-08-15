import fitz  # PyMuPDF
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

class File_Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.document_dir = 'docs/'
        self.image_dir = 'docs/images/'
        os.makedirs(self.document_dir, exist_ok=True)
        os.makedirs(self.image_dir, exist_ok=True)

    def get_file_extension(self):
        return os.path.splitext(self.file_path)[1].lower()
    
    def save_pdf_snapshots(self, pdf_path):
        
        document = fitz.open(pdf_path)
        
        image_paths = []
        
        # Loop through each page
        for page_num in range(document.page_count):
            page = document.load_page(page_num)  # Load the page
            pix = page.get_pixmap()  # Render the page as a pixmap

            # Define the output file path
            output_file = os.path.join(self.image_dir, f"page_{page_num + 1}.png")

            # Save the snapshot to a file
            pix.save(output_file)
            
            # Append the file path to the list
            image_paths.append(output_file)
        
        # Close the document
        document.close()
        
        return image_paths
    
    def save_docx_snapshots(self, docx_path):

        # Convert DOCX to PDF using LibreOffice
        command = [
            'libreoffice', '--headless', '--convert-to', 'pdf',
            '--outdir', self.document_dir, docx_path
        ]
        
        try:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Error converting file: {e}")
            return None
        pdf_path = os.path.join(self.document_dir, os.path.splitext(os.path.basename(docx_path))[0] + '.pdf')
        
        return self.save_pdf_snapshots(pdf_path)
    
    def save_txt_snapshots(self, txt_path):
        font = ImageFont.load_default()
        image_paths = []
        lines_per_image = 100  # Number of lines per image
        line_height = 20  # Height of each line in pixels

        with open(txt_path, 'r') as file:
            lines = file.readlines()
            total_lines = len(lines)
            
            for start in range(0, total_lines, lines_per_image):
                end = min(start + lines_per_image, total_lines)
                lines_chunk = lines[start:end]
                
                # Calculate the image height based on the number of lines
                image_height = line_height * len(lines_chunk)
                
                # Create an image with white background
                image = Image.new('RGB', (800, image_height), color=(255, 255, 255))
                draw = ImageDraw.Draw(image)
                
                # Draw each line of text
                for i, line in enumerate(lines_chunk):
                    draw.text((10, i * line_height), line.strip(), font=font, fill=(0, 0, 0))
                
                # Define the output file path
                output_file = os.path.join(self.image_dir, f"lines_{start + 1}_to_{end}.png")
                
                # Save the image
                image.save(output_file)
                image_paths.append(output_file)
        
        return image_paths
    

    def generate_snapshots(self, prefix=None):
        file_extension = self.get_file_extension()
        image_paths = []
        if file_extension == '.pdf':
            image_paths = self.save_pdf_snapshots(self.file_path)
        elif file_extension == '.docx' or file_extension == '.doc':
            image_paths = self.save_docx_snapshots(self.file_path)
        elif file_extension == '.txt':
            image_paths = self.save_txt_snapshots(self.file_path)
        else:
            print("Unsupported file format")
            return []
        if prefix:
            return [prefix + image_path.split('/')[-1] for image_path in image_paths]
        return image_paths
    
# x = File_Processor('docs/specs.docx')
# print(x.generate_snapshots("images/"))
    
    


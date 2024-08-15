
from services.file_processor import File_Processor
from services.Openai_Service import Openai_Service
import base64
class ATS_Service():
    def __init__(self, file_path):
        
        self.file_path = file_path
        self.document_dir = 'docs/'
        self.image_dir = 'docs/images/'
        self.file_processor = File_Processor(file_path)
        self.openai_service = Openai_Service()
    def parser(self):
        image_urls = self.file_processor.generate_snapshots()
        images = []
        for image_url in image_urls:
            with open(image_url, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                images.append("data:image/png;base64," + encoded_string.decode("utf-8"))
                
        print(images[0][:100])
        return self.openai_service.get_openai_response(images)
    
    
        
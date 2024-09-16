import pytesseract
from PIL import Image
from django.shortcuts import render
from .forms import UploadFileForm

# Specify the correct path to Tesseract OCR (Windows only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text(image_path):
            
    return pytesseract.image_to_string(Image.open(image_path))

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['file']
            # Save the uploaded file to disk
            with open('uploaded_image.png', 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            # Perform text extraction
            extracted_text = extract_text('uploaded_image.png')
            return render(request, 'extraction/result.html', {'text': extracted_text})
    else:
        form = UploadFileForm()
    return render(request, 'extraction/upload.html', {'form': form})

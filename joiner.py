import PyPDF2
import io
import base64

def joiner_pdf(pdf_list):
  joined_pdf = PyPDF2.PdfMerger()
  for pdf in pdf_list:
    joined_pdf.append(pdf)
  output_file = io.BytesIO()
  joined_pdf.write(output_file)
  joined_pdf.close()

  output_file.seek(0)
  pdf_bytes = output_file.read()
  base64_encoded = base64.b64encode(pdf_bytes).decode("utf-8")
  return base64_encoded 
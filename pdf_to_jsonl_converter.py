import fitz  # PyMuPDF
import jsonlines

def pdf_to_jsonl(pdf_path, output_jsonl):
    with jsonlines.open(output_jsonl, mode='w') as writer:
        pdf_document = fitz.open(pdf_path)
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            page_text = page.get_text()
            
            # You can further process 'page_text' to extract meaningful data
            # and create a JSON object containing that data
            
            json_data = {
                "page_number": page_number + 1,
                "text": page_text.strip()  # You can modify this to include more data
            }
            
            writer.write(json_data)

        pdf_document.close()

if __name__ == "__main__":
    pdf_path = "ci_cd_tools.pdf"  # Replace with your input PDF file path
    jsonl_output_path = "output.jsonl"  # Replace with your desired output JSONL file path
    pdf_to_jsonl(pdf_path, jsonl_output_path)
    print("PDF to JSONL conversion completed.")

import pymupdf
import sys

def main(input_pdf_name: str):
    doc = pymupdf.open(f"../input/{input_pdf_name}.pdf")
    
    # Detecting every rectangle in each page and disappear
    for page_num in range(len(doc)):
        page = doc[page_num]
        paths = page.get_drawings()
        rect = paths[0]["rect"]
        page.add_redact_annot(rect)
        page.apply_redactions(0,2,1)

    # creating answer pdf
    output_pdf_path = f"../output/{input_pdf_name}_answer.pdf"
    doc.save(output_pdf_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python revealer.py <input_pdf_name>")
    else:
        main(sys.argv[1])

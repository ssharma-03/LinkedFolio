import fitz  # PyMuPDF
from typing import Dict, Any, BinaryIO
import logging

class PDFParser:
    def __init__(self):
        pass

    def parse_pdf(self, pdf_file: BinaryIO) -> Dict[str, Any]:
        """
        Parse PDF resume and extract structured data
        Args:
            pdf_file: PDF file object
        Returns:
            Dictionary containing structured resume data
        """
        try:
            doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
            text_content = ""
            
            # Extract text from all pages
            for page in doc:
                text_content += page.get_text()
            
            # Basic structure for parsed data
            parsed_data = {
                "raw_text": text_content,
                "sections": self._extract_sections(text_content),
            }
            
            doc.close()
            return parsed_data
            
        except Exception as e:
            logging.error(f"Error parsing PDF: {str(e)}")
            raise e

    def _extract_sections(self, text: str) -> Dict[str, str]:
        """
        Extract different sections from the resume text
        Args:
            text: Raw text content from PDF
        Returns:
            Dictionary with section names and their content
        """
        # This is a basic implementation - can be enhanced with ML/AI
        sections = {
            "contact": "",
            "summary": "",
            "experience": "",
            "education": "",
            "skills": "",
        }
        
        # Simple section detection based on common headers
        lines = text.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            lower_line = line.lower()
            
            # Detect sections based on common headers
            if any(keyword in lower_line for keyword in ["contact", "email", "phone"]):
                current_section = "contact"
            elif any(keyword in lower_line for keyword in ["summary", "objective", "profile"]):
                current_section = "summary"
            elif any(keyword in lower_line for keyword in ["experience", "work", "employment"]):
                current_section = "experience"
            elif any(keyword in lower_line for keyword in ["education", "academic", "qualification"]):
                current_section = "education"
            elif any(keyword in lower_line for keyword in ["skills", "technologies", "competencies"]):
                current_section = "skills"
            
            # Add content to current section
            if current_section and line:
                sections[current_section] += line + "\n"
        
        return sections 
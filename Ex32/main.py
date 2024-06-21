from abc import ABC, abstractmethod

# Абстрактний клас Document
class Document(ABC):
    @abstractmethod
    def print(self):
        pass

    def prepare_for_printing(self):
        # Деякі підготовчі дії, якщо необхідно
        self.print()

# Клас PDFDocument
class PDFDocument(Document):
    def print(self):
        print("Printing PDF document")

# Клас WordDocument
class WordDocument(Document):
    def print(self):
        print("Printing Word document")

# Клас ExcelDocument
class ExcelDocument(Document):
    def print(self):
        print("Printing Excel document")

# Фабричний клас DocumentFactory
class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "PDF":
            return PDFDocument()
        elif doc_type == "Word":
            return WordDocument()
        elif doc_type == "Excel":
            return ExcelDocument()
        else:
            raise ValueError(f"Unknown document type: {doc_type}")

# Тестування функціональності
if __name__ == "__main__":
    # Створення документів за допомогою фабричного методу
    pdf_doc = DocumentFactory.create_document("PDF")
    word_doc = DocumentFactory.create_document("Word")
    excel_doc = DocumentFactory.create_document("Excel")

    # Підготовка документів до друку та друк
    pdf_doc.prepare_for_printing()
    word_doc.prepare_for_printing()
    excel_doc.prepare_for_printing()
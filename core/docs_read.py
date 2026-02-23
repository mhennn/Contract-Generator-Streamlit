from docxtpl import DocxTemplate as dx

class DocsRead:
    def __init__(self, template_name, file_name):
        self.document = dx(f"contract_templates\{template_name}.docx")
        self.file = file_name
    
    def docs_context(self, *args):
        self.context = {
            "effective_date": args[0],
            "party_a_full_name": args[1],
            "party_b_full_name": args[2],
            "party_a_address": args[3],
            "party_b_address": args[4],
            "party_a_city_state_zip": args[5],
            "party_b_city_state_zip": args[6],
        }
        self.document.render(self.context)
        return self.saving_document(self.file)

    def saving_document(self, file_name):
        self.document.save(f"{file_name}.docx")
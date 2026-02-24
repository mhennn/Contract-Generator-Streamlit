from docxtpl import DocxTemplate as dx
import io

class DocsRead:
    def __init__(self, template_name):
        self.document = dx(f"contract_templates/{template_name}.docx")
    
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

    def saving_document(self):
        bio = io.BytesIO()
        self.document.save(bio)
        bio.seek(0)
        return bio
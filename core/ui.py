import streamlit as st
from core.docs_read import DocsRead
import time

class UiApp:
    def __init__(self):
        st.set_page_config(
            page_title="Contract Generator",
            page_icon="✒️"
        )

        st.markdown(
            "<h1> Contract Generator 📑 </h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h5>Create on-the-go contract template with your own choices of template ✒️💻</h5>",
            unsafe_allow_html=True
        )
        self.display_preview()
        self.template_choices()

        self.user_template = ""
        self.effectivity_date = ""
        self.party_a_name = ""
        self.party_b_name = ""
        self.party_a_address = ""
        self.party_b_address = ""
        self.party_a_zip = ""
        self.party_b_zip = ""
        self.file_name = ""

        st.markdown(
            """
            <style>
            .stProgress > div > div > div > div {
                background-color: #FF4B4B;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    def display_preview(self):
        container = st.container(border=True)
        with container:
            st.markdown("<h6>Contract Preview</h6", unsafe_allow_html=True)
            image_path = [
                "contract_templates/Contractor_Agreement_Preview.png",
                "contract_templates/NDA_Preview.png",
                "contract_templates/Partnership_Agreement_Preview.png",
                "contract_templates/Sales_Agreement_Preview.png",
                "contract_templates/Service_Agreement_Preview.png"
            ]
            image_caption = [
                "Contracter Preview",
                "NDA Preview",
                "Partnership Preview",
                "Sales Agreement Preview",
                "Service Agreement"
            ]
            cols = st.columns(5)

            for i in range(len(image_path)):
                with cols[i]:
                    st.image(
                        image_path[i], 
                        caption=image_caption[i]
                    )

    def template_choices(self):
        container = st.container(border=True)
        template_options = [
            "Independent_Contractor_Agreement",
            "Non-Disclosure_Agreement",
            "Partnership_Agreement",
            "Sales_Purchase_Agreement",
            "Service_Agreement"
        ]

        if "fields" not in st.session_state:
            st.session_state.fields = False

        with container:
            if st.button("Complete Fields"):
                st.session_state.fields = True

            self.user_template = st.selectbox("Choose Template", options=template_options, key="user_docx")
            if st.session_state.fields:
                is_missing_data = self.input_fields()
                if st.button("Generate Template"):
                    if is_missing_data:
                        self.generate_template()
                    else:
                        st.error("Incomplete Data. Check Input Fields")
        
    def input_fields(self):
        input_columns = st.columns(2)
        with input_columns[0]:
            self.effectivity_date = st.text_input("Effectivity Date", key="eff_date")
        with input_columns[1]:
            self.file_name = st.text_input("File Name", key="file_location")
        with input_columns[0]:
            self.party_a_name = st.text_input("Party A Full Name", key="p_a_name")
        with input_columns[1]:
            self.party_b_name = st.text_input("Party B Full Name", key="p_b_name")
        with input_columns[0]:
            self.party_a_address = st.text_input("Party A Address", key="p_a_addr")
        with input_columns[1]:
            self.party_b_address = st.text_input("Party B Address", key="p_b_addr")
        with input_columns[0]:
            self.party_a_zip = st.text_input("Party A Zip Code", key="p_a_zip")
        with input_columns[1]:
            self.party_b_zip = st.text_input("Party B Zip Code", key="p_b_zip")

        field_list = [
            self.effectivity_date, self.file_name, self.party_a_name, self.party_b_name,
            self.party_a_address, self.party_b_address, self.party_a_zip, self.party_b_zip
        ]

        return all(field_list)

    def generate_template(self):
        progress_text = "Generating Template..."
        template_bar = st.progress(0, text=progress_text)

        for progs in range(100):
            time.sleep(0.2)
            template_bar.progress(progs + 1, text=progress_text)
        time.sleep(1)
        st.success("Template is ready ✒️")
        
        docsRead = DocsRead(self.user_template)
        docsRead.docs_context(self.effectivity_date, self.party_a_name, self.party_b_name, self.party_a_address, self.party_b_address, self.party_a_zip,
                              self.party_b_zip)
        
        st.download_button(
            label="Download Template",
            data=docsRead.saving_document(),
            file_name=f"{self.file_name}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
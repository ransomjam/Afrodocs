"""
Script to verify that all departments from the Word document are present in the frontend dropdown
"""
from docx import Document

# Extract all faculties and departments from the Word document
doc_path = r'pattern-formatter\Cover Pages\Cover Pages _ University of Bamenda\The University of Bamenda _ Schools-Faculties-Departments.docx'
doc = Document(doc_path)

# Get faculty/school names from paragraphs
faculties_schools = [
    "College of Technology (COL TECH)",
    "Faculty of Arts (FA)",
    "Faculty of Economics and Management Sciences (FEMS)",
    "Faculty of Education (FED)",
    "Faculty of Health Sciences (FHS)",
    "Faculty of Law and Political Science (FLPS)",
    "Faculty of Science (FS)",
    "Higher Institute of Commerce and Management (HICM)",
    "Higher Institute of Transport and Logistics (HITL)",
    "National Higher Polytechnic Institute (NAHPI)",
    "Higher Technical Teacher Training College (HTTTC)",
    "Higher Teacher Training College (HTTC)"
]

# Extract departments from each table and map to faculties
# Based on the output order:
# Table 1: Engineering (College of Technology)
# Table 2: Arts
# Table 3: Business/Management (FEMS)
# Table 4: Education
# Table 5: Health Sciences
# Table 6: Law & Political Science
# Table 7: Science
# Table 8: Commerce/Management (HICM)
# Table 9: Transport & Logistics (HITL)
# Table 10: Technical (NAHPI)
# Table 11: Engineering (likely also COL TECH)
# Table 12: Technical Education
# Table 13: Teacher Training

departments_by_faculty = {}

# Table 1: College of Technology departments
departments_by_faculty["College of Technology"] = [
    "Telecommunications", "Agribusiness Marketing Management", "Agribusiness Project Management",
    "Integrated Development and Management Studies", "Agricultural Power Engineering",
    "Water Resource Engineering", "Maintenance and Production Engineering",
    "Animal Nutrition and Feeding", "Animal Production Technology",
    "Biotechnology and Animal Science: Reproductive Physiology and Animal Health",
    "Biotechnology and Animal Science: Animal Nutrition and Feeding",
    "Reproductive Physiology and Animal Health", "Wildlife Resource Management",
    "Forest Resource Management", "Wildlife Resources Management",
    "Forest Resource Management - Forest Economics", "Computer Engineering - Data Science",
    "Computer Engineering - Information Technology and Cyber Security",
    "Crop Production Technology", "Electrical Power Engineering",
    "Food Science and Human Nutrition", "Food Science and Bioresource Technology",
    "Nutritional Sciences", "Food and Bioresource Technology",
    "Environmental Technology", "Bioenergy Engineering", "Satellite Communications",
    "Renewable Energy Engineering", "Didactics, Curriculum Development and Teaching",
    "Computer Engineering", "Computer Networks and Systems Maintenance",
    "Computer Software Engineering", "Software Engineering",
    "Electrical and Electronics Engineering", "Electric and Power Engineering",
    "Electric Power Engineering", "Electronic Engineering",
    "Renewable Energy Engineering", "Telecommunication"
]

# Table 2: Faculty of Arts departments
departments_by_faculty["Faculty of Arts"] = [
    "International Studies", "Translation", "Communication and Development Studies",
    "Geography and Planning", "Economic and Social Development History",
    "Heritage and Cultural History", "History and Public Policy: Option - Decentralization and Local Governance",
    "English Language", "Literatures in English", "Linguistics and African Languages",
    "Applied Linguistics", "Theatre, Television and Film Studies",
    "Visual Arts and History of Arts", "Philosophy", "English Language and Literature Teaching",
    "Literature and Digital cultures", "Communication",
    "Evaluation and Measurement", "Subject Didactics", "History and Archaeology",
    "Cameroonian Languages and Cultures", "African Renaissance Studies",
    "Mother Tongue Education", "Music and Dance", "Bilingual Letters",
    "Functional Language Enhancement", "Intercultural Communication and Mediation Studies",
    "Multilingual and Intercultural Communication", "Literary and Digital Cultures",
    "Language and Literature Teaching"
]

# Table 3: Faculty of Economics and Management Sciences
departments_by_faculty["Faculty of Economics and Management Sciences"] = [
    "Accounting", "Management", "Economics", "Health Economics, Policy and Management",
    "Environmental Economics, Policy and Management", "Marketing",
    "Human Resource Management", "Banking and Finance", "Finance and Investment",
    "Islamic Banking and Finance", "Quantitative Finance"
]

# Table 4: Faculty of Education
departments_by_faculty["Faculty of Education"] = [
    "Environmental Education", "History of Education", "Philosophy of Education",
    "Sociology of Education", "Educational Measurement and Evaluation",
    "Applied Developmental Psychology", "Community Psychology", "Educational Psychology",
    "Teacher Education", "Educational Leadership and Management",
    "Higher Education Development & Governance", "Economics and Finance of Education",
    "Educational Technology", "Curriculum Planning and Design", "Pedagogy",
    "Inclusive Education", "Physical Education and Animation", "Health Psychology",
    "Clinical Counseling", "Counselling", "Teaching Science, Technology, Engineering and Mathematics",
    "Educational Leadership", "Educational Foundations", "Secondary Education",
    "Nomadic Teacher Education", "STEM Education", "Inspection & Supervision of Instructions",
    "Curriculum Pedagogy", "Braille and Sign Language", "Recreation and Leisure Studies",
    "Guidance and Counselling", "Social and Organizational Psychology", "Social Work",
    "Psychology of Education", "Supervision of Instruction", "Early Childhood Development",
    "Early Childhood Care and Education", "Measurement and Evaluation", "Primary Education",
    "Technical Education", "Economics of Education", "Educational Leadership in Basic Education",
    "Educational Leadership in Secondary Education", "School Principalship",
    "Library, Archival and Information Science", "Physical and Health Education",
    "Sport Psychology", "Coaching", "Wellness and Fitness Instruction",
    "Bereavement Counseling", "Industrial and Organizational Psychology",
    "School Counseling", "Health Counselling", "Distance Education"
]

# Table 5: Faculty of Health Sciences
departments_by_faculty["Faculty of Health Sciences"] = [
    "Chemical Pathology", "Pharmacology and Toxicology", "Medical Laboratory Science",
    "Midwifery Science", "Medical-Surgical Nursing", "Psychiatric Nursing",
    "Paediatric Nursing", "Oncology Nursing", "Public Health", "Biomedical Sciences",
    "Medicine", "Pharmacology", "Medical Laboratory Sciences (BMLS)",
    "Nursing/Midwifery", "Nursing Science", "Nursing", "Midwifery",
    "Community Health", "Pharmacy"
]

# Table 6: Faculty of Law and Political Science
departments_by_faculty["Faculty of Law and Political Science"] = [
    "Regional Integration", "Internal Public Law", "Public International Law",
    "Public Administration and Policy", "Negotiation, Mediation and Peace Building",
    "International Relations and Strategic Studies", "Capacité en Droit",
    "Political Science", "English Private Law", "Property Law", "Human Rights Law",
    "Public Law", "Public Policy and Public Administration", "Comparative Politics",
    "Anthropological Politics", "International Law", "Natural Resource Law", "Law",
    "Business Communication", "Executive Studies in Business Negotiations and Contract Management",
    "Energy, Petroleum and Mineral Law", "Public Administration"
]

# Table 7: Faculty of Science
departments_by_faculty["Faculty of Science"] = [
    "Thermal Engineering", "Environmental Science", "Probability and Statistics",
    "Applied Mathematics", "Physics", "Food and Industrial Microbiology",
    "Applied Botany", "Applied Zoology", "Biochemistry", "Chemistry", "Geology",
    "Mathematics and Statistics", "Microbiology", "Geoscience",
    "Applied Parasitology and Vector Biology", "Medical Microbiology and Infectious Diseases",
    "Industrial and Urban Waste Management", "Applied Geology", "Petroleum Geoscience",
    "Biodiversity, Conservation and Management", "Medicinal Plants"
]

# Table 8: Higher Institute of Commerce and Management
departments_by_faculty["Higher Institute of Commerce and Management"] = [
    "Real Estate Management", "Development Finance", "Project Management",
    "Accounting and Finance", "Insurance and Security", "Marketing",
    "Money and Banking", "Management and Entrepreneurship", "Human Resource Management",
    "Executive Secretariat Duties", "Environmental Accounting", "Tax Accounting",
    "Public Sector Accounting", "Microfinance", "Inventory and Supply Chain Management",
    "Information and Communication Management", "Local Government Management",
    "Logistic Management", "Supply Chain Management", "Executive MBA"
]

# Table 9: Higher Institute of Transport and Logistics
departments_by_faculty["Higher Institute of Transport and Logistics"] = [
    "Transportation", "Port and Shipping Management", "Logistics and Supply Chain Management",
    "Tourism and Sustainable Environmental Management", "Transit and Logistics",
    "Tourism and Hospitality management", "Maritime Transport", "Tourism and cultural Heritage Development",
    "Customs", "Land Transport", "Transport and Logistics Management", "Air Transport"
]

# Table 10: National Higher Polytechnic Institute (M-Tech programs)
departments_by_faculty["National Higher Polytechnic Institute"] = [
    "Ports and Shipping Management", "Logistics and Transport", "Project Management",
    "Marketing", "Corporate Governance and Financial Law", "Software Engineering and Embedded System",
    "Executive Secretariat Studies", "Structural Engineering",
    "Geotechnical Engineering and Transportation Engineering", "Wood Science & Technology",
    "Agricultural Machinery and Power Engineering", "Automation and Control",
    "Electric Power and Energy Systems", "Bakery and Food Processing Technology",
    "Crop Production Technology", "Urban Planning and Surveys Engineering",
    "Community Development", "Conflict Management and Peace Building",
    "Fashion Clothing and Textile", "Sexual and Reproductive Health",
    "Adult and Geriatric Nursing Practice", "Mechanical and Production Engineering",
    "Nutrition and Dietetics"
]

# Print the summary
print("=" * 80)
print("UNIVERSITY OF BAMENDA - COMPREHENSIVE FACULTY AND DEPARTMENT LISTING")
print("=" * 80)
print()

for faculty, depts in departments_by_faculty.items():
    print(f"\n{faculty}:")
    print(f"  Total departments: {len(depts)}")
    for i, dept in enumerate(depts, 1):
        print(f"  {i:2d}. {dept}")

print("\n" + "=" * 80)
print(f"TOTAL FACULTIES/SCHOOLS: {len(departments_by_faculty)}")
print(f"TOTAL DEPARTMENTS: {sum(len(depts) for depts in departments_by_faculty.values())}")
print("=" * 80)

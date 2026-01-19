"""
Comprehensive verification report comparing frontend dropdown with Word document
"""

# Frontend data (from index.html)
frontend_data = {
    "College of Technology": [
        "Agribusiness Technology",
        "Agricultural and Environmental Engineering",
        "Animal Production Technology",
        "Crop Production Technology",
        "Electric Power Engineering",
        "Electronics",
        "Food Science and Technology"
    ],
    "Faculty of Arts": [
        "Communication and Development Studies",
        "English",
        "Geography and Planning",
        "History and Archaeology",
        "Linguistics",
        "Performing and Visual Arts"
    ],
    "Faculty of Education": [
        "Counseling Psychology",
        "Educational Foundations",
        "Educational Leadership",
        "Physical Education"
    ],
    "Faculty of Science": [
        "Biochemistry",
        "Botany",
        "Chemistry",
        "Computer Science",
        "Geology",
        "Mathematics",
        "Physics",
        "Zoology"
    ],
    "Higher Institute of Commerce and Management": [
        "Accounting",
        "Insurance and Security",
        "Management",
        "Marketing"
    ],
    "National Higher Polytechnic Institute": [
        "Civil Engineering",
        "Computer Engineering",
        "Electrical and Electronic Engineering",
        "Mechanical Engineering",
        "Mining and Mineral Engineering",
        "Petroleum Engineering"
    ]
}

# Word document data (complete from verification script)
document_data = {
    "College of Technology": [
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
    ],
    "Faculty of Arts": [
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
    ],
    "Faculty of Economics and Management Sciences": [
        "Accounting", "Management", "Economics", "Health Economics, Policy and Management",
        "Environmental Economics, Policy and Management", "Marketing",
        "Human Resource Management", "Banking and Finance", "Finance and Investment",
        "Islamic Banking and Finance", "Quantitative Finance"
    ],
    "Faculty of Education": [
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
    ],
    "Faculty of Health Sciences": [
        "Chemical Pathology", "Pharmacology and Toxicology", "Medical Laboratory Science",
        "Midwifery Science", "Medical-Surgical Nursing", "Psychiatric Nursing",
        "Paediatric Nursing", "Oncology Nursing", "Public Health", "Biomedical Sciences",
        "Medicine", "Pharmacology", "Medical Laboratory Sciences (BMLS)",
        "Nursing/Midwifery", "Nursing Science", "Nursing", "Midwifery",
        "Community Health", "Pharmacy"
    ],
    "Faculty of Law and Political Science": [
        "Regional Integration", "Internal Public Law", "Public International Law",
        "Public Administration and Policy", "Negotiation, Mediation and Peace Building",
        "International Relations and Strategic Studies", "Capacité en Droit",
        "Political Science", "English Private Law", "Property Law", "Human Rights Law",
        "Public Law", "Public Policy and Public Administration", "Comparative Politics",
        "Anthropological Politics", "International Law", "Natural Resource Law", "Law",
        "Business Communication", "Executive Studies in Business Negotiations and Contract Management",
        "Energy, Petroleum and Mineral Law", "Public Administration"
    ],
    "Faculty of Science": [
        "Thermal Engineering", "Environmental Science", "Probability and Statistics",
        "Applied Mathematics", "Physics", "Food and Industrial Microbiology",
        "Applied Botany", "Applied Zoology", "Biochemistry", "Chemistry", "Geology",
        "Mathematics and Statistics", "Microbiology", "Geoscience",
        "Applied Parasitology and Vector Biology", "Medical Microbiology and Infectious Diseases",
        "Industrial and Urban Waste Management", "Applied Geology", "Petroleum Geoscience",
        "Biodiversity, Conservation and Management", "Medicinal Plants"
    ],
    "Higher Institute of Commerce and Management": [
        "Real Estate Management", "Development Finance", "Project Management",
        "Accounting and Finance", "Insurance and Security", "Marketing",
        "Money and Banking", "Management and Entrepreneurship", "Human Resource Management",
        "Executive Secretariat Duties", "Environmental Accounting", "Tax Accounting",
        "Public Sector Accounting", "Microfinance", "Inventory and Supply Chain Management",
        "Information and Communication Management", "Local Government Management",
        "Logistic Management", "Supply Chain Management", "Executive MBA"
    ],
    "Higher Institute of Transport and Logistics": [
        "Transportation", "Port and Shipping Management", "Logistics and Supply Chain Management",
        "Tourism and Sustainable Environmental Management", "Transit and Logistics",
        "Tourism and Hospitality management", "Maritime Transport", "Tourism and cultural Heritage Development",
        "Customs", "Land Transport", "Transport and Logistics Management", "Air Transport"
    ],
    "National Higher Polytechnic Institute": [
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
}

print("="*100)
print("VERIFICATION REPORT: FRONTEND DROPDOWN vs. WORD DOCUMENT DEPARTMENTS")
print("="*100)
print()

# Missing faculties in frontend
missing_faculties = set(document_data.keys()) - set(frontend_data.keys())
if missing_faculties:
    print("❌ MISSING FACULTIES/SCHOOLS IN FRONTEND:")
    print("-" * 100)
    for faculty in sorted(missing_faculties):
        dept_count = len(document_data[faculty])
        print(f"  • {faculty}")
        print(f"    Total departments in document: {dept_count}")
    print()

# Check each faculty
print("\n✓ COMPARISON BY FACULTY/SCHOOL:")
print("-" * 100)

total_missing_depts = 0
total_mismatches = 0

for faculty in sorted(frontend_data.keys()):
    frontend_depts = set(frontend_data[faculty])
    doc_depts = set(document_data.get(faculty, []))
    
    missing = doc_depts - frontend_depts
    extra = frontend_depts - doc_depts
    match_count = len(frontend_depts & doc_depts)
    
    print(f"\n{faculty}:")
    print(f"  Frontend: {len(frontend_depts)} departments")
    print(f"  Document: {len(doc_depts)} departments")
    print(f"  Match: {match_count}/{len(doc_depts)}")
    
    if missing:
        print(f"  ❌ Missing {len(missing)} departments from document:")
        total_missing_depts += len(missing)
        for dept in sorted(missing):
            print(f"     - {dept}")
    
    if extra:
        print(f"  ⚠️  {len(extra)} departments in frontend but NOT in document:")
        total_mismatches += len(extra)
        for dept in sorted(extra):
            print(f"     - {dept}")
    
    if not missing and not extra:
        print(f"  ✅ All departments match!")

print("\n" + "="*100)
print("SUMMARY:")
print("="*100)
print(f"Total Faculties in Document: {len(document_data)}")
print(f"Total Faculties in Frontend: {len(frontend_data)}")
print(f"Missing Faculties: {len(missing_faculties)}")
if missing_faculties:
    for f in sorted(missing_faculties):
        print(f"  - {f} ({len(document_data[f])} departments)")
print()
print(f"Total Missing Departments: {total_missing_depts}")
print(f"Total Extra/Mismatched Departments: {total_mismatches}")
print()

# Overall accuracy
total_doc_depts = sum(len(depts) for depts in document_data.values())
total_frontend_depts = sum(len(depts) for depts in frontend_data.values())
coverage = (total_frontend_depts - total_mismatches) / total_doc_depts * 100 if total_doc_depts > 0 else 0

print(f"Document Total: {total_doc_depts} departments across {len(document_data)} faculties")
print(f"Frontend Total: {total_frontend_depts} departments across {len(frontend_data)} faculties")
print(f"Coverage: {coverage:.1f}%")
print("="*100)

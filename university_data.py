"""
Parse university faculty data and create structured mappings.
This file contains the extracted institution, faculty, and department data.
"""

# ===== UNIVERSITY OF BAMENDA DATA =====
BAMENDA_DATA = {
    "College of Technology": {
        "Telecommunications": "B.Tech, MSc, MProf",
        "Agribusiness Marketing": "UDT (HND/HPD), M.Tech",
        "Computer Engineering": "B.Tech, BSc, M.Tech",
        "Food Science and Technology": "B.Tech, M.Tech",
        "Forestry and Agroforestry": "B.Tech, M.Tech",
        "Renewable Energy": "B.Tech, M.Tech, PhD"
    },
    "Faculty of Arts": {
        "English Language": "BA, MA, PhD",
        "Philosophy": "BA, MA, PhD",
        "French": "BA, MA, PhD",
        "History": "BA, MA, PhD"
    },
    "Faculty of Economics and Management Sciences": {
        "Accounting": "BSc, MSc, PhD, B.Tech",
        "Management": "BSc, MSc, PhD",
        "Business Administration": "BSc, MSc, MBA",
        "Tourism and Hotel Management": "BSc, MSc"
    },
    "Faculty of Education": {
        "General Pedagogy": "DES I, DES II, DIPES I, DIPES II",
        "Educational Psychology": "B.Ed, M.Ed, PhD",
        "Special Education": "B.Ed, M.Ed"
    },
    "Faculty of Health Sciences": {
        "Nursing": "Bachelor, Masters, PhD",
        "Public Health": "Bachelor, Masters, PhD",
        "Medical Laboratory Science": "Bachelor, Masters"
    },
    "Faculty of Law and Political Science": {
        "Law": "LL.B, LL.M, PhD",
        "Political Science": "BSc, MSc, PhD"
    },
    "Faculty of Science": {
        "Mathematics": "BSc, MSc, PhD",
        "Physics": "BSc, MSc, PhD",
        "Chemistry": "BSc, MSc, PhD",
        "Biology": "BSc, MSc, PhD"
    },
    "Higher Institute of Commerce and Management": {
        "Hospitality Management": "B.Tech, M.Tech",
        "Business Management": "B.Tech, M.Tech",
        "Commerce": "B.Tech, M.Tech"
    },
    "Higher Institute of Transport and Logistics": {
        "Transport Management": "B.Tech, M.Tech",
        "Logistics": "B.Tech, M.Tech"
    },
    "National Higher Polytechnic Institute": {
        "Engineering": "HND, B.Tech",
        "Technology": "HND, B.Tech"
    },
    "Higher Teacher Training College": {
        "English": "DIPES I, DIPES II",
        "Mathematics": "DIPES I, DIPES II",
        "Biology": "DIPES I, DIPES II",
        "Physics": "DIPES I, DIPES II"
    },
    "Higher Technical Teacher Training College": {
        "Administrative Techniques": "Diploma in Technical Education I & II",
        "Civil Engineering and Forestry Techniques": "Diploma in Technical Education I & II",
        "Computer Science": "Diploma in Technical Education I & II",
        "Economic Science": "Diploma in Technical Education I & II",
        "Electrical and Power Engineering": "Diploma in Technical Education I & II"
    }
}

# ===== UNIVERSITY OF BUEA DATA =====
BUEA_DATA = {
    "College of Technology (COT)": {
        "Computer Engineering": "B.Tech, M.Tech, Top up",
        "Hardware Maintenance": "B.Tech",
        "Information and Communication Technology": "B.Tech",
        "Software Engineering": "M.Tech, Top up",
        "Software Engineering and Computing": "B.Tech",
        "Air Conditioning and Refrigeration": "B.Tech",
        "Electrical and Electronic Engineering": "B.Tech, M.Tech, Top up",
        "Electric Power System": "B.Tech, M.Tech",
        "Telecommunication and Networks": "M.Tech, Top up",
        "Telecommunication": "B.Tech",
        "Mechanical Engineering": "B.Tech, M.Tech",
        "Industrial Maintenance and Manufacturing": "M.Tech, Top-Up M.Sc",
        "Mechanical Fabrication": "B.Tech",
        "Materials Characterisation, Maintenance and Management": "Professional Master",
        "Structural & Metallic Construction": "B.Tech",
        "Thermo-Fluids Engineering": "B.Tech",
        "Welding Technology": "B.Tech",
        "Renewable Energy": "B.Tech"
    },
    "Advanced School of Translators and Interpreters (ASTI)": {
        "Conference Interpretation": "Certificate",
        "Translation": "Certificate, M.A., PhD, Professional B.A.",
        "Interpretation": "M.A., Postgraduate Diploma",
        "Conference Interpretation (Pan African)": "M.A.",
        "Translation and Intercultural Studies": "PhD, Professional B.A."
    },
    "Faculty of Agriculture and Veterinary Medicine (FAVM)": {
        "Agricultural Economics and Agribusiness": "BSc, PhD, Professional M.Sc",
        "Agricultural Extension and Rural Development": "B.Sc, M.Sc",
        "Agronomic and Applied Molecular Science": "BSc, M.Sc, PhD, Professional M.Sc",
        "Animal Science": "B.Sc, M.Sc, PhD",
        "Food Science and Technology": "B.Sc, M.Sc",
        "Forestry and Wildlife": "B.Sc, M.Sc",
        "Veterinary Medicine": "Doctor of Veterinary Medicine",
        "Fisheries and Aquatic Resources Management": "B.Sc, M.Sc, PhD"
    },
    "Faculty of Arts (FA)": {
        "Bilingual and Communication Studies (French)": "B.A., M.A., PhD, Professional Masters",
        "Bilingual and Communication Studies (Bilingual Letters)": "B.A., M.A.",
        "Bilingual and Communication Studies (Francophone Literatures)": "B.A., M.A., PhD",
        "Bilingual and Communication Studies (Sciences du Langage)": "M.A.",
        "Bilingual and Communication Studies (Teaching French)": "M.A.",
        "Philosophy": "B.A.",
        "English (Language)": "B.A., M.A., PhD",
        "English (Literature)": "B.A., M.A., PhD",
        "History": "B.A., M.A., PhD, Professional Masters",
        "Theoretical Linguistics": "B.A., M.A., PhD",
        "Applied Linguistics": "M.A., PhD",
        "Communication for Sustainable Development": "M.A.",
        "Second Foreign Language Teaching": "M.A.",
        "Performing and Visual Arts": "B.A., M.A., Professional B.A."
    },
    "Faculty of Education (FED)": {
        "Curriculum Studies and Teaching": "B.Ed, M.Ed, PhD, Professional Masters, Professional Higher Education Certificate, Top up M.Ed",
        "Educational Foundations and Administration": "B.Ed, M.Ed, Masters, PhD",
        "Educational Psychology": "B.Ed, M.Sc, M.Ed, PhD",
        "Library, Archival and Information Sciences": "Bachelor, Professional M.Sc"
    },
    "Faculty of Engineering and Technology (FET)": {
        "Civil Engineering": "M.Eng",
        "Computer Engineering": "B.Eng, M.Eng, M.Sc, PhD, Top-Up",
        "Chemical and Petroleum Engineering": "B.Eng",
        "Electrical and Electronic Engineering": "B.Eng, M.Eng, M.Sc, PhD, Professional Masters, Top-Up",
        "Mechanical and Industrial Engineering": "B.Eng, M.Eng, M.Sc, Professional Master, Top-Up"
    },
    "Faculty of Health Sciences (FHS)": {
        "Biomedical Sciences": "B.Sc., Master, PhD",
        "Obstetrics and Gynaecology": "Resident",
        "Medical Laboratory Science": "Bachelor, M.Sc., PhD, Professional M.Sc.",
        "Medicine": "Doctor (DDS, MD, PharmD), Resident",
        "Nursing": "Bachelor, B.Sc., M.Sc., Masters, PhD, Professional Masters",
        "Public Health": "B.Sc., Master, PhD, Professional Masters (MPH)",
        "Surgery and Specialities (Anaesthesiology)": "M.Sc."
    },
    "Faculty of Laws and Political Science (FLPS)": {
        "Customary and Comparative Law": "Master",
        "Business Law": "LL.B, LL.M",
        "Civil Law": "LL.B, LL.M",
        "English Law": "LL.B, LL.M, PhD, Professional LL.M",
        "Political Science and Comparative Politics": "B.Sc, M.Sc, Masters, PhD",
        "Public Law and Public Administration": "B.Sc, LL.B, Masters, M.Sc, PhD, Professional Masters, Top-Up M.Sc",
        "International Relations and Conflict Resolutions": "B.Sc, M.Sc, PhD, Professional Masters, Top-Up Master"
    },
    "Faculty of Science (FS)": {
        "Animal Biology": "B.Sc, M.Sc, PhD, Professional BSc",
        "Biochemistry and Molecular Biology": "B.Sc, M.Sc, Masters, PhD, Professional BSc, Professional M.Sc, Top up M.Sc",
        "Chemistry": "B.Sc, M.Sc, PhD, Professional Masters, Top up M.Sc",
        "Computer Science": "B.Sc, M.Sc, PhD",
        "Environmental Science": "B.Sc, M.Sc, PhD, Professional Masters, Professional MSc",
        "Geology": "B.Sc, M.Sc, PhD, Professional Minor",
        "Mathematics": "B.Sc, M.Sc, PhD",
        "Microbiology and Parasitology": "B.Sc, M.Sc, PhD, Professional M.Sc, Top up M.Sc",
        "Physics": "B.Sc, M.Sc, PhD",
        "Plant Science": "B.Sc, M.Sc, PhD, Professional Masters, Professional MSc"
    },
    "Faculty of Social and Management Sciences (SMS)": {
        "Banking and Finance": "B.Sc, M.Sc, MBA, PhD",
        "Economics and Management": "B.Sc, MBA, M.Sc, PhD, Professional M.Sc, Professional MBA",
        "Geography": "B.Sc, M.Sc, PhD, Professional Masters",
        "Journalism and Mass Communication": "B.Sc, M.Sc, PhD, Professional Masters",
        "Law": "B.L, LL.B, LL.M, PhD",
        "Management": "B.Sc, M.Sc, PhD",
        "Political Science": "B.Sc, M.Sc, PhD, Professional Masters (MPA)",
        "Sociology and Anthropology": "B.Sc, M.Sc, Masters, PhD",
        "Women's and Gender Studies": "Double Major, M.Sc, PhD"
    },
    "Higher Teachers Training College (HTTC)": {
        "Languages, Arts, and Literatures (various combinations)": "DIPES I / DIPES II",
        "Philosophy and Citizenship Education (various combinations)": "DIPES I / DIPES II",
        "Bilingual Letters": "DIPES I / DIPES II",
        "Biology": "DIPES I / DIPES II",
        "Chemistry": "DIPES I / DIPES II",
        "Computer Science": "DIPES I / DIPES II",
        "Information and Communication Technology": "DIPES I / DIPES II",
        "Economics": "DIPES I / DIPES II",
        "English Modern Letters": "DIPES I / DIPES II",
        "French Modern Letters": "DIPES I / DIPES II",
        "Geography": "DIPES I / DIPES II",
        "Geology": "DIPES I / DIPES II",
        "Guidance and Counselling": "DIPES II",
        "History": "DIPES I / DIPES II",
        "Mathematics": "DIPES I / DIPES II",
        "Natural Science": "DIPES I / DIPES II",
        "Philosophy": "DIPES II",
        "Physics": "DIPES I / DIPES II",
        "Science of Education": "DIPEN II",
        "Sciences (Combined: Biology, Chemistry, Geology, Environmental)": "DIPES I / DIPES II",
        "Sciences (Combined: Mathematics, Computer Science)": "DIPES I / DIPES II",
        "Sciences (Combined: Physics, Chemistry & Technology)": "DIPES I / DIPES II",
        "Social Sciences and Humanities (Combinations)": "DIPES I / DIPES II",
        "Special Needs Education": "DIPES I / DIPES II"
    },
    "Higher Technical Teachers Training College (HTTTC)": {
        "Administrative Techniques": "B.Sc, DIPET I, DIPET II, HND, M.Tech, PhD, Professional B.Tech",
        "Agriculture": "B.Tech, DIPET II, HND, M.Tech, Professional B.Tech",
        "Civil Engineering & Forestry Techniques": "DIPET I, DIPET II, HND, M.Tech, Professional B.Tech",
        "Computer Science": "DIPET I, DIPET II, HND, M.Tech, Professional B.Tech",
        "Electrical & Power Engineering": "DIPET I, DIPET II, HND, M.Tech, Professional B.Tech",
        "Guidance Counselling": "DIPCO I, DIPCO, M.Ed, Professional B.Tech",
        "Law": "DIPET I, DIPET II, HND, M.Tech, Professional B.Tech",
        "Management Sciences": "DIPET I, DIPET II, HND, M.Tech, Professional B.Tech",
        "Mechanical Engineering": "DIPET I, DIPET II, HND, M.Tech, Professional B.Tech",
        "Renewable Energy": "DIPET I, DIPET II, HND, M.Tech, Professional B.Tech",
        "Science of Education": "DIPET I, DIPET II, HND, M.Ed, Professional B.Tech",
        "Social Economy & Family Management": "B.Sc, DIPET I, DIPET II, HND, M.Tech, PhD, Professional B.Tech",
        "Topography & Real Estate Management": "DIPET I, DIPET II, Professional B.Tech",
        "Tourism & Hospitality Management": "B.Sc, DIPET I, DIPET II, HND, M.Tech, PhD, Professional B.Tech, Professional IATA Diploma",
        "System Administration": "B.Sc, DIPET I, DIPET II, HND, M.Tech, Professional B.Tech"
    }
}

# Simplified lists for dropdowns
BAMENDA_INSTITUTIONS = list(BAMENDA_DATA.keys())
BUEA_INSTITUTIONS = list(BUEA_DATA.keys())

def get_departments(university, institution):
    """Get departments for a given institution and university."""
    if university == "Bamenda":
        return list(BAMENDA_DATA.get(institution, {}).keys())
    elif university == "Buea":
        return list(BUEA_DATA.get(institution, {}).keys())
    return []

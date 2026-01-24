"""
Test script to verify headings don't have unwanted page breaks.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from pattern_formatter_backend import DocumentProcessor, WordGenerator, FormatPolicy

TEST_DOCUMENT = """
CHAPTER ONE

INTRODUCTION

### **1.1 Background to the Study**

The evolution of digital preservation has been remarkable, transforming from a simple storage solution to a complex, technology-driven field. Early preservation efforts focused mainly on storing digital content for future access; however, recent advancements have shown a major shift toward more structured, strategic, and dynamic systems of preserving digital information. Contemporary studies highlight the increasing adoption of interactive approaches, incorporating immersive technologies such as **Virtual Reality (VR)** and **Augmented Reality (AR)** to enhance cultural heritage preservation and presentation (Lian & Xie, 2024). Through these tools, institutions can recreate historical environments, enable virtual access to cultural artefacts, and improve public engagement with preserved materials.

In addition, the emergence of **digital twins**, **3D modelling**, and **Geographic Information Systems (GIS)** has strengthened preservation efforts by enabling more accurate reconstruction and representation of historical artefacts and sites (Rizzi et al., 2022). These technologies support detailed documentation, preserve fragile heritage objects in digital form, and allow long-term monitoring and analysis. Furthermore, the rise of **digital-first publications** and **open-access journals** has changed the way academic communities approach citation practices, leading organizations such as the **Modern Language Association (MLA)** and the **American Psychological Association (APA)** to update their guidelines to accommodate digital sources and online materials (Rizzi et al., 2022). This shift highlights how digital preservation is not only relevant in heritage institutions but is also essential to academic life.

Academic records maintenance has undergone significant transformation over the years, largely driven by technological innovations and changing educational needs. Traditionally, records such as student transcripts, admission files, results sheets, and graduation registers were kept manually, resulting in limited accessibility, high storage costs, weak security, and increased risks of physical loss. The shift to electronic and online record management systems has improved the **accuracy, efficiency, confidentiality, security, and accessibility** of academic information. Recent studies emphasize that effective management of academic records depends on factors such as **data accuracy, integrity, institutional culture, staff capacity, and infrastructure** (Bing & Farhana, 2024).

Today's world is experiencing an unprecedented era of digital transformation, where academic institutions generate vast amounts of data and digital records across multiple platforms. Universities now produce records not only in physical forms but also as electronic documents including emails, databases, scanned archives, online transcripts, student portals, and learning management systems. Preserving these records is crucial for maintaining their integrity, authenticity, and long-term accessibility. Beyond institutional usefulness, academic record preservation supports legal compliance, transparency, and evidence-based decision-making in higher education.

---

### **1.1.1 Digital Preservation and the Growth of Digital Academic Records**

The growth of digital academic records is linked to modern educational systems where students and staff rely heavily on technology. Academic institutions now create records such as:

* student admission data
* course registration logs
* examination results
* transcripts and certificates
* disciplinary records
* tuition and fee payment records
* student evaluation files
* graduation and alumni records

These digital records are critical for both institutional planning and individual student progress tracking. However, without proper preservation measures, digital records can become inaccessible due to file corruption, system failure, accidental deletion, cyber-attacks, or format obsolescence.

---

### **1.1.2 Importance of Digital Preservation in Higher Education Institutions**

Digital preservation is essential in academic institutions because it ensures:

1. **Continuity of academic operations**
   (records are retrievable when needed for administrative processes)

2. **Protection of institutional credibility**
   (records prove authenticity of student credentials)

3. **Long-term access to academic history**
   (students and alumni can retrieve records years later)

4. **Compliance with policies and regulations**
   (universities are required to keep reliable documentation)

5. **Support for governance and accountability**
   (records serve as evidence in institutional audits and reviews)

---

### **1.1.3 Digital Preservation Practices in Developed Countries**

In developed countries, digital preservation strategies have become a major priority for educational institutions and national record agencies. In the United States, Jennifer and David (2020) note that standardized workflows, file integrity checks, and well-defined digital record processes help ensure long-term accessibility and usability of academic records (Trant & Bearman, 2022). The **National Archives and Records Administration (NARA)** has developed a comprehensive digital preservation strategy emphasizing preservation metadata, digital integrity validation, and long-term storage planning (Wilson, 2022).

In the United Kingdom, researchers have emphasized the need for trusted digital repositories that support secure storage, standardization, and accessibility (Helen & Andraw, 2024). The **National Archives (UK)** promotes a digital preservation strategy aligned with the **Open Archival Information System (OAIS)** reference model, focusing on long-term sustainability and trusted repository principles (Lavoie, 2022).

Australia has also advanced digital preservation through clear institutional policy frameworks. Colin and Paul (2021) highlight that national digital preservation policies provide guidance on preservation priorities, format management, data integrity, and collection sustainability (Colin & Paul, 2021). Similarly, Canada has adopted structured digital preservation frameworks, with **Library and Archives Canada (LAC)** emphasizing trusted digital repositories and digital collection management planning (Parent & Page, 2022; Wilson, 2024).

---

### **1.1.4 Digital Preservation Challenges in Developing Countries**

In developing countries, digital preservation is often a pressing challenge due to limited infrastructure, financial constraints, and inadequate technical expertise. Many institutions struggle with inconsistent electricity supply, limited ICT capacity, weak policy enforcement, and insufficient storage resources. The absence of effective strategies has resulted in loss and inaccessibility of records, affecting institutional transparency and academic credibility.

For example, in India, Kumar and Tripathi (2020) stress that digital preservation remains critical for ensuring long-term access to academic records, especially research outputs and institutional archives (Kumar & Tripathi, 2021). Government efforts like the **National Digital Preservation Program** aim to promote standardized preservation practices and national frameworks (Chakraborty, 2023).

In Indonesia, efforts have focused on institutional repositories such as the **Indonesian Digital Repository (IDR)**, which supports preservation and dissemination of academic outputs including theses and dissertations (Rahardjo & Riyanto, 2019; Wibowo & Sari, 2025). Malaysia has also made progress through national policy initiatives that emphasize metadata management, rights management, and preservation planning (Aziz & Ahmad, 2022).

Brazil has implemented strategies through digital repositories such as the **Brazilian Digital Library** and national policies supporting the long-term preservation of digital academic resources (Almeida & Leite, 2018; Silva & Souza, 2024).

---

### **1.1.5 Digital Preservation in Africa**

In Africa, digital preservation is a major concern because many academic institutions face serious constraints such as poor infrastructure, limited funding, weak technical capacity, and insufficient staff training. Unlike developed countries where digital preservation is structured and standardized, many African universities lack comprehensive frameworks guiding record preservation practices (Adeyinka & Ojo, 2021). Onyema and Oluwaseyi (2020) observed that only a small number of African universities have clear digital preservation policies, leading to frequent loss of academic records and compromised trust in academic systems (Onyema & Oluwaseyi, 2017).

South Africa has made notable progress, with scholars emphasizing the need for long-term preservation mechanisms that ensure sustainability and access (Mnisi & Onyango, 2022). Nigeria has attempted to expand digital repositories for academic record preservation, especially theses and dissertations, through institutional strategies and repository development (Adeyinka & Ojo, 2020; Mnisi & Onyango, 2021). Kenya has also implemented active preservation strategies in institutions like the University of Nairobi, preserving thousands of digital documents through a structured repository approach (Mutula & Wamuyu, 2025; Mutula & Wamuyu, 2022).

---

### **1.1.6 Digital Preservation and Academic Records Management in Cameroon**

In Cameroon, academic record preservation is a significant concern due to inadequate infrastructure, limited resources, and insufficient professional expertise (Adeyinka T., 2023). Many universities still rely on semi-manual processes, fragmented record-keeping systems, and weak backup mechanisms. Studies show that several Cameroonian institutions lack clear digital preservation policies, leading to the loss of valuable academic data and weakening the reliability of academic credentials (Nguimbous & Tchouamou, 2020). For example, the University of Yaounde I has reportedly struggled with record loss due to inadequate storage and preservation measures (Ndongo, 2023).

In response, the Ministry of Higher Education introduced a national digital preservation policy focusing on preservation planning, metadata management, and digital rights protection (MINESUP, 2022). Some institutions such as the University of Douala have adopted digital repositories and metadata-based systems aimed at improving record accessibility and reducing loss (Mbassi, 2021).

At the University of Bamenda, where this study will be carried out, digital preservation has become increasingly important due to growing dependence on electronic academic administration. The university has created a digital repository to preserve and disseminate academic records and institutional documents (University of Bamenda, 2022). However, significant difficulties remain, including limited technical resources, poor storage expansion capability, weak staff training, and inconsistent preservation procedures. This study therefore seeks to investigate the digital preservation strategies used at the University of Bamenda and assess how they affect the maintenance of academic records, with the aim of proposing feasible and sustainable improvements.

---

## **1.2 Statement of the Problem**

Academic records are crucial for the continuity and credibility of educational institutions, yet they are increasingly vulnerable to loss, damage, and manipulation. At the University of Bamenda, traditional paper-based record systems are still common in many departments and administrative units, but such systems are vulnerable to deterioration due to environmental factors including humidity, mould, dust, and poor storage conditions (Smith, 2020). Furthermore, the absence of standardized filing and archiving procedures has contributed to disorganization and delays, making it difficult for students, staff, and external bodies to access accurate academic records promptly (Johnson, 2021).

With increasing reliance on digital systems across educational administration, the inadequacy of current record-keeping methods becomes more evident. Digital records, though easier to store and retrieve, introduce new risks including cyber threats, system failure, file corruption, accidental deletion, software obsolescence, and poor backup procedures. This creates a pressing need for effective digital preservation strategies to protect the authenticity and usability of academic records.

In response, the University of Bamenda has initiated measures such as establishing a centralized records office and introducing a basic electronic record management system (Morris, 2022). Staff training has been introduced to improve skills in handling digital data and electronic record systems (Adams, 2021). Despite these improvements, the institution still faces persistent problems such as inadequate financing, limited infrastructure, unstable storage systems, and weak enforcement of record management procedures (Nguyen, 2023).

If these challenges are not effectively addressed, the consequences could be severe. Students may experience delays or difficulty accessing transcripts and certificates, affecting opportunities for employment and further education (Nguimbous, 2020). The University's credibility may also decline due to missing or inaccurate academic data, reducing public confidence among employers, prospective students, alumni, and partner institutions (Williams, 2023). In addition, weak record preservation may create legal and administrative disputes regarding academic qualifications, leading to institutional and reputational risk (Ngah & Hussin, 2019).

Despite attempts to modernize academic record systems, issues persist in maintaining secure, accurate, and accessible records. Therefore, this study examines the effect of digital preservation strategies on maintaining academic records at the University of Bamenda.

---

## **1.3 Research Questions**

### **1.3.1 Main Research Question**

What are the effects of digital preservation strategies on the maintenance of academic records at the University of Bamenda?

### **1.3.2 Specific Research Questions**

1. What is the effect of digital migration strategy on the maintenance of academic records at the University of Bamenda?
2. What is the effect of digital replication strategy on the maintenance of academic records at the University of Bamenda?
3. What is the effect of digital refreshing strategy on the maintenance of academic records at the University of Bamenda?

---

## **1.4 Research Objectives**

### **1.4.1 Main Research Objective**

To analyse the effects of digital preservation strategies on the maintenance of academic records at the University of Bamenda.

### **1.4.2 Specific Research Objectives**

1. To investigate the effect of digital migration strategy on the maintenance of academic records at the University of Bamenda.
2. To examine the effect of digital replication strategy on the maintenance of academic records at the University of Bamenda.
3. To analyse the effect of digital refreshing strategy on the maintenance of academic records at the University of Bamenda.

---

## **1.5 Research Hypotheses**

1. **H1:** Digital migration has no statistically significant effect on the maintenance of academic records at the University of Bamenda.
2. **H2:** Digital replication has no statistically significant effect on the maintenance of academic records at the University of Bamenda.
3. **H3:** Digital refreshing has no statistically significant effect on the maintenance of academic records at the University of Bamenda.

---

## **1.6 Significance of the Study**

This research is significant to the University of Bamenda because it will provide clear insights into the effectiveness of its current digital preservation approaches. It will identify institutional strengths and weaknesses in record management, highlight key areas requiring improvement, and provide practical recommendations for strengthening digital preservation strategies. The findings will support the development of policies and procedures that improve record integrity, security, and accessibility, thereby supporting institutional credibility and improving service delivery.

The study is significant to policymakers because it provides evidence-based recommendations relevant for designing and enforcing digital preservation frameworks in higher education. Policymakers can use the findings to inform decisions on infrastructure investment, national policy alignment, training priorities, and institutional compliance requirements. Strengthening digital preservation in universities supports accountability, transparency, and improved educational administration nationally.

The study is significant to researchers because it contributes to the growing body of knowledge on digital preservation strategies in academic record maintenance, especially within developing contexts. It will highlight challenges, opportunities, and evidence-driven best practices that can guide further research and the development of innovative record preservation models suitable for institutions with limited resources.

---

## **1.7 Organisation of the Study**

This work begins with the preliminary pages, including the declaration, acknowledgement, abstract, and table of contents. The research is arranged into five chapters. Chapter One introduces the study and covers the background, statement of the problem, research questions, objectives, hypotheses, significance of the study, and the organisation of the research.

Chapter Two focuses on the literature review and is divided into conceptual, theoretical, and empirical literature. Chapter Three presents the methodology, covering the study area, research design, sources and methods of data collection, methods of analysis, and validity of results. Chapter Four contains data presentation, analysis, and discussion of findings. Finally, Chapter Five presents the conclusion, recommendations, areas for further studies, references, and appendices.




**CHAPTER TWO**

**LITERATURE REVIEW**

### **2.0 Introduction to the Chapter**

This chapter reviews existing literature related to digital preservation strategies and the maintenance of academic records. The purpose of this chapter is to establish a strong academic foundation for the study by examining relevant concepts, theories, and empirical studies. It presents a conceptual review of key terms such as digital preservation, academic records, and record maintenance. It also explains major digital preservation strategies including migration, replication, and refreshing, which form the independent variables of this study. In addition, the chapter discusses theoretical perspectives that support digital preservation practices in institutions and reviews empirical findings from previous studies to identify gaps that justify the current research.

---

## **2.1 Conceptual Literature**

### **2.1.1 Digital Preservation**

Digital preservation refers to the processes and activities involved in ensuring that digital information remains accessible, authentic, and usable over time. It involves more than simply saving files on a computer system; it requires continuous monitoring, planning, and adaptation to prevent loss due to technological changes or degradation. Egbe and Ifeakachuku (2022) define digital preservation as the managed activities necessary for ensuring both the long-term maintenance of a digital object's integrity and the continued accessibility of its contents over time. This definition highlights that digital preservation is an active and ongoing process aimed at protecting digital materials from potential damage.

Modern scholars argue that digital information is fragile because it depends on software, hardware, storage media, and file formats that may become obsolete. Bountouri (2021) explains that digital materials can become inaccessible within a short time due to format abandonment, software updates, or failure of storage devices. In academic institutions, where records are generated daily and stored digitally, digital preservation becomes a critical requirement for ensuring institutional accountability and long-term record availability.

Corrado and Moulaison Sandy (2020) describe digital preservation as a structured process of ensuring continued access to digital resources through planning, resource allocation, and the use of appropriate preservation methods. Their perspective emphasizes the organizational commitment required for preservation activities to succeed. Digital preservation therefore involves both technical mechanisms such as backups and format migration, and administrative frameworks such as policies, staff training, and preservation standards.

---

### **2.1.1.1 Objectives of Digital Preservation**

The main objective of digital preservation is to ensure that digital content remains available and readable regardless of technological change. The goal is to prevent the loss of digital assets and guarantee that digital records can be retrieved and used in the future. In the context of academic records, preservation ensures that transcripts, results, admission records, and graduation documents remain reliable for future verification.

Digital preservation also aims to ensure integrity and authenticity. Integrity ensures that records remain complete and unchanged, while authenticity ensures that records are original and trustworthy. These objectives are essential in academic institutions, where record accuracy affects students' career opportunities, university credibility, and institutional compliance with regulations.

---

### **2.1.1.2 Key Characteristics of Digital Preservation**

Digital preservation is defined by key characteristics such as continuity, security, and strategic management. It is continuous because records require long-term monitoring to prevent corruption or obsolescence. It is secure because preserved materials must be protected from unauthorised access, manipulation, or cyber-attacks. It is strategic because institutions must plan for technological changes, storage upgrades, and long-term funding needs.

Furthermore, preservation focuses on usability. A record may exist in storage, but if it cannot be opened due to outdated software or corrupted format, then it has failed preservation goals. Therefore, digital preservation must ensure that digital records remain accessible and interpretable over time.

---

### **2.1.1.3 Threats to Digital Preservation**

There are several threats that can affect digital preservation in academic institutions. One of the biggest threats is technological obsolescence, where files become unreadable due to outdated software or unsupported formats. Hardware failure is also a major risk, as storage devices such as hard drives and servers can crash and lead to permanent data loss. Accidental deletion or human error is another frequent threat, especially where record systems are poorly managed or staff lack proper training.

Cybersecurity threats, including malware and hacking, also endanger digital records. Institutions that lack secure systems and proper access control are vulnerable to data breaches and manipulation. Poor infrastructure, limited funding, and inconsistent power supply further intensify preservation challenges in developing countries.

---

### **2.1.2 Academic Records**

Academic records refer to documents and data that provide official evidence of a student's academic history within an educational institution. These records include admission files, registration details, course forms, results, transcripts, attendance reports, disciplinary records, and graduation certificates. Academic records serve as proof of academic achievement and are essential for monitoring student progression and institutional performance.

Academic records can be classified into physical records and digital records. Physical academic records include paper files stored in cabinets, folders, and archives, while digital records exist in electronic formats stored on databases, servers, cloud systems, and digital repositories. The shift from paper records to electronic records has improved accessibility and efficiency, but it has also introduced concerns related to security, digital loss, and long-term accessibility.

---

### **2.1.2.1 Importance of Academic Records in Universities**

Academic records are important because they support decision-making, accountability, and operational continuity in universities. They enable institutions to track student performance, plan academic activities, provide transcripts, and verify qualifications. Without reliable academic records, universities may face challenges in proving academic results, issuing accurate certificates, and responding to administrative or legal queries.

Academic records also play a key role in employment and further education. Employers and scholarship boards often demand transcripts and proof of graduation. Therefore, a university's ability to maintain and preserve academic records directly affects the opportunities available to its students and graduates.

---

### **2.1.3 Maintenance of Academic Records**

Maintenance of academic records refers to the systematic process of collecting, organizing, storing, protecting, updating, and retrieving academic records in a way that guarantees their long-term accessibility and reliability. Record maintenance ensures that academic data remains accurate and complete from the point of creation to the point of disposal or archiving.

Effective record maintenance requires clear procedures, adequate infrastructure, trained personnel, and reliable storage systems. In modern academic environments, record maintenance also includes digital processes such as database management, access control systems, backup scheduling, and preservation planning. Poor record maintenance results in disorganized files, delays in service delivery, and risk of record loss.

---

### **2.1.3.1 Factors Affecting Academic Records Maintenance**

Several factors influence the maintenance of academic records in institutions. These factors include staff competency, availability of technological infrastructure, organizational policies, leadership commitment, and financial support. Institutions that invest in staff training and structured information systems tend to maintain more accurate and accessible records.

Other factors include security measures, backup strategies, and institutional culture. A weak culture of accountability and professionalism can lead to careless handling of records, poor documentation practices, and limited emphasis on record protection.

---

### **2.1.4 Digital Preservation Strategies**

Digital preservation strategies refer to deliberate techniques used to protect digital records from loss, corruption, or obsolescence. These strategies are designed to ensure that digital information remains accessible and usable across time despite changes in technology. In this study, the digital preservation strategies considered include digital migration, digital replication, and digital refreshing.

---

### **2.1.4.1 Digital Migration Strategy**

Digital migration refers to the process of transferring digital records from one technological environment to another in order to maintain accessibility. This may involve moving data from old file formats to newer formats, or transferring records from outdated systems to modern platforms. Migration is commonly used when software or hardware becomes obsolete and no longer supports older formats.

In academic institutions, digital migration is important because academic records must remain readable for many years. Migrating transcript records, student databases, and examination data ensures that records remain accessible even when institutions upgrade their management systems. However, migration must be carefully managed because it may result in data loss or alteration if not properly executed.

---

### **2.1.4.2 Digital Replication Strategy**

Digital replication refers to creating copies of digital records and storing them in multiple locations to prevent data loss. Replication ensures that if one copy is corrupted or destroyed, another copy can be recovered. Replication can be achieved through local backups, external hard drives, cloud storage, and institutional repositories.

Replication is crucial in academic institutions because academic records are valuable assets that should not be lost under any circumstances. By replicating student records across storage systems, universities improve data availability and reduce risks caused by equipment failure, disasters, or cyber-attacks. Replication also supports continuity in institutional services, especially when one system fails unexpectedly.

---

### **2.1.4.3 Digital Refreshing Strategy**

Digital refreshing refers to the process of moving digital records from ageing storage media to newer storage media without changing the content or format. The goal is to prevent data loss caused by physical deterioration of storage devices. Storage devices such as CDs, USB drives, and hard disks have limited lifespans and may degrade over time, leading to file corruption.

In academic institutions, refreshing is important because records stored on outdated media may become unreadable after several years. Refreshing ensures that records remain stable and retrievable by transferring them to modern storage devices or upgraded servers. It also supports long-term preservation by ensuring that storage media remains functional and reliable.

---

### **2.1.5 Digital Repositories in Academic Institutions**

Digital repositories are platforms used for storing, organizing, and preserving digital content for long-term access. Universities use repositories to preserve academic outputs such as theses, dissertations, research papers, and institutional documents. Digital repositories also serve as a central place for storing academic records, ensuring consistent access and protection.

Digital repositories support digital preservation by integrating strategies such as metadata management, access control, file integrity checks, and replication. In many institutions, repositories are key tools for ensuring that digital records remain accessible in the long term.

---

### **2.1.6 Digital Preservation Policies and Standards**

Digital preservation is most effective when guided by institutional policies and preservation standards. A digital preservation policy provides a framework outlining how records should be created, managed, protected, accessed, and preserved. It clarifies staff responsibilities and ensures consistency in preservation procedures.

International standards such as the Open Archival Information System (OAIS) model guide institutions in building trustworthy preservation systems. Preservation standards also emphasize metadata, integrity checks, and audit mechanisms. Without these policies, preservation strategies may be inconsistent and poorly implemented.

---

## **2.2 Theoretical Framework**

This study is supported by theories that explain how digital records can be preserved in an organized and reliable manner. Two key theories that guide this study include the Records Continuum Model and the Open Archival Information System (OAIS) framework.

---

### **2.2.1 Records Continuum Model**

The Records Continuum Model views records management as a continuous process that begins from the creation of a record and continues through its organization, storage, use, and preservation. This model rejects the idea that records move in separate stages such as creation, use, and archiving. Instead, it suggests that records should be managed throughout their entire life-cycle.

In universities, this model is relevant because academic records are continuously needed throughout student life and beyond graduation. By applying the continuum approach, institutions can design record systems that maintain accessibility and authenticity for both current administrative needs and long-term historical use.

---

### **2.2.2 Open Archival Information System (OAIS) Model**

The OAIS model provides a structured approach to digital preservation by defining how digital archives should ingest, manage, preserve, and provide access to digital information. It emphasizes preservation planning, storage management, and access mechanisms that ensure digital records remain usable over time.

The OAIS model is relevant to this study because it supports the concept of trusted preservation systems. Academic institutions that implement OAIS principles can better maintain digital records through standardized processes and controlled preservation mechanisms.

---

## **2.3 Empirical Literature Review**

Empirical literature refers to previous studies that have examined digital preservation strategies and record maintenance in different contexts. Many studies have explored how universities manage digital records and the challenges they face in preserving them.

Research in developing countries shows that many institutions struggle with poor infrastructure, limited funding, and lack of preservation expertise. These challenges lead to record loss, inconsistencies, and difficulty retrieving records when required. Studies also show that institutions that implement structured strategies such as replication and migration experience improved data accessibility and reduced record loss.

Other studies highlight that digital preservation requires more than technological tools. Institutional commitment, policies, staff training, and continuous evaluation play critical roles in ensuring successful academic record preservation. This suggests that preservation strategies must be supported by governance and professional competence.

---

## **2.4 Summary of Literature Review and Knowledge Gap**

From the reviewed literature, it is evident that digital preservation is essential for ensuring the integrity, accessibility, and sustainability of academic records. While many institutions globally have adopted preservation frameworks, universities in developing contexts face significant challenges that hinder effective preservation. Although studies have discussed digital preservation strategies broadly, limited research has focused specifically on the combined effects of migration, replication, and refreshing strategies on academic record maintenance in the University of Bamenda. This creates a research gap that this study aims to address.
"""

def test_document():
    print("=" * 70)
    print("GENERATING TEST DOCUMENT")
    print("=" * 70)
    
    # Create processor with default policy
    policy = FormatPolicy()
    processor = DocumentProcessor(policy=policy)
    
    # Process the text
    result, images, shapes = processor.process_text(TEST_DOCUMENT)
    structured_data = result['structured']
    
    # Create Word generator
    generator = WordGenerator(policy=policy)
    
    # Generate document
    output_path = os.path.join(os.path.dirname(__file__), 'test_heading_output.docx')
    generator.generate(
        structured_data=structured_data,
        output_path=output_path,
        images=images,
        shapes=shapes,
        font_size=12,
        line_spacing=2.0,
        margins={'left': 3.0, 'top': 2.5, 'bottom': 2.5, 'right': 2.5},
        include_toc=False
    )
    
    print(f"\nDocument generated: {output_path}")
    print("\nPlease open the document and verify:")
    print("  1. Sections like 1.1, 1.2, 1.3, etc. do NOT start on new pages")
    print("  2. Subsections like 1.1.1, 1.1.2, etc. do NOT start on new pages")
    print("  3. Only CHAPTER ONE and CHAPTER TWO start on new pages")
    print("  4. The --- horizontal rules are NOT visible in the document")
    print("=" * 70)

if __name__ == '__main__':
    test_document()

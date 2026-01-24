"""
Test script to verify that second-level headings (2.0, 2.1, etc.) 
do NOT start on new pages after the fix.
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

Australia has also advanced digital preservation through clear institutional policy frameworks. Colin and Paul (2021) highlight that national digital preservation policies provide guidance on preservation priorities, format management, data integrity, and collection sustainability (Colin & Paul, 2021). Similarly, Canada has adopted structured digital preservation frameworks, with **Library and Archives Canada (LAC)** emphasizing trusted digital repositories and digital collection management planning (Parent & Pagé, 2022; Wilson, 2024).

---

### **1.1.4 Digital Preservation Challenges in Developing Countries**

In developing countries, digital preservation is often a pressing challenge due to limited infrastructure, financial constraints, and inadequate technical expertise. Many institutions struggle with inconsistent electricity supply, limited ICT capacity, weak policy enforcement, and insufficient storage resources. The absence of effective strategies has resulted in loss and inaccessibility of records, affecting institutional transparency and academic credibility.

For example, in India, Kumar and Tripathi (2020) stress that digital preservation remains critical for ensuring long-term access to academic records, especially research outputs and institutional archives (Kumar & Tripathi, 2021). Government efforts like the **National Digital Preservation Program** aim to promote standardized preservation practices and national frameworks (Chakraborty, 2023).

---

### **1.1.5 Digital Preservation in Africa**

In Africa, digital preservation is a major concern because many academic institutions face serious constraints such as poor infrastructure, limited funding, weak technical capacity, and insufficient staff training. Unlike developed countries where digital preservation is structured and standardized, many African universities lack comprehensive frameworks guiding record preservation practices (Adeyinka & Ojo, 2021). Onyema and Oluwaseyi (2020) observed that only a small number of African universities have clear digital preservation policies, leading to frequent loss of academic records and compromised trust in academic systems (Onyema & Oluwaseyi, 2017).

South Africa has made notable progress, with scholars emphasizing the need for long-term preservation mechanisms that ensure sustainability and access (Mnisi & Onyango, 2022). Nigeria has attempted to expand digital repositories for academic record preservation, especially theses and dissertations, through institutional strategies and repository development (Adeyinka & Ojo, 2020; Mnisi & Onyango, 2021). Kenya has also implemented active preservation strategies in institutions like the University of Nairobi, preserving thousands of digital documents through a structured repository approach (Mutula & Wamuyu, 2025; Mutula & Wamuyu, 2022).

---

### **1.1.6 Digital Preservation and Academic Records Management in Cameroon**

In Cameroon, academic record preservation is a significant concern due to inadequate infrastructure, limited resources, and insufficient professional expertise (Adeyinka T., 2023). Many universities still rely on semi-manual processes, fragmented record-keeping systems, and weak backup mechanisms. Studies show that several Cameroonian institutions lack clear digital preservation policies, leading to the loss of valuable academic data and weakening the reliability of academic credentials (Nguimbous & Tchouamou, 2020).

---

## **1.2 Statement of the Problem**

Academic records are crucial for the continuity and credibility of educational institutions, yet they are increasingly vulnerable to loss, damage, and manipulation. At the University of Bamenda, traditional paper-based record systems are still common in many departments and administrative units, but such systems are vulnerable to deterioration due to environmental factors including humidity, mould, dust, and poor storage conditions (Smith, 2020).

With increasing reliance on digital systems across educational administration, the inadequacy of current record-keeping methods becomes more evident. Digital records, though easier to store and retrieve, introduce new risks including cyber threats, system failure, file corruption, accidental deletion, software obsolescence, and poor backup procedures. This creates a pressing need for effective digital preservation strategies to protect the authenticity and usability of academic records.

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

This research is significant to the University of Bamenda because it will provide clear insights into the effectiveness of its current digital preservation approaches. It will identify institutional strengths and weaknesses in record management, highlight key areas requiring improvement, and provide practical recommendations for strengthening digital preservation strategies.

---

## **1.7 Organisation of the Study**

This work begins with the preliminary pages, including the declaration, acknowledgement, abstract, and table of contents. The research is arranged into five chapters. Chapter One introduces the study and covers the background, statement of the problem, research questions, objectives, hypotheses, significance of the study, and the organisation of the research.




**CHAPTER TWO**

**LITERATURE REVIEW**

### **2.0 Introduction to the Chapter**

This chapter reviews existing literature related to digital preservation strategies and the maintenance of academic records. The purpose of this chapter is to establish a strong academic foundation for the study by examining relevant concepts, theories, and empirical studies.

---

## **2.1 Conceptual Literature**

### **2.1.1 Digital Preservation**

Digital preservation refers to the processes and activities involved in ensuring that digital information remains accessible, authentic, and usable over time. It involves more than simply saving files on a computer system; it requires continuous monitoring, planning, and adaptation to prevent loss due to technological changes or degradation. Egbe and Ifeakachuku (2022) define digital preservation as the managed activities necessary for ensuring both the long-term maintenance of a digital object's integrity and the continued accessibility of its contents over time.

Modern scholars argue that digital information is fragile because it depends on software, hardware, storage media, and file formats that may become obsolete. Bountouri (2021) explains that digital materials can become inaccessible within a short time due to format abandonment, software updates, or failure of storage devices.

---

### **2.1.1.1 Objectives of Digital Preservation**

The main objective of digital preservation is to ensure that digital content remains available and readable regardless of technological change. The goal is to prevent the loss of digital assets and guarantee that digital records can be retrieved and used in the future.

---

### **2.1.1.2 Key Characteristics of Digital Preservation**

Digital preservation is defined by key characteristics such as continuity, security, and strategic management. It is continuous because records require long-term monitoring to prevent corruption or obsolescence. It is secure because preserved materials must be protected from unauthorised access, manipulation, or cyber-attacks.

---

### **2.1.1.3 Threats to Digital Preservation**

There are several threats that can affect digital preservation in academic institutions. One of the biggest threats is technological obsolescence, where files become unreadable due to outdated software or unsupported formats. Hardware failure is also a major risk, as storage devices such as hard drives and servers can crash and lead to permanent data loss.

---

### **2.1.2 Academic Records**

Academic records refer to documents and data that provide official evidence of a student's academic history within an educational institution. These records include admission files, registration details, course forms, results, transcripts, attendance reports, disciplinary records, and graduation certificates.

---

### **2.1.2.1 Importance of Academic Records in Universities**

Academic records are important because they support decision-making, accountability, and operational continuity in universities. They enable institutions to track student performance, plan academic activities, provide transcripts, and verify qualifications.

---

### **2.1.3 Maintenance of Academic Records**

Maintenance of academic records refers to the systematic process of collecting, organizing, storing, protecting, updating, and retrieving academic records in a way that guarantees their long-term accessibility and reliability.

---

### **2.1.3.1 Factors Affecting Academic Records Maintenance**

Several factors influence the maintenance of academic records in institutions. These factors include staff competency, availability of technological infrastructure, organizational policies, leadership commitment, and financial support.

---

### **2.1.4 Digital Preservation Strategies**

Digital preservation strategies refer to deliberate techniques used to protect digital records from loss, corruption, or obsolescence. These strategies are designed to ensure that digital information remains accessible and usable across time despite changes in technology.

---

### **2.1.4.1 Digital Migration Strategy**

Digital migration refers to the process of transferring digital records from one technological environment to another in order to maintain accessibility. This may involve moving data from old file formats to newer formats, or transferring records from outdated systems to modern platforms.

---

### **2.1.4.2 Digital Replication Strategy**

Digital replication refers to creating copies of digital records and storing them in multiple locations to prevent data loss. Replication ensures that if one copy is corrupted or destroyed, another copy can be recovered.

---

### **2.1.4.3 Digital Refreshing Strategy**

Digital refreshing refers to the process of moving digital records from ageing storage media to newer storage media without changing the content or format. The goal is to prevent data loss caused by physical deterioration of storage devices.

---

## **2.2 Theoretical Framework**

This study is supported by theories that explain how digital records can be preserved in an organized and reliable manner. Two key theories that guide this study include the Records Continuum Model and the Open Archival Information System (OAIS) framework.

---

### **2.2.1 Records Continuum Model**

The Records Continuum Model views records management as a continuous process that begins from the creation of a record and continues through its organization, storage, use, and preservation.

---

### **2.2.2 Open Archival Information System (OAIS) Model**

The OAIS model provides a structured approach to digital preservation by defining how digital archives should ingest, manage, preserve, and provide access to digital information.

---

## **2.3 Empirical Literature Review**

Empirical literature refers to previous studies that have examined digital preservation strategies and record maintenance in different contexts. Many studies have explored how universities manage digital records and the challenges they face in preserving them.

---

## **2.4 Summary of Literature Review and Knowledge Gap**

From the reviewed literature, it is evident that digital preservation is essential for ensuring the integrity, accessibility, and sustainability of academic records. While many institutions globally have adopted preservation frameworks, universities in developing contexts face significant challenges that hinder effective preservation.
"""


def test_page_break_fix():
    """Test that second-level headings (2.0, 2.1, etc.) don't get page breaks."""
    print("=" * 70)
    print("TESTING PAGE BREAK FIX FOR SECOND-LEVEL HEADINGS")
    print("=" * 70)
    
    # Process the document
    processor = DocumentProcessor()
    result, images, shapes = processor.process_text(TEST_DOCUMENT)
    
    # Analyze structured data for page breaks
    print("\n📋 ANALYZING STRUCTURED SECTIONS:")
    print("-" * 70)
    
    sections_with_page_breaks = []
    all_sections = []
    
    for section in result.get('structured', []):
        heading = section.get('heading', 'N/A')
        level = section.get('level', 0)
        needs_page_break = section.get('needs_page_break', False)
        use_page_break_before = section.get('use_page_break_before', False)
        
        all_sections.append({
            'heading': heading,
            'level': level,
            'needs_page_break': needs_page_break,
            'use_page_break_before': use_page_break_before
        })
        
        if needs_page_break or use_page_break_before:
            sections_with_page_breaks.append({
                'heading': heading,
                'level': level,
                'needs_page_break': needs_page_break,
                'use_page_break_before': use_page_break_before
            })
    
    # Print all sections
    print("\nAll Sections:")
    for i, s in enumerate(all_sections):
        pb_info = ""
        if s['needs_page_break'] or s['use_page_break_before']:
            pb_info = " ⚠️ PAGE BREAK"
        print(f"  {i+1}. Level {s['level']}: {s['heading'][:60]}...{pb_info}")
    
    # Check for problematic page breaks on level 2+ sections
    print("\n" + "=" * 70)
    print("🔍 CHECKING FOR INCORRECT PAGE BREAKS ON LEVEL 2+ SECTIONS:")
    print("-" * 70)
    
    problematic_sections = []
    for s in sections_with_page_breaks:
        # Check if it's a numbered sub-section (2.0, 2.1, 2.1.1, etc.)
        import re
        is_numbered = bool(re.match(r'^\d+\.\d+', s['heading'].strip()))
        is_level_2_plus = s['level'] >= 2
        
        if is_numbered or is_level_2_plus:
            problematic_sections.append(s)
            print(f"  ❌ PROBLEM: Level {s['level']} heading '{s['heading'][:50]}' has page break!")
    
    if not problematic_sections:
        print("  ✅ No problematic page breaks found on level 2+ sections!")
    
    # Generate Word document
    print("\n" + "=" * 70)
    print("📄 GENERATING WORD DOCUMENT...")
    print("-" * 70)
    
    policy = FormatPolicy()
    
    generator = WordGenerator(policy=policy)
    output_path = os.path.join(os.path.dirname(__file__), 'test_page_break_output.docx')
    
    generator.generate(
        structured_data=result.get('structured', []),
        output_path=output_path,
        font_size=12,
        line_spacing=2.0,
        include_toc=False
    )
    
    print(f"  ✅ Document generated: {output_path}")
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 SUMMARY:")
    print("-" * 70)
    print(f"  Total sections: {len(all_sections)}")
    print(f"  Sections with page breaks: {len(sections_with_page_breaks)}")
    print(f"  Problematic page breaks on level 2+ sections: {len(problematic_sections)}")
    
    if len(problematic_sections) == 0:
        print("\n  ✅ TEST PASSED: No unwanted page breaks on second-level headings!")
    else:
        print("\n  ❌ TEST FAILED: Some second-level headings still have page breaks!")
        for s in problematic_sections:
            print(f"      - {s['heading'][:50]}")
    
    print("\n" + "=" * 70)
    return len(problematic_sections) == 0


if __name__ == "__main__":
    success = test_page_break_fix()
    exit(0 if success else 1)

#!/usr/bin/env python
"""Check for section breaks in full text"""

test_content = """Discussions of Findings

This section presents the key findings from our research methodology and analysis.

**Rewards**

Rewards represent one of the most critical components of our study. They serve as both incentive mechanisms and performance indicators.

1. Implications for Students:

a. Improved academic performance through better resource allocation
b. Enhanced engagement with course materials
c. Stronger connections with peer support networks
d. Better understanding of personal learning styles

---

2. Institutional Benefits:

a. More effective curriculum design based on empirical data
b. Better resource planning and budget allocation
c. Improved student retention rates
d. Enhanced reputation and accreditation standing

**Challenges and Limitations**

Our research identified several important challenges that warrant discussion.

- Time constraints limited the depth of analysis
- Resource limitations affected sample size
- Institutional policy changes mid-study required adaptation
- Technology infrastructure limitations

---

**Conclusions**

The structured approach demonstrated significant improvements across all measured dimensions.
"""

print("Lines with '---':")
for i, line in enumerate(test_content.split('\n')):
    if '---' in line:
        print(f"Line {i}: {repr(line)} (stripped: {repr(line.strip())})")

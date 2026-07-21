from markdown_pdf import MarkdownPdf, Section

markdown_content = """
# 1. Executive Summary

The primary objective of this Exploratory Data Analysis (EDA) is to analyze customer demographic, behavioral, and transactional data to uncover key patterns driving customer churn in a telecommunications service provider. By conducting rigorous statistical and visual analysis, this project identifies high-risk churn segments and delivers actionable data preprocessing recommendations to prepare the dataset for predictive machine learning workflows.

### Key Findings
* **Baseline Churn Rate:** Overall customer churn stands at **26.5%** across the analyzed dataset (1,869 out of 7,043 total instances).
* **Contract Type Sensitivity:** Customers on **month-to-month contracts** exhibit a significantly higher churn rate (~42.7%) compared to those on one-year (~11.2%) or two-year (~2.8%) commitments.
* **Payment Method Friction:** Customers paying via **electronic check** account for a disproportionately high churn rate (~45.3%) compared to automated payment methods like credit card or bank transfer (~15%).
* **Critical Tenure Window:** Customer attrition drops sharply after the first **12 months** of service, establishing early-stage retention as the most critical period for intervention.
"""

pdf = MarkdownPdf(toc_level=2)
pdf.add_section(Section(markdown_content))
pdf.save("EDA_Executive_Summary.pdf")
print("PDF generated successfully as 'EDA_Executive_Summary.pdf'")
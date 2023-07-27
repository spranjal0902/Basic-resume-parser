import re
import json

def parse_resume(resume_text):
    # Regular expressions for education, work experience, and skills
    education_pattern = r"(?i)education|qualification|degree|certificate.*?:\s*(.*)"
    experience_pattern = r"(?i)work experience|experience.*?:\s*(.*)"
    skills_pattern = r"(?i)skills|technical skills.*?:\s*(.*)"

    # Initialize the extracted data dictionary
    extracted_data = {
        "education": "",
        "work_experience": "",
        "skills": "",
    }

    # Extract education, work experience, and skills using regular expressions
    education_match = re.search(education_pattern, resume_text)
    if education_match:
        extracted_data["education"] = education_match.group(1)

    experience_match = re.search(experience_pattern, resume_text)
    if experience_match:
        extracted_data["work_experience"] = experience_match.group(1)

    skills_match = re.search(skills_pattern, resume_text)
    if skills_match:
        extracted_data["skills"] = skills_match.group(1)

    # Prepare the JSON output
    output_data = json.dumps(extracted_data, indent=4)
    return output_data

# Test the resume parser
resume_text = """
Name: Alex
Education: Bachelor of Science in Computer Science, XYZ University, 2020
Work Experience: 
- Software Engineer, ABC Tech, 2020-present
- Intern, XYZ Corp, 2019
Skills: Python, Java, C++, Machine Learning
"""

parsed_json = parse_resume(resume_text)
print(parsed_json)

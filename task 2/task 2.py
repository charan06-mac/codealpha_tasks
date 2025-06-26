import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Regular expression for emails
        emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', content)

        with open(output_file, 'w') as out_file:
            for email in emails:
                out_file.write(email + '\n')

        print(f"✅ Extracted {len(emails)} emails and saved to '{output_file}'")

    except FileNotFoundError:
        print("❌ Input file not found!")

# Example usage
extract_emails("input.txt", "emails.txt")

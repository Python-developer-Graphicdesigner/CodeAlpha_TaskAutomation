"""
Task Automation with Python: Email Address Extractor
CodeAlpha Python Programming Internship - Task 3

Automates a small repetitive task: scans a .txt file, finds every email
address inside it using a regular expression, and saves the unique
addresses into a new output file.

Key concepts used: os, re, file handling.
"""

import os
import re


# Regular expression that matches standard email address patterns
EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')


def extract_emails_from_file(input_path):
    """
    Reads the input text file and returns a sorted list of unique
    email addresses found inside it.
    """
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Could not find file: {input_path}")

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    found_emails = EMAIL_PATTERN.findall(content)

    # Remove duplicates while keeping the list sorted and clean
    unique_emails = sorted(set(email.lower() for email in found_emails))
    return unique_emails


def save_emails_to_file(emails, output_path):
    """
    Writes the list of emails to the output file, one per line.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")


def run():
    print("=" * 55)
    print(" Email Address Extractor - Task Automation Script")
    print("=" * 55)

    input_path = input("Enter the path of the .txt file to scan: ").strip()
    output_path = input("Enter the path for the output file (e.g. found_emails.txt): ").strip()

    if not output_path:
        output_path = "found_emails.txt"

    try:
        emails = extract_emails_from_file(input_path)
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        return

    if not emails:
        print("\nNo email addresses were found in the file.")
        return

    save_emails_to_file(emails, output_path)

    print(f"\nFound {len(emails)} unique email address(es):")
    for email in emails:
        print(" -", email)

    print(f"\nSaved to: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    run()

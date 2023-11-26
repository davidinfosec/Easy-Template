"""
Program by David D. (DavidInfosec)
"""


import os
import shutil
import calendar
import sys

def generate_template_folders(month, year, day, num_parents, num_subfolders, use_template, subfolder_prefix):
    # Calculate the day of the week for the 1st day of the month
    first_day_of_month = calendar.weekday(year, month, 1)

    # Find the first occurrence of the specified day in the month
    first_occurrence = (day - first_day_of_month + 7) % 7 + 1

    # Generate parent folders for the specified day of the week
    for i in range(num_parents):
        current_day = first_occurrence + (i * 7)

        # Adjust for rollover into the next month
        while current_day > calendar.monthrange(year, month)[1]:
            current_day -= calendar.monthrange(year, month)[1]
            month += 1
            if month > 12:
                month = 1
                year += 1

        # Create root folder for the month, year, and specified day
        root_folder = f"ET {year}-{month:02d}-{current_day:02d} {calendar.day_name[day]}"

        os.makedirs(root_folder)

        # Generate subfolders
        for j in range(1, num_subfolders + 1):
            subfolder_name = f"{subfolder_prefix}_{j}" if subfolder_prefix else f"Session_{j}"
            subfolder = os.path.join(root_folder, subfolder_name)
            os.makedirs(subfolder)

            # Create .rpp files with content from the template files
            template_folder = "Template"

            # Handle parent template files
            parent_template_folder = os.path.join(template_folder, "parent")
            for template_file in os.listdir(parent_template_folder):
                template_path = os.path.join(parent_template_folder, template_file)
                target_path = os.path.join(root_folder, f"{template_file}")

                if use_template and os.path.isfile(template_path):
                    shutil.copy(template_path, target_path)
                    print(f"Parent template file created: {target_path}")

            # Handle subfolder template files
            sub_template_folder = os.path.join(template_folder, "sub")
            for template_file in os.listdir(sub_template_folder):
                template_path = os.path.join(sub_template_folder, template_file)
                target_path = os.path.join(subfolder, template_file)

                if use_template and os.path.isfile(template_path):
                    shutil.copy(template_path, target_path)
                    print(f"Subfolder template file created: {target_path}")

        # Create README.md file in the parent folder
        readme_path = os.path.join(root_folder, "README.md")
        with open(readme_path, "w") as readme_file:
            readme_file.write("# Root README.md\n\nGenerated by etgen.py")

        print(f"README.md file created at: {readme_path}")


if __name__ == "__main__":
    # Get user input
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))

    # Display numbered list of days
    days_of_week = list(calendar.day_name)
    for i, day in enumerate(days_of_week, start=1):
        print(f"{i}. {day}")

    day_number = int(input("Enter the number corresponding to the day of the week: "))
    selected_day = days_of_week[day_number - 1]

    num_parents = int(input("Enter the number of parent folders (1 or more): "))
    num_subfolders = int(input("Enter the number of subfolders (1-100, or more with caution): "))

    # Warn if more than 100 subfolders
    if num_subfolders > 100:
        user_response = input(
            "⚠️ Warning: Specifying more than 100 subfolders may impact system performance. Do you want to proceed? (yes/no): ").lower()

        if user_response != "yes":
            print("Operation canceled. Please run the script again with a lower number of subfolders.")
            sys.exit()

    use_template = input("Do you want to use template files? (yes/no): ").lower() == "yes"
    subfolder_prefix = input("Enter a prefix for subfolders (press Enter for default 'Session'): ")

    # Generate template folders
    generate_template_folders(month, year, days_of_week.index(selected_day), num_parents, num_subfolders, use_template,
                              subfolder_prefix)

    print("Template folders created successfully!")

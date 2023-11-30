def calculate_grade(average_percentage):

    if average_percentage >= 90:

        return 'A'

    elif 80 <= average_percentage < 90:

        return 'B'

    elif 70 <= average_percentage < 80:

        return 'C'

    elif 60 <= average_percentage < 70:

        return 'D'

    else:

        return 'F'

 

def main():

    # Initialize variables

    total_marks = 0

    num_subjects = 5

 

    # Ask the user for marks in each subject

    for i in range(1, num_subjects + 1):

        marks = float(input(f"Enter marks for Subject {i}: "))

        total_marks += marks

 

    # Calculate average percentage

    average_percentage = total_marks / num_subjects

 

    # Assign grade based on average percentage

    grade = calculate_grade(average_percentage)

 

    # Display the results

    print("\nResults:")

    print(f"Total Marks: {total_marks}")

    print(f"Average Percentage: {average_percentage:.2f}%")

    print(f"Grade: {grade}")

 

if __name__ == "__main__":

    main()
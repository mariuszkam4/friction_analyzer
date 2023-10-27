import pandas as pd
import os
import matplotlib.pyplot as plt

# path to files folder
user_directory = input("Enter the path to the directory with the data for analysis:\n")
user_number = int(input("Indicate the number of measurements to be averaged (e.g. 100):\n"))

normalized_path = os.path.normpath(user_directory)

print("Data processing...")

if os.path.isdir(normalized_path):
    source_folder_path = normalized_path
    output_file_path = os.path.join(source_folder_path, "summary.csv")
    main_directory = os.path.basename(os.path.normpath(source_folder_path))

    results = pd.DataFrame()

    # Iterating over all files in a folder.
    for filename in os.listdir(source_folder_path):
        # Checking if the file is a .txt file
        if filename.endswith(".txt"):
            file_path = os.path.join(source_folder_path, filename)  # full path to the file

            try:
                # Loading text as a DataFrame
                df = pd.read_csv(file_path, delimiter="\t", skiprows=62, header=0, decimal=",")
                df['µ'] = df['µ'].astype(float)

                averages = df['µ'].groupby(df.index // user_number).mean()  # set grouping value
                averages.name = filename  # Set the column name to match the source file name

                # Add averages to the results
                results = pd.concat([results, averages], axis=1)

            except KeyError:
                print(f"File processing error: {file_path}")
                continue

    # Add an empty column at the beginning
    results.insert(0, "", "")

    # Save the results to the output file
    results.to_csv(output_file_path, sep=";", decimal=".", index=False, header=True)

    print("The data has been processed")
    print("Generating graph...")

    # Create a chart for each column in the DataFrame
    results.plot(kind='line')

    # Adding title and axis labels
    plt.title(main_directory)
    plt.xlabel('Quantity')
    plt.ylabel('Friction coefficient (μ)')

    # Displaying the chart
    plt.savefig(os.path.join(source_folder_path, "wykres.png"))
    print("Success!!!")
else:
    print("The provided directory does not exist. Please check the path and try again.")

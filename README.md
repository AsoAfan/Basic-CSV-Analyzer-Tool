# **Basic CSV Analyzer Tool**

A Python tool for analyzing and visualizing numerical data from CSV files. It allows users to upload CSV files, compute basic statistics (Mean, Median, Mode, Standard Deviation), and display the data with various graph types (e.g., Histogram, Box Plot). It also includes a CSV Generator feature that lets users create random CSV data based on selected columns and number of rows.

---

## **Features**

- **CSV Upload**: Load CSV files with numerical data.
- **Basic Statistics Calculation**: Compute and display mean, median, mode, standard deviation, and more.
- **Graph Visualization**: Display different types of graphs like histogram, box plot, scatter plot, etc.
- **CSV Generator**: Generate a new CSV with user-defined columns and random data.
- **Color Customization**: Choose the color for the charts.
- **Responsive Design**: The GUI adjusts dynamically for a better user experience.

---

## **Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AsoAfan/Basic-CSV-Analyzer-Tool.git
    cd csv-analyzer
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

---

## **Usage**

1. **Upload CSV**:  
   Click on the **"Upload CSV"** button in the sidebar to load a CSV file containing numerical data.
   
2. **Select Column**:  
   After uploading the CSV, choose the numerical column you want to analyze.

3. **Compute Statistics**:  
   Click the **"Compute Statistics"** button to calculate and display the basic statistical data for the selected column (Mean, Median, Mode, Standard Deviation).

4. **Visualize Data**:  
   Select the type of graph you want to visualize (e.g., Histogram, Box Plot) from the navigation menu and the chart will be displayed.

5. **Generate CSV**:  
   To generate a CSV file, click the **"Generate CSV"** button, specify the columns and the number of rows, and the tool will create a new CSV file with random values.

6. **Change Chart Color**:  
   Use the **color dropdown** to select a custom color for the charts.

---

## **CSV Generator**

The CSV Generator allows you to create a CSV with random data. 

1. Enter **column names** (comma-separated).
2. Enter the **number of rows** you want the CSV to contain.
3. Click **"Generate CSV"**, and the numerical file will be saved/overridden as `generated_data.csv`.

---

## **Directory Structure**

```
csv_analyzer/
│── main.py              # Entry point to run the application
│── gui.py               # Handles the graphical interface
│── stats.py             # Computes basic statistical calculations
│── plot.py              # Contains functions to plot different graphs
│── utils.py             # Utility functions like loading CSV
│── csv_generator.py     # Handles CSV generation from random data
│── requirements.txt     # Dependencies for the project
```

---

## **Requirements**

- **Python 3.7+**
- **Tkinter**: For GUI development.
- **Pandas**: For data manipulation and statistics calculations.
- **Matplotlib**: For plotting graphs.
- **CustomTkinter**: For an improved and beautiful UI.

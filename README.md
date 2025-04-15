# **Basic CSV Analyzer Tool**

A Python tool for analyzing and visualizing numerical data from CSV files. It allows users to upload CSV files, compute basic statistics (Mean, Median, Mode, Standard Deviation), and display the data with various graph types (e.g., Histogram, Box Plot). It also includes a CSV Generator feature that lets users create random CSV data based on selected columns and number of rows.

---

## **Features**

- **CSV Upload**: Load CSV files with numerical data.
- **Basic Statistics Calculation**: Compute and display mean, median, mode, standard deviation, and more.
- **Graph Visualization**: Display different types of graphs like histogram, box plot, scatter plot, etc.
- **CSV Generator**: Generate a new CSV with user-defined columns and random data.
- **Color Customization**: Choose the color for the charts.

---

## **Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AsoAfan/Basic-CSV-Analyzer-Tool.git
    cd Basic-CSV-Analyzer-Tool
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
Basic-CSV-Analyzer-Tool/
├── app/                      # Main application code
│   ├── gui.py                # GUI-related logic using CustomTkinter
│   ├── stats.py              # Statistical data processing (Mean, Mode, etc.)
│   ├── plot.py               # Graphing and plotting logic
│   ├── utils.py              # Utility functions used across the app
│   └── csv_generator.py      # CSV generation and random data functionality
├── data/                     # Data files (can store sample or user-uploaded CSVs)
│   └── simple_data.csv       # Sample CSV data file
├── main.py                   # Entry point to run the application
├── requirements.txt          # List of Python dependencies
├── .gitignore                # Git ignore file to exclude unnecessary files
└── Readme.md                 # Project documentation and instructions

```
---

## **Requirements**

- **Python 3.7+**
- **Tkinter**: For GUI development.
- **Pandas**: For data manipulation and statistics calculations.
- **Matplotlib**: For plotting graphs.
- **CustomTkinter**: For an improved and beautiful UI.

---

Sure! Here's a refined **Contribution** section for your README that includes a friendly note about the app not being error-free:

---

## **Contribution**

We welcome contributions to help make this project better!

While we've worked hard to build a functional and user-friendly app, it may **not be completely error-free**. If you come across any bugs or issues, or have ideas for improvements, your input is greatly appreciated!

### **How to Contribute**
1. **Fork** the repository  
2. **Clone** your fork locally:  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
3. Create a **new branch** for your changes:  
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes and commit with clear, concise messages  
5. **Push** your branch and open a **pull request**

### **Contribution Guidelines**
- Keep pull requests focused and descriptive
- Include screenshots or descriptions if you’re changing the UI
- Test your changes before submitting

### **Found a Bug or Have an Idea?**
- Open an issue to report a bug, suggest a feature, or ask a question
- Contributions big or small are all welcome!

---

Happy coding 🥰
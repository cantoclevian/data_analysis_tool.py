
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

class DataAnalysisTool:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.report_content = []

    def analyze_data(self):
        self.report_content.append("Data Analysis Report")
        self.report_content.append("====================\n")
        
        # Basic statistics
        self.report_content.append("Basic Statistics:\n")
        self.report_content.append(str(self.data.describe()))
        
        # Visualization of key metrics
        self.plot_data()

    def plot_data(self):
        # Example: Plotting the first two columns
        columns = self.data.columns[:2]
        self.data.plot(kind='bar', x=columns[0], y=columns[1])
        plt.title('Key Metrics Visualization')
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
        plt.savefig('visualization.png')
        plt.close()
        
        self.report_content.append("\n\nVisualization saved as 'visualization.png'.")

    def generate_report(self):
        # Generate PDF report
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        for line in self.report_content:
            pdf.multi_cell(0, 10, line)
        
        pdf.output("data_analysis_report.pdf")
        print("Report generated: data_analysis_report.pdf")

if __name__ == "__main__":
    # Example usage
    file_path = 'example_data.csv'  # Change this to your CSV file path
    tool = DataAnalysisTool(file_path)
    tool.analyze_data()
    tool.generate_report()

# 📊 Cloud SPSS Bypass: Local Statistical Analysis Engine

## 🎯 Architectural Objective
This project replaces cloud-based SPSS dependencies with locally orchestrated Python scripts to compute frequency distributions and descriptive statistics for Behavioral Statistics. By executing data analytics entirely on local hardware, this project eliminates the data privacy risks associated with routing internal data strings through unvetted, third-party educational cloud infrastructure.

## 🧱 The Zero-Trust Justification
Funneling datasets through external cloud instances solely to render histograms or frequency tables introduces unnecessary network exposure and violates strict data sovereignty hygiene. This script achieves **100% data privacy** via sandboxed local processing.

## ⚙️ Engineering Stack
*   **Language:** Python 3
*   **Libraries:** `pandas`, `numpy`, `matplotlib`

## 📊 Modeled Statistical Outputs ($N=40$)
*   **Mean ($M$):** `3.75`
*   **Median:** `4.00`
*   **Sample Variance ($s^2$):** `3.42`
*   **Sample Standard Deviation ($s$):** `1.85`

## 📈 Visualizations Rendered
The script automatically compiles SPSS-style frequency validation tables and outputs sharp distribution graphs locally using custom Matplotlib matrices (e.g., discrete categorical bar charts and sea-green ratio data histograms).


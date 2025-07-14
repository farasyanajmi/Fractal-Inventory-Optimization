# APPLICATION OF NON-LINEAR FUNCTIONS IN FRACTAL INTERPOLATION TECHNIQUES FOR OPTIMIZING FOOD PRODUCT INVENTORY
 
This thesis explores the application of **non-linear fractal interpolation functions** to predict commercial rice demand. It then utilizes a **fuzzy Economic Order Quantity (EOQ) model** to determine optimal order sizes, safety stock, and reorder points. The goal is to enhance inventory management for Perum BULOG Divre Sumsel and Babel by reducing operational costs and ensuring product availability.

---

## Key Contributions & Findings

* **Demand Prediction:** Successfully applied non-linear fractal interpolation for rice demand data, achieving a **MAPE of 6.57%**.
* **Inventory Optimization:** Determined an optimal order size of **20,275.67 tons/year**, safety stock of **1,123.51 tons**, and reorder point of **7,277.25 tons** using a fuzzy EOQ model.
* **Methodology:** Integrated fractal interpolation with fuzzy logic to address uncertainties in demand forecasting and inventory planning.

---

## Files in this Repository

* `module_fix_3.py`: Contains core functions for fractal interpolation calculations.
* `Interpolation.py`: The main script to run the fractal interpolation and fuzzy EOQ calculations.
* `requirements.txt`: Lists the Python dependencies required to run the code.
* `data/`: Directory for raw or processed datasets, if applicable
* `calculations/`: Directory for supplementary calculation files.

---

## Technologies Used

* **Python**
* **PyCharm**
* **Microsoft Excel**

---

## Installation

To set up the environment and run the code:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/farasyanajmi/Fractal-Inventory-Optimization
    ```
2.  **Install dependencies:** Ensure you have Python installed. Then, install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
    The required libraries are `numpy`, `matplotlib`, and `pandas`.

---

## How to Use

1.  **Prepare Data:** If your `Interpolation.py` script requires external data, ensure you have an Excel file in your `data/` directory or specify its path when prompted.
2.  **Run the Interpolation Script:** Execute the main script from your terminal:
    ```bash
    python Interpolation.py
    ```
    The script will output data, calculation results, and display a graph.
3.  **Examine supplementary files:** Review the Excel files in the `calculations/` directory using **Microsoft Excel** for detailed fuzzy EOQ computations.

---

## Acknowledgements

* I would like to point out that the predictions and analyses presented in this thesis are specifically based on data for **2021**.
* I welcome any **criticism or suggestions** that could be useful for future research or improvements to this work.

---

## Contact

For any inquiries, feedback, or further discussion regarding this thesis, please feel free to reach out to me.

---

## License

All Rights Reserved

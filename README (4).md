# Material Shortage Dashboard

A small tool that monitors inventory levels, flags materials that have fallen below their safety stock threshold, and alerts the responsible buyers.

## What it does

- Reads inventory data (material, current stock, safety stock, buyer) from an Excel file
- Identifies materials where current stock is below the safety stock level
- Displays everything in a Streamlit dashboard: total critical materials, full inventory, critical materials list, and a stock-level chart
- Sends automated email alerts to buyers for any material in shortage, on a daily schedule

## Project Structure

```
.
├── app.py            # Streamlit dashboard
├── project.py        # Shortage detection + scheduled email alerts
├── inventory.xlsx     # Source inventory data
└── README.md
```

## Data Format

`inventory.xlsx` expects these columns:

| Column          | Description                            |
|------------------|-----------------------------------------|
| `Material_ID`    | Unique identifier for the material      |
| `Material_Name`  | Name of the material                    |
| `Current_Stock`  | Current stock quantity                  |
| `Safety_Stock`   | Minimum safe stock threshold            |
| `Buyer_Email`    | Buyer responsible for the material      |
| `Planner_Email`  | Planner for the material (optional)     |

## Setup

```bash
pip install streamlit pandas schedule openpyxl
```

## Usage

**Run the dashboard:**

```bash
streamlit run app.py
```

**Run the shortage alert scheduler:**

```bash
python project.py
```

## Requirements

- Python 3.8+
- streamlit, pandas, schedule, openpyxl

## License

Add a license of your choice (MIT, Apache 2.0, etc.).

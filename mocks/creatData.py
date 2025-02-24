import pandas as pd
import random
from datetime import datetime, timedelta

def CreateFuelData(filename="fuel_data3.xlsx", num_rows=100):
    """Creates an Excel spreadsheet with random fuel-related data."""
    
        # List of random states (Modify this as needed)
    states = ["California", "Texas", "New York", "Florida", "Illinois", "Ohio", "Nevada", "Michigan", "Arizona", "Georgia"]
    
     # Generate random timestamps within a given range
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)

    timestamps = [start_date + timedelta(days=random.randint(0, 364), hours=random.randint(0, 23), minutes=random.randint(0, 59)) for _ in range(num_rows)]

    # Generate random data
    
    # Generate random data
    data = {
        "State": [random.choice(states) for _ in range(num_rows)],  # Assign a random state
        "Timestamp": timestamps,  # Randomized timestamps
        "Pressure (psi)": [round(random.uniform(200, 1000), 2) for _ in range(num_rows)],  # Fuel line pressure
        "Temperature (°F)": [round(random.uniform(-30, 70), 2) for _ in range(num_rows)],  # Fuel temperature
        "Flow Rate (L/min)": [round(random.uniform(10, 500), 2) for _ in range(num_rows)],  # Fuel movement inside tubes
        "Fuel Levels (%)": [round(random.uniform(0, 100), 2) for _ in range(num_rows)],  # Fuel storage tank levels
        "Fuel Density (kg/m³)": [round(random.uniform(700, 850), 2) for _ in range(num_rows)],  # Fuel density
        "Contaminants Presence (%)": [round(random.uniform(0, 5), 2) for _ in range(num_rows)],  # Impurities percentage
        "Pump Efficiency (%)": [round(random.uniform(50, 100), 2) for _ in range(num_rows)],  # Pump performance efficiency
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to Excel
    df.to_excel(filename, index=False)
    print(f"Excel file '{filename}' created successfully!")

# Run the function
CreateFuelData()

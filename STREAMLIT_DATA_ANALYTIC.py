import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
# Create the DataFrame
data = {
    'station': ['Aotizhongxin', 'Nongzhanguan', 'Guanyuan', 'Gucheng', 'Dongsi', 'Tiantan', 'Changping', 'Shunyi', 'Huairou', 'Dingling'],
    'NO2': [59.31, 58.10, 57.90, 55.88, 53.70, 53.16, 44.19, 43.91, 32.51, 27.59]
}
df = pd.DataFrame(data)

# Create the bar chart using matplotlib
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.bar(df['station'], df['NO2'], color='skyblue')
plt.xlabel('Station')
plt.ylabel('NO2 Concentration')
plt.title('Average NO2 Concentration at Different Stations')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
plt.tight_layout()

# Display the chart in Streamlit
st.pyplot()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
# Create the DataFrame
data = {
    'month': ["1", "2", "3", "12", "11", "4", "5", "10", "6", "9", "7", "8"],
    'SO2': [30.424496, 26.971881, 26.889141, 24.259698, 15.028278, 13.675225, 13.474855, 8.391005, 7.482812, 6.025976, 5.295546, 4.374445]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['month'], df['SO2'], color='black')
plt.xlabel('Month')
plt.ylabel('SO2 Concentration')
plt.title('Average SO2 Concentration at Different Month')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the chart in Streamlit
st.pyplot()






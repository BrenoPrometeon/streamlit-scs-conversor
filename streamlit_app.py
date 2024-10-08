import streamlit as st
import pandas as pd
import io
from PIL import Image

logo_path = "assets/logoWhite.png"
    
# Load local image
image = Image.open(logo_path)

# Show image in Streamlit
st.image(image, caption='Prometeon Type Group', use_column_width=True)

# Title and Description
st.title("SCS Converter")
st.write("Upload a CSV file and select an option to modify it:")

# Upload CSV file
uploaded = st.file_uploader("Select a file ", type="csv")

# Check if a file was uploaded
if uploaded is not None:
    # Reading user CSV file
    file_name =  uploaded.name
    file_data = io.BytesIO(uploaded.read())

    # Read CSV file and name the column
    df1 = pd.read_csv(file_data, names=['Column'], nrows = 3)
    
    # Capture the contents of the first column
    first_column = df1['Column']

    # Reset Buffer
    file_data.seek(0)
    
    # Read the CSV file
    df = pd.read_csv(file_data, skiprows=5, sep=';')
    
    # Select 8 columns
    df = df.iloc[:, :8]

    # Variables
    old_values_RP = ['L\'\'','P','Q','R','R\'','R\'\'','T','V','Y']
    old_values_RP_S = ['L\'\'','P','Q','R','R\'','R\'\'','T','V','Y','S']
    old_values_P = ['F\'\'\'','O']

    # Options to modify the file
    options = ["Yes", "No"]
    selected_option = st.selectbox('O pneu é bordo Avolgente?', options)

    # Modify the file based on the selected option
    if selected_option == "Yes":
        df.loc[df['Name'].isin(old_values_RP_S), 'Type'] = 'RP'
    elif selected_option == "No":
       df.loc[df['Name'].isin(old_values_RP), 'Type'] = 'RP'
    
    df.loc[df['Name'].isin(old_values_P), 'Type'] = 'P'

    # New file name
    new_file_name = file_name[:-4] + "_f" + file_name[-4:]

    # Create new file
    with io.StringIO() as f:
    # Write comments to new file
        for comment in first_column:
            f.write(comment)
            f.write('\n')
        f.write('\n\n')   

        new_lines = [
        ['LC', '', 0, '0,0', '0,0', 'mm', 'P', ''],
        ['BC1', '', 0, '0,0', '0,0', 'mm', 'P', ''],
        ['BC2', '', 0, '0,0', '0,0', 'mm', 'P', ''],
        ['R01', '', 0, '0,0', '0,0', 'mm', 'C', ''],
        ['R02', '', 0, '0,0', '0,0', 'mm', 'C', ''],
        ['R03', '', 0, '0,0', '0,0', 'mm', 'C', ''],
        ['R04', '', 0, '0,0', '0,0', 'mm', 'C', ''],
        ['R05', '', 0, '0,0', '0,0', 'mm', 'C', ''],
        ['R06', '', 0, '0,0', '0,0', 'mm', 'C', '']
        ]
        new_lines_df = pd.DataFrame(new_lines, columns=df.columns[:8])

        # Concatenar o DataFrame existente com as novas linhas
        df_atualizado = pd.concat([df, new_lines_df])

        # Write the dataframe to the new file
        df_atualizado.to_csv(f, index=False, sep=';')

        # Get the file content as a string
        f.seek(0)
        csv_content = f.read()

    # Option to download the modified CSV file 
    st.markdown("### Download the modified CSV file")
    st.download_button("Click here to download", data=csv_content, file_name=new_file_name)
else:
    st.warning('Please, upload a file!')

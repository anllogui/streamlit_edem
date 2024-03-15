conda create -n streamlit python=3.11
conda activate streamlit

activate autoreload:
mkdir .streamlit

config.toml --> runOnSave

conda install -c conda-forge pandas streamlit openpyxl python-duckdb plotly seaborn openai==0.28

prompt para chatgpt:
generame una aplicación de streamlit que cree un cuadro de mandos complejo a partir de un excel.

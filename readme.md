conda create -n streamlit-report python=3.11
conda activate streamlit-report

activate autoreload:
mkdir .streamlit
config.toml --> runOnSave

conda install -c conda-forge pandas streamlit openpyxl python-duckdb plotly openai==0.28

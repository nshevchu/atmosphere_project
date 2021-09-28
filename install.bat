set CURR_DIR=%CD%
set VENV=%CURR_DIR%\venv
set ACTIVATE=%VENV%\Scripts\activate.bat

IF EXIST "requirements.txt" (
  pip install -r requirements.txt
  ECHO file filename exists
) ELSE (
  ECHO file filename does not exist
)

pip install ipykernel
pip install jupyter

python -m ipykernel install --user --name=venv_atmosphere
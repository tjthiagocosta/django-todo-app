python -m venv venv
activate() {
  . venv/bin/activate
  echo "Instaling requirements to virtual environment"
  pip install -r requirements.txt
}
activate
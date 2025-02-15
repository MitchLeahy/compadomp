# Data Comparison Tool

A Streamlit application for comparing CSV and Excel files with support for multiple column comparisons and synthetic key generation.

## Features

- Upload and compare CSV or Excel files
- Select multiple columns for comparison
- Automatic synthetic key generation for multi-column comparisons
- Downloadable comparison reports
- Match score calculation
- Detailed difference analysis

## Local Development Setup

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

To run the application locally:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Azure Deployment

### Prerequisites

- Azure subscription
- Azure CLI installed and configured
- Git (for source control)

### Deployment Steps

1. Login to Azure:
```bash
az login
```

2. Navigate to the azure_template directory:
```bash
cd azure_template
```

3. Make the deployment script executable:
```bash
chmod +x deploy.sh
```

4. Run the deployment script:
```bash
./deploy.sh
```

This will:
- Create a new resource group (compadomp-Rg01)
- Deploy an App Service Plan
- Create and configure a Web App

### Configuration Details

The deployment uses:
- Region: East US 2
- App Service Plan: Free tier (F1)
- Python version: 3.12
- Custom startup command for Streamlit

### Post-Deployment

After deployment, you'll need to:

1. Set up deployment from your source code:
   - Configure GitHub Actions, or
   - Use Azure App Service's deployment center

2. Verify the application is running by visiting the deployed URL:
```
https://<app-name>.azurewebsites.net
```

Replace `<app-name>` with the name specified in `azuredeploy.parameters.json`

## Troubleshooting

### Local Development

- If you get a port conflict, you can specify a different port:
```bash
streamlit run app.py --server.port <port-number>
```

- For virtual environment issues, ensure you're activating the correct environment and all dependencies are installed.

### Azure Deployment

- If deployment fails with quota issues, try:
  - Using a different region
  - Requesting a quota increase
  - Using a different service tier

- For application startup issues:
  - Check the application logs in Azure Portal
  - Verify all dependencies are correctly listed in requirements.txt

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Specify your license here]

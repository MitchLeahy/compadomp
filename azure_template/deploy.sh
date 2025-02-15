#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Variables
RESOURCE_GROUP="compadomp-Rg01"
LOCATION="eastus2"
DEPLOYMENT_NAME="compadomp-deployment"

# Change to the script directory
cd "$SCRIPT_DIR"

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Deploy ARM template
az deployment group create \
  --name $DEPLOYMENT_NAME \
  --resource-group $RESOURCE_GROUP \
  --template-file azuredeploy.json \
  --parameters @azuredeploy.parameters.json 
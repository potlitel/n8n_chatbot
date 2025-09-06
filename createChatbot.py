from workflows_utils.CreateBasicWorkflow import CreateBasicWorkflow
from workflows_utils.ListExistingsWorkflows import ListExistingWorkflows

# Configura la URL de tu instancia de n8n
N8N_API_URL = 'http://localhost:5678'  # Cambia esto si tu n8n está en otra dirección
N8N_API_KEY  = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1ZmE5YWExZi0yNjhlLTQ4ZDUtYWZkNS1mMTJkMDJhNGNlMDAiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzU2OTMwMzA0fQ.1vLMcxBPfmld9q6Dm27egm8aHv0WmVr1D_yux6ydyVA'  # Reemplaza con tu token de API

# Configura los headers para la autenticación básica
headers = {
    'X-N8N-API-KEY': N8N_API_KEY,
    'Content-Type': 'application/json'
}


CreateBasicWorkflow(N8N_API_URL, headers)

ListExistingWorkflows(N8N_API_URL, headers)

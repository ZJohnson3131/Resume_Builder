#routers/health.py — First Endpoint (Python)
#
#Purpose: Minimal endpoint to verify the service is running.
#
#What to include:
#
#APIRouter instance
#
#One GET endpoint: /health
#
#Simple JSON response
#
#Pseudocode guidance:
#
#router = APIRouter()
#
#@router.get("/health")
#
#Function returns { "status": "ok" }
#
#This endpoint should:
#
#Have no dependencies
#
#Never fail under normal conditions
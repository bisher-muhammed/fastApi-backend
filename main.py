from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(
    title="3D Model API",
    description="API for retrieving 3D model metadata",
    version="1.0"
)

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Modify for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define response model
class ModelInfoResponse(BaseModel):
    model_name: str
    vertex_count: int
    texture_details: str

# API endpoint to fetch model metadata
@app.get("/python-model-info", response_model=ModelInfoResponse, 
         summary="Get 3D Model Metadata",
         description="Returns details about the 3D model.")
async def get_model_info():
    """
    Retrieve metadata about a 3D model.

    - **model_name**: Name of the 3D model
    - **vertex_count**: Number of vertices in the model
    - **texture_details**: Description of applied texture
    """
    return ModelInfoResponse(
        model_name="3D Model A",
        vertex_count=6000,
        texture_details="Diffuse map applied"
    )

# Custom OpenAPI Schema Function (Optional)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="3D Model API",
        version="1.0.0",
        description="API for retrieving 3D model metadata",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
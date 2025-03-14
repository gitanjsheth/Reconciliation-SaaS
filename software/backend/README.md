# Backend - Reconciliation SaaS

## Setup instructions

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate virtual environment:
    ```bash
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the development server:
    ```bash
    uvicorn app.main:app --reload
    ```

## Project Structure

```
backend/
├── app/
│   ├── api/        # API routes and endpoints
│   ├── core/       # Core functionality and config
│   ├── db/         # Database models and connection
│   ├── models/     # Pydantic models/schemas
│   ├── services/   # Business logic
│   └── utils/      # Utility functions
├── tests/          # Test files
├── scripts/        # Utility scripts
└── requirements.txt
```

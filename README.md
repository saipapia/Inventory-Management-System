# Inventory Management System

This Inventory Management System is built using FastAPI (Backend) and Streamlit (Frontend) with MySQL as the database. 

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/inventory_management.git
   cd inventory_management
   ```
2. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
    or
    PyCharm terminal:
    uvicorn main:app --reload
   ```
4. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
5. **Configure MySQL Database**:   
   ```Ensure MySQL is running and create a database:
      CREATE DATABASE inventory_db;
      Update database.py with your MySQL credentials.
   ```
6. **API Endpoints:**
   Method	Endpoint	Description
   GET	/api/products/	Get all products
   GET	/api/products/{id}	Get product by ID
   POST	/api/products/	Add a new product
   PUT	/api/products/{id}	Update product details
   DELETE /api/products/{id}	Delete a product

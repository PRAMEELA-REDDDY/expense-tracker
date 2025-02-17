# Expense Tracking System

This is an **Expense Tracking System** built with **FastAPI** for the backend API and **Streamlit** for the frontend application. The system allows users to:

- Track and update expenses for specific dates.
- Analyze expenses by category between specified dates.
- Analyze expenses by month for a given month.

## Features

### 1. **Add/Update Expenses**
   - Add or update expenses for a specific date.
   
### 2. **Analytics By Category**
   - View an analysis of expenses grouped by category between two specific dates.
   
### 3. **Analytics By Month**
   - View an analysis of expenses for a particular month.

## Project Structure

- **`db_helper.py`**: Contains code for interacting with the database (fetching and updating records).
- **`server.py`**: Handles the FastAPI server and API routes.
- **`app.py`**: Contains the Streamlit app code for the frontend interface.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- **FastAPI** and **Streamlit** libraries
- **Uvicorn** for running the FastAPI server

### Installing Dependencies

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker

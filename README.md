# Cafe Finder

A simple web application to list, add, and manage cafes.

## Features

- List all cafes with details like name, location, amenities, etc.
- Add a new cafe.
- Search functionality to find cafes by name.
- Pagination to navigate through multiple pages of cafe listings.
- Delete a cafe from the list.

## Setup and Installation

### Prerequisites

- Python 3.8 or newer
- pip
- virtualenv (optional)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/MariosAvraam/cafe-and-wifi-website.git
```

2. Go to the directory:
```bash
cd cafe-and-wifi-website
```


3. (Optional) Create a virtual environment:
```bash
virtualenv venv
source venv/bin/activate # On Windows, use 'venv\Scripts\activate'
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

5. Initialize the database:
```python
from app import db
db.create_all()

6. Run the application
python app.py

The application will start and should be accessible at http://127.0.0.1:5000/.

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing
The code in this project is licensed under the MIT license.


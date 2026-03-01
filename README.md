# Web Technologies - Lab 4: Django Templates+HTML 

**Name:** Ghaida Al-harbi  
**Lab Number:** 4  

## Summary of Work
This lab focused on mastering the **Django Template System**, implementing **Template Inheritance** for UI consistency. 

## Key Technical Tasks

### 1. Template Architecture & Inheritance
* **Base Template**: Created `base.html` to serve as a master layout, including reusable `header` and `footer` components.
* **Blocks Implementation**: Used `{% block content %}` to allow child templates to inject specific data while maintaining the global layout.
* **DRY Principle**: Applied the "Don't Repeat Yourself" principle by inheriting from the base template in `list_books.html`.

### 2. Static Files & Asset Management
* **Directory Structure**: Organized assets within `apps/blog/static/blog/`, keeping CSS and images separate and modular.
* **Static Tagging**: Used the `{% load static %}` tag to dynamically link CSS files and display book cover images.
* **Styling**: Applied custom CSS to enhance the visual presentation of the book list.

### 3. Git Workflow & Authentication (Security-Focused)
* **Identity Management**: Configured Git global settings with professional credentials `GhaidaIbrahim`.
* **Token-Based Auth**: Utilized **GitHub Personal Access Tokens (PAT)** for secure CLI operations, following modern security standards to overcome authentication barriers.
* **Deployment**: Successfully pushed 52 project objects to the `Lab4-Web-Technologies` repository using the Terminal.



## Personal Notes & Key Takeaways
* **Modular Design**: Learned how template inheritance significantly reduces code redundancy and makes UI updates easier.
* **Security Awareness**: Realized the importance of managing Git credentials and tokens carefully to protect repository integrity.
* **Specialist Insight**: As a CS specialist, I prioritized using the Terminal for all Git operations to gain deeper control over the versioning and deployment process.

## Lab Deliverables
* **Source Code**: Full Django project structure with templates and static folders.
* **Repository**: [GhaidaIbrahim/Lab4-Web-Technologies](https://github.com/GhaidaIbrahim/Lab4-Web-Technologies)

### 4. Quick Start Guide (Terminal) 
To run this project on my local machine, follow these steps in the terminal:
* **Navigate to the Project Root:** `cd ~/Desktop/CS471/bookproject`
* **Activate the Virtual Environment:** `source bin/activate`
* **Enter the Web Application Directory:** `cd bookwebsite`
* **Start the Development Server:** `python3 manage.py runserver`
* **Access the Application:** Open your browser and visit: `http://127.0.0.1:8000/list_books/`

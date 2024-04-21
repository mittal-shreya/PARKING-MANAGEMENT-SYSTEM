# Smart Parking Management System

## Overview

The Smart Parking Management System is an advanced, interactive web application designed to simplify the management of vehicle parking spaces in lots or garages. It employs two key Python frameworks: Streamlit for the frontend user interface and Flask for the backend server operations. The application is connected to a PostgreSQL database, ensuring robust data handling and persistence.

## Features

- **Real-Time Space Availability**: Users can view up-to-date parking space availability through a Streamlit-based UI that visualizes the parking lot's status.
  
- **Parking and Exit Logging**: The system allows for the parking of vehicles by assigning available spaces and logs the exit times to calculate parking durations.
  
- **Cost Calculation**: On vehicle exit, the system calculates the total cost based on the duration of the stay and the vehicle type, with considerations for hourly rate pricing.
  
- **Vehicle Tracking**: The application facilitates the tracking of vehicles, including entry and exit times and the total cost associated with their parking.
  
- **Intuitive User Interface**: Streamlit provides an easy-to-use interface that allows operators to park and remove vehicles, view parking space statuses, and retrieve vehicle information with ease.
  
- **Database Backed**: PostgreSQL database ensures that all vehicle, parking space, and cost data are securely stored and easily accessible.
  
- **Scalability**: The architecture of the system is designed to be scalable to accommodate future enhancements, such as reservation systems, automated billing, and more.

## Technical Stack

### Backend:

- **Flask**: Serves as the web server framework to render templates and handle server-side logic.
  
- **PostgreSQL**: Used as the application's relational database to store parking space details, vehicle information, and types.

- **SQLAlchemy**: The ORM used in conjunction with Flask for database handling, simplifying the code for database operations.
  
### Frontend:

- **Streamlit**: Empowers the creation of the frontend user interface to interact with the backend, providing an engaging and responsive user experience.
  
- **HTML/CSS**: Utilized for custom template design rendered through Flask, enabling the display of parking space grids and vehicle data.

### Deployment:

- **Heroku**, **AWS Elastic Beanstalk**, or any other cloud service provider could be considered for deploying this application for real-world usage.

## Getting Started

Before you can run the application, ensure you have Python installed on your system, along with the necessary libraries: Flask, Streamlit, psycopg2, pandas, and SQLAlchemy. You will also need to set up a PostgreSQL database, ensuring it is accessible to the application.

To run the application, navigate to the project directory and execute:

For the Flask server:

```sh
python app.py
```

For the Streamlit interface:

```sh
streamlit run main.py
```


## Future Enhancements

Looking ahead, the system could be improved with features like:

- **Online Reservations**: Allowing users to reserve parking spaces in advance through the app.
  
- **Payment Integration**: Adding support for payment gateway integration to facilitate online payments.

- **License Plate Recognition**: Implementing license plate recognition can automate vehicle identification and further streamline the parking process.

- **Analytics Dashboard**: Providing administrators with insights into parking lot utilization rates, peak hours, and financial reports.
  
- **User Account Management**: Implementing account management for regular customers to store vehicle information and offer targeted discounts or services.


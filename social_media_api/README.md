SOCIAL MEDIA API
PHASE 1 – AUTHENTICATION FOUNDATION

INTRODUCTION

The Social Media API is a backend application built using Django and Django REST Framework.
The goal of this phase is to set up the project environment and implement user authentication features that will serve as the foundation for a full social media platform.

This phase focuses on user registration, login, token-based authentication, and basic profile management.

TECHNOLOGIES USED

The following technologies were used in building this project:

• Python
• Django
• Django REST Framework
• Token Authentication
• SQLite database (default)

PROJECT SETUP

A new Django project named “social_media_api” was created.
An application called “accounts” was added to handle all user-related functionality.

The Django REST Framework and token authentication system were configured to support API development.

USER AUTHENTICATION SYSTEM

A custom user model was created by extending Django’s AbstractUser class.
Additional fields were added to support social media functionality, including:

• Bio – short description about the user
• Profile picture – optional image field
• Followers – a many-to-many relationship that allows users to follow one another

Token-based authentication was implemented to secure API requests.
A token is generated automatically when a user registers or logs in.

API ENDPOINTS

The following endpoints were implemented in this phase:

User Registration
Endpoint: /api/accounts/register/
Method: POST
Purpose: Creates a new user account and returns an authentication token.

User Login
Endpoint: /api/accounts/login/
Method: POST
Purpose: Authenticates a user and returns an authentication token.

User Profile
Endpoint: /api/accounts/profile/
Method: GET
Purpose: Retrieves the authenticated user’s profile information.

TESTING

The Django development server was started to confirm that the project setup was successful.

API endpoints were tested using tools such as Postman to verify:
• Successful user registration
• Successful login
• Token generation
• Authorized access to protected endpoints

PROJECT STRUCTURE OVERVIEW

The project is structured into two main parts:

• The main Django project (social_media_api) containing configuration files
• The accounts app containing models, serializers, views, and URLs related to users

This structure allows for easy scalability as more features are added.

FUTURE IMPROVEMENTS

Planned future features include:

• Creating posts
• Following and unfollowing users
• Likes and comments
• User feeds
• Pagination and filtering
• Media uploads

CONCLUSION

This phase successfully establishes the foundation for a Social Media API.
The project environment is fully configured, user authentication is functional, and the system is ready for future expansion into full social media features.
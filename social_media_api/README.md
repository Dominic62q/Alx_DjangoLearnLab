SOCIAL MEDIA API
PROJECT DOCUMENTATION

INTRODUCTION

The Social Media API is a backend application built using Django and Django REST Framework.
The purpose of this project is to create a scalable API that supports user authentication and core social media features such as posting content and commenting on posts.

The project is developed in phases to ensure a strong and secure foundation.

TECHNOLOGIES USED

The following technologies were used:

• Python
• Django
• Django REST Framework
• Token-based Authentication
• SQLite Database

PROJECT OVERVIEW

The Social Media API consists of two main functional phases:

• Phase 1: User Authentication and Profile Management
• Phase 2: Posts and Comments Functionality

Each phase builds on the previous one to expand the platform’s capabilities.

USER AUTHENTICATION AND PROFILE MANAGEMENT (PHASE 1)

This phase focuses on setting up user management and authentication.

Key features implemented:

• Custom user model extending Django’s AbstractUser
• Additional user fields such as bio, profile picture, and followers
• Token-based authentication for secure API access
• User registration and login functionality
• Authenticated user profile retrieval

User authentication ensures that only verified users can access protected API endpoints.

AUTHENTICATION ENDPOINTS

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
Purpose: Retrieves profile details of the authenticated user.

POSTS FUNCTIONALITY (PHASE 2)

Posts allow users to share content on the platform.

Each post contains:
• Author
• Title
• Content
• Date created
• Date updated

Authenticated users can:
• Create posts
• View posts
• Edit their own posts
• Delete their own posts

COMMENTS FUNCTIONALITY (PHASE 2)

Comments allow users to engage with posts created by other users.

Each comment contains:
• Related post
• Author
• Content
• Date created
• Date updated

Authenticated users can:
• Add comments to posts
• View comments
• Edit their own comments
• Delete their own comments

POSTS AND COMMENTS ENDPOINTS

Posts
Endpoint: /api/posts/
Methods: GET, POST

Single Post
Endpoint: /api/posts/{id}/
Methods: PUT, DELETE

Comments
Endpoint: /api/comments/
Methods: GET, POST

Single Comment
Endpoint: /api/comments/{id}/
Methods: PUT, DELETE

AUTHENTICATION AND PERMISSIONS

Token-based authentication is required for all protected endpoints.

Permission rules include:
• Only authenticated users can create posts and comments
• Users can only update or delete content they own
• All users can view posts and comments

These rules ensure secure and fair usage of the platform.

PAGINATION AND SEARCH

Pagination is implemented to limit the number of posts and comments returned per request.

Search functionality allows users to filter posts using keywords found in the post title or content.

TESTING AND VALIDATION

The API was tested using Postman to ensure:

• Successful user registration and login
• Token generation and authentication
• Proper creation and management of posts and comments
• Correct enforcement of permissions
• Pagination and search functionality working as expected

CONCLUSION

This project successfully implements the core backend functionality required for a social media platform. The API supports secure user authentication, content creation through posts, and user interaction through comments. The system is designed to be scalable and ready for future enhancements.
# LibraryProject
This is a Django web application for managing library books, users, and borrowing records.

# Custom User Model + Permissions

- Custom user model created in accounts.models.CustomUser
- Custom permissions added to Article model:
  - can_view
  - can_create
  - can_edit
  - can_delete
- Groups created in admin with matching permissions
- Views protected using @permission_required
- All user references use AUTH_USER_MODEL

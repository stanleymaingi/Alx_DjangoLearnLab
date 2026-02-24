# Permissions and Groups Setup

Custom permissions added to Book model:
- can_view
- can_create
- can_edit
- can_delete

Groups created:
- Editors: can_view, can_create, can_edit
- Viewers: can_view
- Admins: all permissions

Views are protected using Django's @permission_required decorator.

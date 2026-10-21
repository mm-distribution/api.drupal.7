# modules/user/user.module

- **Source:** [local](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · 4172 lines
- **Module/theme:** user

## File documentation

```text
@file
Enables the user registration and login system.
```

## Functions (derived index)

- [user_help()](user_help.md) — Implements hook_help().
- [user_module_invoke()](user_module_invoke.md) — Invokes a user hook in every module.
- [user_theme()](user_theme.md) — Implements hook_theme().
- [user_entity_info()](user_entity_info.md) — Implements hook_entity_info().
- [user_uri()](user_uri.md) — Implements callback_entity_info_uri().
- [user_field_info_alter()](user_field_info_alter.md) — Implements hook_field_info_alter().
- [user_field_extra_fields()](user_field_extra_fields.md) — Implements hook_field_extra_fields().
- [user_external_load()](user_external_load.md) — Fetches a user object based on an external authentication source.
- [user_load_multiple()](user_load_multiple.md) — Load multiple users based on certain conditions.
- [user_load()](user_load.md) — Loads a user object.
- [user_load_by_mail()](user_load_by_mail.md) — Fetch a user object by email address.
- [user_load_by_name()](user_load_by_name.md) — Fetch a user object by account name.
- [user_save()](user_save.md) — Save changes to a user account or add a new user.
- [user_validate_name()](user_validate_name.md) — Verify the syntax of the given name.
- [user_validate_mail()](user_validate_mail.md) — Validates a user's email address.
- [user_validate_picture()](user_validate_picture.md) — Validates an image uploaded by a user.
- [user_password()](user_password.md) — Generate a random alphanumeric password.
- [user_role_permissions()](user_role_permissions.md) — Determine the permissions for one or more roles.
- [user_access()](user_access.md) — Determine whether the user has a given privilege.
- [user_is_blocked()](user_is_blocked.md) — Checks for usernames blocked by user administration.
- [user_has_role()](user_has_role.md) — Checks if a user has a role.
- [user_permission()](user_permission.md) — Implements hook_permission().
- [user_file_download()](user_file_download.md) — Implements hook_file_download().
- [user_file_move()](user_file_move.md) — Implements hook_file_move().
- [user_file_delete()](user_file_delete.md) — Implements hook_file_delete().
- [user_search_info()](user_search_info.md) — Implements hook_search_info().
- [user_search_access()](user_search_access.md) — Implements hook_search_access().
- [user_search_execute()](user_search_execute.md) — Implements hook_search_execute().
- [user_element_info()](user_element_info.md) — Implements hook_element_info().
- [user_user_view()](user_user_view.md) — Implements hook_user_view().
- [user_account_form()](user_account_form.md) — Helper function to add default user account fields to user registration and edit form.
- [user_validate_current_pass()](user_validate_current_pass.md) — Form validation handler for the current password on the user_account_form().
- [user_account_form_validate()](user_account_form_validate.md) — Form validation handler for user_account_form().
- [user_user_presave()](user_user_presave.md) — Implements hook_user_presave().
- [user_user_categories()](user_user_categories.md) — Implements hook_user_categories().
- [user_login_block()](user_login_block.md)
- [user_block_info()](user_block_info.md) — Implements hook_block_info().
- [user_block_configure()](user_block_configure.md) — Implements hook_block_configure().
- [user_block_save()](user_block_save.md) — Implements hook_block_save().
- [user_block_view()](user_block_view.md) — Implements hook_block_view().
- [template_preprocess_user_picture()](template_preprocess_user_picture.md) — Process variables for user-picture.tpl.php.
- [theme_user_list()](theme_user_list.md) — Returns HTML for a list of users.
- [user_is_anonymous()](user_is_anonymous.md) — Determines if the current user is anonymous.
- [user_is_logged_in()](user_is_logged_in.md) — Determines if the current user is logged in.
- [user_register_access()](user_register_access.md) — Determines if the current user has access to the user registration page.
- [user_view_access()](user_view_access.md) — User view access callback.
- [user_edit_access()](user_edit_access.md) — Access callback for user account editing.
- [user_cancel_access()](user_cancel_access.md) — Menu access callback; limit access to account cancellation pages.
- [user_menu()](user_menu.md) — Implements hook_menu().
- [user_menu_site_status_alter()](user_menu_site_status_alter.md) — Implements hook_menu_site_status_alter().
- [user_menu_link_alter()](user_menu_link_alter.md) — Implements hook_menu_link_alter().
- [user_translated_menu_link_alter()](user_translated_menu_link_alter.md) — Implements hook_translated_menu_link_alter().
- [user_admin_paths()](user_admin_paths.md) — Implements hook_admin_paths().
- [user_uid_only_optional_to_arg()](user_uid_only_optional_to_arg.md) — Returns $arg or the user ID of the current user if $arg is '%' or empty.
- [user_uid_optional_load()](user_uid_optional_load.md) — Load either a specified or the current user account.
- [user_category_load()](user_category_load.md) — Return a user object after checking if any profile category in the path exists.
- [user_uid_optional_to_arg()](user_uid_optional_to_arg.md) — Returns $arg or the user ID of the current user if $arg is '%' or empty.
- [user_menu_title()](user_menu_title.md) — Menu item title callback for the 'user' path.
- [user_page_title()](user_page_title.md) — Menu item title callback - use the user name.
- [user_get_authmaps()](user_get_authmaps.md) — Discover which external authentication module(s) authenticated a username.
- [user_set_authmaps()](user_set_authmaps.md) — Save mappings of which external authentication module(s) authenticated a user. Maps external usernames to user ids in the users table.
- [user_login()](user_login.md) — Form builder; the main user login form.
- [user_login_default_validators()](user_login_default_validators.md) — Set up a series for validators which check for blocked users, then authenticate against local database, then return an error if authentication fails. Distributed authentication modules are welcome to use hook_form_alter() to change this series in order to authenticate against their user database instead of the local users table. If a distributed authentication module is successful, it should set $form_state['uid'] to a user ID.
- [user_login_name_validate()](user_login_name_validate.md) — A FAPI validate handler. Sets an error if supplied username has been blocked.
- [user_login_authenticate_validate()](user_login_authenticate_validate.md) — A validate handler on the login form. Check supplied username/password against local users table. If successful, $form_state['uid'] is set to the matching user ID.
- [user_login_final_validate()](user_login_final_validate.md) — The final validation handler on the login form.
- [user_user_flood_control()](user_user_flood_control.md) — Implements hook_user_flood_control().
- [user_authenticate()](user_authenticate.md) — Try to validate the user's login credentials locally.
- [user_login_finalize()](user_login_finalize.md) — Finalize the login process. Must be called when logging in a user.
- [user_login_submit()](user_login_submit.md) — Submit handler for the login form. Load $user object and perform standard login tasks. The user is then redirected to the My Account page. Setting the destination in the query string overrides the redirect.
- [user_external_login_register()](user_external_login_register.md) — Helper function for authentication modules. Either logs in or registers the current user, based on username. Either way, the global $user object is populated and login tasks are performed.
- [user_pass_reset_url()](user_pass_reset_url.md) — Generates a unique URL for a user to login and reset their password.
- [user_cancel_url()](user_cancel_url.md) — Generates a URL to confirm an account cancellation request.
- [user_pass_rehash()](user_pass_rehash.md) — Creates a unique hash value for use in time-dependent per-user URLs.
- [user_cancel()](user_cancel.md) — Cancel a user account.
- [_user_cancel()](_user_cancel.md) — Implements callback_batch_operation().
- [_user_cancel_session_regenerate()](_user_cancel_session_regenerate.md) — Implements callback_batch_finished().
- [user_delete()](user_delete.md) — Delete a user.
- [user_delete_multiple()](user_delete_multiple.md) — Delete multiple user accounts.
- [user_view_page()](user_view_page.md) — Page callback wrapper for user_view().
- [user_view()](user_view.md) — Generate an array for rendering the given user.
- [user_build_content()](user_build_content.md) — Builds a structured array representing the profile content.
- [user_mail()](user_mail.md) — Implements hook_mail().
- [_user_mail_text()](_user_mail_text.md) — Returns a mail string for a variable name.
- [user_mail_tokens()](user_mail_tokens.md) — Token callback to add unsafe tokens for user mails.
- [user_roles()](user_roles.md) — Retrieve an array of roles matching specified conditions.
- [user_role_load()](user_role_load.md) — Fetches a user role by role ID.
- [user_role_load_by_name()](user_role_load_by_name.md) — Fetches a user role by role name.
- [user_role_save()](user_role_save.md) — Save a user role to the database.
- [user_role_delete()](user_role_delete.md) — Delete a user role from database.
- [user_role_edit_access()](user_role_edit_access.md) — Menu access callback for user role editing.
- [user_permission_get_modules()](user_permission_get_modules.md) — Determine the modules that permissions belong to.
- [user_role_change_permissions()](user_role_change_permissions.md) — Change permissions for a user role.
- [user_role_grant_permissions()](user_role_grant_permissions.md) — Grant permissions to a user role.
- [user_role_revoke_permissions()](user_role_revoke_permissions.md) — Revoke permissions from a user role.
- [user_user_operations()](user_user_operations.md) — Implements hook_user_operations().
- [user_user_operations_unblock()](user_user_operations_unblock.md) — Callback function for admin mass unblocking users.
- [user_user_operations_block()](user_user_operations_block.md) — Callback function for admin mass blocking users.
- [user_multiple_role_edit()](user_multiple_role_edit.md) — Callback function for admin mass adding/deleting a user role.
- [user_multiple_cancel_confirm()](user_multiple_cancel_confirm.md)
- [user_multiple_cancel_confirm_submit()](user_multiple_cancel_confirm_submit.md) — Submit handler for mass-account cancellation form.
- [_user_categories()](_user_categories.md) — Retrieve a list of all user setting/information categories and sort them by weight.
- [_user_sort()](_user_sort.md)
- [user_filters()](user_filters.md) — List user administration filters that can be applied.
- [user_build_filter_query()](user_build_filter_query.md) — Extends a query object for user administration filters based on session.
- [user_comment_view()](user_comment_view.md) — Implements hook_comment_view().
- [theme_user_signature()](theme_user_signature.md) — Returns HTML for a user signature.
- [user_preferred_language()](user_preferred_language.md) — Get the language object preferred by the user. This user preference can be set on the user account editing page, and is only available if there are more than one languages enabled on the site. If the user did not choose a preferred language, or is the anonymous user, the $default value, or if it is not set, the site default language will be returned.
- [_user_mail_notify()](_user_mail_notify.md) — Conditionally create and send a notification email when a certain operation happens on the given user account.
- [user_form_process_password_confirm()](user_form_process_password_confirm.md) — Form element process handler for client-side password validation.
- [user_node_load()](user_node_load.md) — Implements hook_node_load().
- [user_image_style_delete()](user_image_style_delete.md) — Implements hook_image_style_delete().
- [user_image_style_save()](user_image_style_save.md) — Implements hook_image_style_save().
- [user_action_info()](user_action_info.md) — Implements hook_action_info().
- [user_block_user_action()](user_block_user_action.md) — Blocks a specific user or the current user, if one is not specified.
- [user_unblock_user_action()](user_unblock_user_action.md) — Unblocks a specific user or the current user, if one is not specified.
- [user_form_field_ui_field_edit_form_alter()](user_form_field_ui_field_edit_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [user_form_field_ui_field_edit_form_submit()](user_form_field_ui_field_edit_form_submit.md) — Additional submit handler for the 'Edit field instance' form.
- [user_register_form()](user_register_form.md) — Form builder; the user registration form.
- [user_register_validate()](user_register_validate.md) — Validation function for the user registration form.
- [user_register_submit()](user_register_submit.md) — Submit handler for the user registration form.
- [user_modules_installed()](user_modules_installed.md) — Implements hook_modules_installed().
- [user_modules_uninstalled()](user_modules_uninstalled.md) — Implements hook_modules_uninstalled().
- [user_login_destination()](user_login_destination.md) — Helper function to rewrite the destination to avoid redirecting to login page after login.
- [user_cookie_save()](user_cookie_save.md) — Saves visitor information as a cookie so it can be reused.
- [user_cookie_delete()](user_cookie_delete.md) — Delete a visitor information cookie.
- [user_rdf_mapping()](user_rdf_mapping.md) — Implements hook_rdf_mapping().
- [user_file_download_access()](user_file_download_access.md) — Implements hook_file_download_access().
- [user_system_info_alter()](user_system_info_alter.md) — Implements hook_system_info_alter().

## Classes and interfaces (derived index)

- [UserController](UserController.md) — Controller class for users.

## Constants

### USERNAME_MAX_LENGTH

- Line 11

```php
define('USERNAME_MAX_LENGTH', 60);
```

```text
Maximum length of username text field.
```

### EMAIL_MAX_LENGTH

- Line 16

```php
define('EMAIL_MAX_LENGTH', 254);
```

```text
Maximum length of user e-mail text field.
```

### USER_REGISTER_ADMINISTRATORS_ONLY

- Line 21

```php
define('USER_REGISTER_ADMINISTRATORS_ONLY', 0);
```

```text
Only administrators can create user accounts.
```

### USER_REGISTER_VISITORS

- Line 26

```php
define('USER_REGISTER_VISITORS', 1);
```

```text
Visitors can create their own accounts.
```

### USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL

- Line 32

```php
define('USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL', 2);
```

```text
Visitors can create accounts, but they don't become active without
administrative approval.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

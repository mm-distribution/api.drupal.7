# modules/profile/profile.module

- **Source:** [local](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · 631 lines
- **Module/theme:** profile

## File documentation

```text
@file
Support for configurable user profiles.
```

## Functions (derived index)

- [profile_help()](profile_help.md) — Implements hook_help().
- [profile_theme()](profile_theme.md) — Implements hook_theme().
- [profile_menu()](profile_menu.md) — Implements hook_menu().
- [profile_block_info()](profile_block_info.md) — Implements hook_block_info().
- [profile_block_configure()](profile_block_configure.md) — Implements hook_block_configure().
- [profile_block_save()](profile_block_save.md) — Implements hook_block_save().
- [profile_block_view()](profile_block_view.md) — Implements hook_block_view().
- [profile_user_presave()](profile_user_presave.md) — Implements hook_user_presave().
- [profile_user_insert()](profile_user_insert.md) — Implements hook_user_insert().
- [profile_user_cancel()](profile_user_cancel.md) — Implements hook_user_cancel().
- [profile_user_delete()](profile_user_delete.md) — Implements hook_user_delete().
- [profile_user_load()](profile_user_load.md) — Implements hook_user_load().
- [profile_save_profile()](profile_save_profile.md)
- [profile_view_field()](profile_view_field.md)
- [profile_user_view()](profile_user_view.md) — Implements hook_user_view().
- [_profile_form_explanation()](_profile_form_explanation.md)
- [profile_form_alter()](profile_form_alter.md) — Implements hook_form_alter().
- [_profile_update_user_fields()](_profile_update_user_fields.md) — Helper function: update an array of user fields by calling profile_view_field
- [profile_user_form_validate()](profile_user_form_validate.md) — Form validation handler for the user register/profile form.
- [profile_user_categories()](profile_user_categories.md) — Implements hook_user_categories().
- [profile_category_access()](profile_category_access.md) — Menu item access callback - check if a user has access to a profile category.
- [template_preprocess_profile_block()](template_preprocess_profile_block.md) — Process variables for profile-block.tpl.php.
- [template_preprocess_profile_listing()](template_preprocess_profile_listing.md) — Process variables for profile-listing.tpl.php.
- [template_preprocess_profile_wrapper()](template_preprocess_profile_wrapper.md) — Process variables for profile-wrapper.tpl.php.
- [_profile_field_types()](_profile_field_types.md)
- [_profile_field_serialize()](_profile_field_serialize.md)
- [_profile_get_fields()](_profile_get_fields.md)

## Constants

### PROFILE_PRIVATE

- Line 11

```php
define('PROFILE_PRIVATE', 1);
```

```text
Private field, content only available to privileged users.
```

### PROFILE_PUBLIC

- Line 16

```php
define('PROFILE_PUBLIC', 2);
```

```text
Public field, content shown on profile page but not used on member list pages.
```

### PROFILE_PUBLIC_LISTINGS

- Line 21

```php
define('PROFILE_PUBLIC_LISTINGS', 3);
```

```text
Public field, content shown on profile page and on member list pages.
```

### PROFILE_HIDDEN

- Line 26

```php
define('PROFILE_HIDDEN', 4);
```

```text
Hidden profile field, only accessible by administrators, modules and themes.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

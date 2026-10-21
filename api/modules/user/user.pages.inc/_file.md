# modules/user/user.pages.inc

- **Source:** [local](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · 708 lines
- **Module/theme:** user

## File documentation

```text
@file
User page callback file for the user module.
```

## Functions (derived index)

- [user_autocomplete()](user_autocomplete.md) — Menu callback; Retrieve a JSON object containing autocomplete suggestions for existing users.
- [user_pass()](user_pass.md) — Form builder; Request a password reset.
- [user_pass_validate()](user_pass_validate.md) — Form validation handler for user_pass().
- [user_pass_submit()](user_pass_submit.md) — Form submission handler for user_pass().
- [user_pass_reset()](user_pass_reset.md) — Menu callback; process one time login link and redirects to the user page on success.
- [user_logout()](user_logout.md) — Menu callback; logs the current user out, and redirects to the home page.
- [user_logout_current_user()](user_logout_current_user.md) — Logs the current user out.
- [template_preprocess_user_profile()](template_preprocess_user_profile.md) — Process variables for user-profile.tpl.php.
- [template_preprocess_user_profile_item()](template_preprocess_user_profile_item.md) — Process variables for user-profile-item.tpl.php.
- [template_preprocess_user_profile_category()](template_preprocess_user_profile_category.md) — Process variables for user-profile-category.tpl.php.
- [user_profile_form()](user_profile_form.md) — Form builder; edit a user account or one of their profile categories.
- [user_profile_form_validate()](user_profile_form_validate.md) — Form validation handler for user_profile_form().
- [user_profile_form_submit()](user_profile_form_submit.md) — Form submission handler for user_profile_form().
- [user_edit_cancel_submit()](user_edit_cancel_submit.md) — Submit function for the 'Cancel account' button on the user edit form.
- [user_cancel_confirm_form()](user_cancel_confirm_form.md) — Form builder; confirm form for cancelling user account.
- [user_cancel_confirm_form_submit()](user_cancel_confirm_form_submit.md) — Submit handler for the account cancellation confirm form.
- [user_cancel_methods()](user_cancel_methods.md) — Helper function to return available account cancellation methods.
- [user_cancel_confirm()](user_cancel_confirm.md) — Menu callback; Cancel a user account via e-mail confirmation link.
- [user_page()](user_page.md) — Page callback: Displays the user page.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

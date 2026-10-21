# hook_form_FORM_ID_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1708–1719 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1708-L1719)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_form_FORM_ID_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Provide a form-specific alteration instead of the global hook_form_alter().

Modules can implement hook_form_FORM_ID_alter() to modify a specific form,
rather than implementing hook_form_alter() and checking the form ID, or
using long switch statements to alter multiple forms.

Form alter hooks are called in the following order: hook_form_alter(),
hook_form_BASE_FORM_ID_alter(), hook_form_FORM_ID_alter(). See
hook_form_alter() for more details.

@param $form
  Nested array of form elements that comprise the form.
@param $form_state
  A keyed array containing the current state of the form. The arguments
  that drupal_get_form() was originally called with are available in the
  array $form_state['build_info']['args'].
@param $form_id
  String representing the name of the form itself. Typically this is the
  name of the function that generated the form.

@see hook_form_alter()
@see hook_form_BASE_FORM_ID_alter()
@see drupal_prepare_form()
@see forms_api_reference.html
```

## Code

```php
function hook_form_FORM_ID_alter(&$form, &$form_state, $form_id) {
  // Modification for the form with the given form ID goes here. For example, if
  // FORM_ID is "user_register_form" this code would run only on the user
  // registration form.

  // Add a checkbox to registration form about agreeing to terms of use.
  $form['terms_of_use'] = array(
    '#type' => 'checkbox',
    '#title' => t("I agree with the website's terms and conditions."),
    '#required' => TRUE,
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_form_FORM_ID_alter()".

- [block_form_form_test_alter_form_alter()](../../simpletest/tests/form_test.module/block_form_form_test_alter_form_alter.md) — `modules/simpletest/tests/form_test.module`
- [form_test_form_form_test_alter_form_alter()](../../simpletest/tests/form_test.module/form_test_form_form_test_alter_form_alter.md) — `modules/simpletest/tests/form_test.module`
- [form_test_form_form_test_state_persist_alter()](../../simpletest/tests/form_test.module/form_test_form_form_test_state_persist_alter.md) — `modules/simpletest/tests/form_test.module`
- [form_test_form_user_register_form_alter()](../../simpletest/tests/form_test.module/form_test_form_user_register_form_alter.md) — `modules/simpletest/tests/form_test.module`
- [session_test_form_user_login_alter()](../../simpletest/tests/session_test.module/session_test_form_user_login_alter.md) — `modules/simpletest/tests/session_test.module`
- [system_form_form_test_alter_form_alter()](../../simpletest/tests/form_test.module/system_form_form_test_alter_form_alter.md) — `modules/simpletest/tests/form_test.module`
- [block_form_system_performance_settings_alter()](../../block/block.module/block_form_system_performance_settings_alter.md) — `modules/block/block.module`
- [block_form_user_profile_form_alter()](../../block/block.module/block_form_user_profile_form_alter.md) — `modules/block/block.module`
- [book_form_node_delete_confirm_alter()](../../book/book.module/book_form_node_delete_confirm_alter.md) — `modules/book/book.module`
- [color_form_system_theme_settings_alter()](../../color/color.module/color_form_system_theme_settings_alter.md) — `modules/color/color.module`
- [color_form_system_themes_alter()](../../color/color.module/color_form_system_themes_alter.md) — `modules/color/color.module`
- [comment_form_node_type_form_alter()](../../comment/comment.module/comment_form_node_type_form_alter.md) — `modules/comment/comment.module`
- [contact_form_user_admin_settings_alter()](../../contact/contact.module/contact_form_user_admin_settings_alter.md) — `modules/contact/contact.module`
- [contact_form_user_profile_form_alter()](../../contact/contact.module/contact_form_user_profile_form_alter.md) — `modules/contact/contact.module`
- [dashboard_form_block_add_block_form_alter()](../../dashboard/dashboard.module/dashboard_form_block_add_block_form_alter.md) — `modules/dashboard/dashboard.module`
- [dashboard_form_block_admin_configure_alter()](../../dashboard/dashboard.module/dashboard_form_block_admin_configure_alter.md) — `modules/dashboard/dashboard.module`
- [dashboard_form_block_admin_display_form_alter()](../../dashboard/dashboard.module/dashboard_form_block_admin_display_form_alter.md) — `modules/dashboard/dashboard.module`
- [dashboard_form_dashboard_admin_display_form_alter()](../../dashboard/dashboard.module/dashboard_form_dashboard_admin_display_form_alter.md) — `modules/dashboard/dashboard.module`
- [dblog_form_system_logging_settings_alter()](../../dblog/dblog.module/dblog_form_system_logging_settings_alter.md) — `modules/dblog/dblog.module`
- [field_ui_form_node_type_form_alter()](../../field_ui/field_ui.module/field_ui_form_node_type_form_alter.md) — `modules/field_ui/field_ui.module`
- [forum_form_taxonomy_form_term_alter()](../../forum/forum.module/forum_form_taxonomy_form_term_alter.md) — `modules/forum/forum.module`
- [forum_form_taxonomy_form_vocabulary_alter()](../../forum/forum.module/forum_form_taxonomy_form_vocabulary_alter.md) — `modules/forum/forum.module`
- [garland_form_system_theme_settings_alter()](../../../themes/garland/theme-settings.php/garland_form_system_theme_settings_alter.md) — `themes/garland/theme-settings.php`
- [image_form_system_file_system_settings_alter()](../../image/image.module/image_form_system_file_system_settings_alter.md) — `modules/image/image.module`
- [locale_form_comment_form_alter()](../../locale/locale.module/locale_form_comment_form_alter.md) — `modules/locale/locale.module`
- [locale_form_node_type_form_alter()](../../locale/locale.module/locale_form_node_type_form_alter.md) — `modules/locale/locale.module`
- [locale_form_path_admin_form_alter()](../../locale/locale.module/locale_form_path_admin_form_alter.md) — `modules/locale/locale.module`
- [menu_form_node_type_form_alter()](../../menu/menu.module/menu_form_node_type_form_alter.md) — `modules/menu/menu.module`
- [minimal_form_install_configure_form_alter()](../../../profiles/minimal/minimal.profile/minimal_form_install_configure_form_alter.md) — `profiles/minimal/minimal.profile`
- [node_form_search_form_alter()](../../node/node.module/node_form_search_form_alter.md) — `modules/node/node.module`
- [openid_form_user_login_alter()](../../openid/openid.module/openid_form_user_login_alter.md) — `modules/openid/openid.module`
- [openid_form_user_login_block_alter()](../../openid/openid.module/openid_form_user_login_block_alter.md) — `modules/openid/openid.module`
- [openid_form_user_register_form_alter()](../../openid/openid.module/openid_form_user_register_form_alter.md) — `modules/openid/openid.module`
- [overlay_form_user_profile_form_alter()](../../overlay/overlay.module/overlay_form_user_profile_form_alter.md) — `modules/overlay/overlay.module`
- [path_form_taxonomy_form_term_alter()](../../path/path.module/path_form_taxonomy_form_term_alter.md) — `modules/path/path.module`
- [standard_form_install_configure_form_alter()](../../../profiles/standard/standard.profile/standard_form_install_configure_form_alter.md) — `profiles/standard/standard.profile`
- [syslog_form_system_logging_settings_alter()](../../syslog/syslog.module/syslog_form_system_logging_settings_alter.md) — `modules/syslog/syslog.module`
- [system_form_user_profile_form_alter()](../system.module/system_form_user_profile_form_alter.md) — `modules/system/system.module`
- [system_form_user_register_form_alter()](../system.module/system_form_user_register_form_alter.md) — `modules/system/system.module`
- [test_theme_form_system_theme_settings_alter()](../../simpletest/tests/themes/test_theme/theme-settings.php/test_theme_form_system_theme_settings_alter.md) — `modules/simpletest/tests/themes/test_theme/theme-settings.php`
- [translation_form_node_type_form_alter()](../../translation/translation.module/translation_form_node_type_form_alter.md) — `modules/translation/translation.module`
- [update_form_system_modules_alter()](../../update/update.module/update_form_system_modules_alter.md) — `modules/update/update.module`
- [user_form_field_ui_field_edit_form_alter()](../../user/user.module/user_form_field_ui_field_edit_form_alter.md) — `modules/user/user.module`
- [user_form_test_form_user_pass_reset_alter()](../../user/tests/user_form_test.module/user_form_test_form_user_pass_reset_alter.md) — `modules/user/tests/user_form_test.module`
- [user_form_test_form_user_profile_form_alter()](../../user/tests/user_form_test.module/user_form_test_form_user_profile_form_alter.md) — `modules/user/tests/user_form_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

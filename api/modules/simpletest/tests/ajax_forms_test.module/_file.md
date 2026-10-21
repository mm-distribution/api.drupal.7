# modules/simpletest/tests/ajax_forms_test.module

- **Source:** [local](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · 521 lines
- **Module/theme:** batch_test

## File documentation

```text
@file
Simpletest mock module for Ajax forms testing.
```

## Functions (derived index)

- [ajax_forms_test_menu()](ajax_forms_test_menu.md) — Implements hook_menu().
- [ajax_forms_test_simple_form()](ajax_forms_test_simple_form.md) — A basic form used to test form_state['values'] during callback.
- [ajax_forms_test_simple_form_select_callback()](ajax_forms_test_simple_form_select_callback.md) — Ajax callback triggered by select.
- [ajax_forms_test_simple_form_checkbox_callback()](ajax_forms_test_simple_form_checkbox_callback.md) — Ajax callback triggered by checkbox.
- [ajax_forms_test_ajax_commands_form()](ajax_forms_test_ajax_commands_form.md) — Form to display the Ajax Commands.
- [ajax_forms_test_advanced_commands_after_callback()](ajax_forms_test_advanced_commands_after_callback.md) — Ajax callback for 'after'.
- [ajax_forms_test_advanced_commands_alert_callback()](ajax_forms_test_advanced_commands_alert_callback.md) — Ajax callback for 'alert'.
- [ajax_forms_test_advanced_commands_append_callback()](ajax_forms_test_advanced_commands_append_callback.md) — Ajax callback for 'append'.
- [ajax_forms_test_advanced_commands_before_callback()](ajax_forms_test_advanced_commands_before_callback.md) — Ajax callback for 'before'.
- [ajax_forms_test_advanced_commands_changed_callback()](ajax_forms_test_advanced_commands_changed_callback.md) — Ajax callback for 'changed'.
- [ajax_forms_test_advanced_commands_changed_asterisk_callback()](ajax_forms_test_advanced_commands_changed_asterisk_callback.md) — Ajax callback for 'changed' with asterisk marking inner div.
- [ajax_forms_test_advanced_commands_css_callback()](ajax_forms_test_advanced_commands_css_callback.md) — Ajax callback for 'css'.
- [ajax_forms_test_advanced_commands_data_callback()](ajax_forms_test_advanced_commands_data_callback.md) — Ajax callback for 'data'.
- [ajax_forms_test_advanced_commands_invoke_callback()](ajax_forms_test_advanced_commands_invoke_callback.md) — Ajax callback for 'invoke'.
- [ajax_forms_test_advanced_commands_html_callback()](ajax_forms_test_advanced_commands_html_callback.md) — Ajax callback for 'html'.
- [ajax_forms_test_advanced_commands_insert_callback()](ajax_forms_test_advanced_commands_insert_callback.md) — Ajax callback for 'insert'.
- [ajax_forms_test_advanced_commands_prepend_callback()](ajax_forms_test_advanced_commands_prepend_callback.md) — Ajax callback for 'prepend'.
- [ajax_forms_test_advanced_commands_remove_callback()](ajax_forms_test_advanced_commands_remove_callback.md) — Ajax callback for 'remove'.
- [ajax_forms_test_advanced_commands_restripe_callback()](ajax_forms_test_advanced_commands_restripe_callback.md) — Ajax callback for 'restripe'.
- [ajax_forms_test_advanced_commands_settings_callback()](ajax_forms_test_advanced_commands_settings_callback.md) — Ajax callback for 'settings'.
- [ajax_forms_test_advanced_commands_add_css_callback()](ajax_forms_test_advanced_commands_add_css_callback.md) — Ajax callback for 'add_css'.
- [ajax_forms_test_validation_form()](ajax_forms_test_validation_form.md) — This form and its related submit and callback functions demonstrate not validating another form element when a single Ajax element is triggered.
- [ajax_forms_test_validation_form_submit()](ajax_forms_test_validation_form_submit.md) — Submit handler for the validation form.
- [ajax_forms_test_validation_form_callback()](ajax_forms_test_validation_form_callback.md) — Ajax callback for the 'drivertext' element of the validation form.
- [ajax_forms_test_lazy_load_form()](ajax_forms_test_lazy_load_form.md) — Form builder: Builds a form that triggers a simple AJAX callback.
- [ajax_forms_test_lazy_load_form_submit()](ajax_forms_test_lazy_load_form_submit.md) — Form submit handler: Adds JavaScript and CSS that wasn't on the original form.
- [ajax_forms_test_lazy_load_form_ajax()](ajax_forms_test_lazy_load_form_ajax.md) — AJAX callback for the ajax_forms_test_lazy_load_form() form.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

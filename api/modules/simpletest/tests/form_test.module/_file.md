# modules/simpletest/tests/form_test.module

- **Source:** [local](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · 2019 lines
- **Module/theme:** batch_test

## File documentation

```text
@file
Helper module for the form API tests.
```

## Functions (derived index)

- [form_test_menu()](form_test_menu.md) — Implements hook_menu().
- [_form_test_submit_values_json()](_form_test_submit_values_json.md) — Form submit handler to return form values as JSON.
- [form_test_alter_form()](form_test_alter_form.md) — Form builder for testing hook_form_alter() and hook_form_FORM_ID_alter().
- [block_form_form_test_alter_form_alter()](block_form_form_test_alter_form_alter.md) — Implements hook_form_FORM_ID_alter() on behalf of block.module.
- [form_test_form_alter()](form_test_form_alter.md) — Implements hook_form_alter().
- [form_test_form_form_test_alter_form_alter()](form_test_form_form_test_alter_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [system_form_form_test_alter_form_alter()](system_form_form_test_alter_form_alter.md) — Implements hook_form_FORM_ID_alter() on behalf of system.module.
- [form_test_validate_form()](form_test_validate_form.md) — Form builder for testing drupal_validate_form().
- [form_test_element_validate_name()](form_test_element_validate_name.md) — Form element validation handler for 'name' in form_test_validate_form().
- [form_test_validate_form_validate()](form_test_validate_form_validate.md) — Form validation handler for form_test_validate_form().
- [form_test_validate_required_form()](form_test_validate_required_form.md) — Form constructor to test the #required property.
- [form_test_validate_required_form_submit()](form_test_validate_required_form_submit.md) — Form submission handler for form_test_validate_required_form().
- [form_test_validate_required_form_no_title()](form_test_validate_required_form_no_title.md) — Form constructor to test the #required property without #title.
- [form_test_validate_required_form_no_title_submit()](form_test_validate_required_form_no_title_submit.md) — Form submission handler for form_test_validate_required_form_no_title().
- [form_test_validate_no_token()](form_test_validate_no_token.md) — Form builder for testing submission of a form without a CSRF token.
- [form_test_validate_no_token_submit()](form_test_validate_no_token_submit.md) — Form submission handler for form_test_validate_no_token().
- [form_test_limit_validation_errors_form()](form_test_limit_validation_errors_form.md) — Builds a simple form with a button triggering partial validation.
- [form_test_limit_validation_errors_element_validate_test()](form_test_limit_validation_errors_element_validate_test.md) — Form element validation handler for the 'test' element.
- [form_test_limit_validation_errors_form_partial_submit()](form_test_limit_validation_errors_form_partial_submit.md) — Form submit handler for the partial validation submit button.
- [_form_test_tableselect_get_data()](_form_test_tableselect_get_data.md) — Create a header and options array. Helper function for callbacks.
- [_form_test_tableselect_form_builder()](_form_test_tableselect_form_builder.md) — Build a form to test the tableselect element.
- [_form_test_tableselect_multiple_true_form()](_form_test_tableselect_multiple_true_form.md) — Test the tableselect #multiple = TRUE functionality.
- [_form_test_tableselect_multiple_true_form_submit()](_form_test_tableselect_multiple_true_form_submit.md) — Process the tableselect #multiple = TRUE submitted values.
- [_form_test_tableselect_multiple_false_form()](_form_test_tableselect_multiple_false_form.md) — Test the tableselect #multiple = FALSE functionality.
- [_form_test_tableselect_multiple_false_form_submit()](_form_test_tableselect_multiple_false_form_submit.md) — Process the tableselect #multiple = FALSE submitted values.
- [_form_test_tableselect_empty_form()](_form_test_tableselect_empty_form.md) — Test functionality of the tableselect #empty property.
- [_form_test_tableselect_js_select_form()](_form_test_tableselect_js_select_form.md) — Test functionality of the tableselect #js_select property.
- [_form_test_vertical_tabs_form()](_form_test_vertical_tabs_form.md) — Tests functionality of vertical tabs.
- [_form_test_tableselect_ajax_callback()](_form_test_tableselect_ajax_callback.md) — Ajax callback that returns the form element.
- [form_test_storage_form()](form_test_storage_form.md) — A multistep form for testing the form storage.
- [form_test_storage_legacy_handler()](form_test_storage_legacy_handler.md) — Emulate legacy AHAH-style ajax callback.
- [form_test_storage_element_validate_value_cached()](form_test_storage_element_validate_value_cached.md) — Form element validation handler for 'value' element in form_test_storage_form().
- [form_storage_test_form_continue_submit()](form_storage_test_form_continue_submit.md) — Form submit handler to continue multi-step form.
- [form_test_storage_form_submit()](form_test_storage_form_submit.md) — Form submit handler to finish multi-step form.
- [form_test_storage_page_cache_form()](form_test_storage_page_cache_form.md) — A simple form for testing form storage when page caching is enabled.
- [form_test_storage_page_cache_old_build_id()](form_test_storage_page_cache_old_build_id.md) — Form element #after_build callback: output the old form build-id.
- [form_test_storage_page_cache_rebuild()](form_test_storage_page_cache_rebuild.md) — Form submit callback: Rebuild the form and continue.
- [form_test_cache_form()](form_test_cache_form.md) — A simple form for testing form caching.
- [form_label_test_form()](form_label_test_form.md) — A form for testing form labels and required marks.
- [form_test_wrapper_callback()](form_test_wrapper_callback.md) — Menu callback; Invokes a form builder function with a wrapper callback.
- [form_test_wrapper_callback_wrapper()](form_test_wrapper_callback_wrapper.md) — Form wrapper for form_test_wrapper_callback_form().
- [form_test_wrapper_callback_form()](form_test_wrapper_callback_form.md) — Form builder for form wrapper callback test.
- [form_test_form_state_values_clean_form()](form_test_form_state_values_clean_form.md) — Form builder for form_state_values_clean() test.
- [form_test_form_state_values_clean_form_submit()](form_test_form_state_values_clean_form_submit.md) — Form submit handler for form_state_values_clean() test form.
- [form_test_form_state_values_clean_advanced_form()](form_test_form_state_values_clean_advanced_form.md) — Form constructor for the form_state_values_clean() test.
- [form_test_form_state_values_clean_advanced_form_submit()](form_test_form_state_values_clean_advanced_form_submit.md) — Form submission handler for form_test_form_state_values_clean_advanced_form().
- [_form_test_checkbox()](_form_test_checkbox.md) — Build a form to test a checkbox.
- [_form_test_checkbox_submit()](_form_test_checkbox_submit.md) — Return the form values via JSON.
- [form_test_select()](form_test_select.md) — Builds a form to test #type 'select' validation.
- [form_test_select_submit()](form_test_select_submit.md) — Form submit handler for form_test_select().
- [form_test_checkboxes_radios()](form_test_checkboxes_radios.md) — Form constructor to test expansion of #type checkboxes and radios.
- [_form_test_disabled_elements()](_form_test_disabled_elements.md) — Build a form to test disabled elements.
- [_form_test_disabled_elements_submit()](_form_test_disabled_elements_submit.md) — Return the form values via JSON.
- [_form_test_input_forgery()](_form_test_input_forgery.md) — Build a form to test input forgery of enabled elements.
- [_form_test_input_forgery_submit()](_form_test_input_forgery_submit.md) — Return the form values via JSON.
- [form_test_form_rebuild_preserve_values_form()](form_test_form_rebuild_preserve_values_form.md) — Form builder for testing preservation of values during a rebuild.
- [form_test_form_rebuild_preserve_values_form_add_more()](form_test_form_rebuild_preserve_values_form_add_more.md) — Button submit handler for form_test_form_rebuild_preserve_values_form().
- [form_test_form_rebuild_preserve_values_form_submit()](form_test_form_rebuild_preserve_values_form_submit.md) — Form submit handler for form_test_form_rebuild_preserve_values_form().
- [form_test_state_persist()](form_test_state_persist.md) — Form constructor for testing form state persistence.
- [form_test_state_persist_submit()](form_test_state_persist_submit.md) — Submit handler.
- [form_test_form_form_test_state_persist_alter()](form_test_form_form_test_state_persist_alter.md) — Implements hook_form_FORM_ID_alter().
- [form_test_programmatic_form()](form_test_programmatic_form.md) — Form builder to test programmatic form submissions.
- [form_test_programmatic_form_validate()](form_test_programmatic_form_validate.md) — Form validation handler for programmatic form submissions.
- [form_test_programmatic_form_submit()](form_test_programmatic_form_submit.md) — Form submit handler for programmatic form submissions.
- [form_test_clicked_button()](form_test_clicked_button.md) — Form builder to test button click detection.
- [form_test_clicked_button_validate()](form_test_clicked_button_validate.md) — Form validation handler for the form_test_clicked_button() form.
- [form_test_clicked_button_submit()](form_test_clicked_button_submit.md) — Form submit handler for the form_test_clicked_button() form.
- [form_test_redirect()](form_test_redirect.md) — Form builder to detect form redirect.
- [form_test_redirect_submit()](form_test_redirect_submit.md) — Form submit handler to test different redirect behaviours.
- [form_test_form_user_register_form_alter()](form_test_form_user_register_form_alter.md) — Implements hook_form_FORM_ID_alter() for the registration form.
- [form_test_user_register_form_rebuild()](form_test_user_register_form_rebuild.md) — Submit callback that just lets the form rebuild.
- [form_test_two_instances()](form_test_two_instances.md) — Menu callback that returns two instances of the node form.
- [form_test_load_include_custom()](form_test_load_include_custom.md) — Menu callback for testing custom form includes.
- [form_test_checkbox_type_juggling()](form_test_checkbox_type_juggling.md)
- [form_test_checkboxes_zero()](form_test_checkboxes_zero.md)
- [_form_test_checkboxes_zero_no_redirect()](_form_test_checkboxes_zero_no_redirect.md)
- [form_test_double_form()](form_test_double_form.md) — Menu callback returns two instances of the same form.
- [form_test_html_id()](form_test_html_id.md) — Builds a simple form to test duplicate HTML IDs.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

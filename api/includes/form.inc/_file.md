# includes/form.inc

- **Source:** [local](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · 4867 lines

## File documentation

```text
@file
Functions for form and batch generation and processing.
```

## Functions (derived index)

- [drupal_get_form()](drupal_get_form.md) — Returns a renderable form array for a given form ID.
- [drupal_build_form()](drupal_build_form.md) — Builds and process a form based on a form id.
- [form_state_defaults()](form_state_defaults.md) — Retrieves default values for the $form_state array.
- [drupal_rebuild_form()](drupal_rebuild_form.md) — Constructs a new $form from the information in $form_state.
- [form_get_cache()](form_get_cache.md) — Fetches a form from cache.
- [form_set_cache()](form_set_cache.md) — Stores a form in the cache.
- [form_state_keys_no_cache()](form_state_keys_no_cache.md) — Returns an array of $form_state keys that shouldn't be cached.
- [form_load_include()](form_load_include.md) — Ensures an include file is loaded whenever the form is processed.
- [drupal_form_submit()](drupal_form_submit.md) — Retrieves, populates, and processes a form.
- [drupal_retrieve_form()](drupal_retrieve_form.md) — Retrieves the structured array that defines a given form.
- [drupal_process_form()](drupal_process_form.md) — Processes a form submission.
- [drupal_prepare_form()](drupal_prepare_form.md) — Prepares a structured form array.
- [_drupal_invalid_token_set_form_error()](_drupal_invalid_token_set_form_error.md) — Helper function to call form_set_error() if there is a token error.
- [drupal_validate_form()](drupal_validate_form.md) — Validates user-submitted form data in the $form_state array.
- [drupal_redirect_form()](drupal_redirect_form.md) — Redirects the user to a URL after a form has been processed.
- [_form_validate()](_form_validate.md) — Performs validation on form elements.
- [form_execute_handlers()](form_execute_handlers.md) — Executes custom validation and submission handlers for a given form.
- [form_set_error()](form_set_error.md) — Files an error against a form element.
- [form_clear_error()](form_clear_error.md) — Clears all errors against all form elements made by form_set_error().
- [form_get_errors()](form_get_errors.md) — Returns an associative array of all errors if any.
- [form_get_error()](form_get_error.md) — Returns the error message filed against the given form element.
- [form_error()](form_error.md) — Flags an element as having an error.
- [form_builder()](form_builder.md) — Builds and processes all elements in the structured form array.
- [_form_builder_handle_input_element()](_form_builder_handle_input_element.md) — Adds the #name and #value properties of an input element before rendering.
- [_form_element_triggered_scripted_submission()](_form_element_triggered_scripted_submission.md) — Detects if an element triggered the form submission via Ajax.
- [_form_button_was_clicked()](_form_button_was_clicked.md) — Determines if a given button triggered the form submission.
- [form_state_values_clean()](form_state_values_clean.md) — Removes internal Form API elements and buttons from submitted form values.
- [form_type_image_button_value()](form_type_image_button_value.md) — Determines the value for an image button form element.
- [form_type_checkbox_value()](form_type_checkbox_value.md) — Determines the value for a checkbox form element.
- [form_type_checkboxes_value()](form_type_checkboxes_value.md) — Determines the value for a checkboxes form element.
- [form_type_tableselect_value()](form_type_tableselect_value.md) — Determines the value for a tableselect form element.
- [form_type_radios_value()](form_type_radios_value.md) — Form value callback: Determines the value for a #type radios form element.
- [form_type_password_confirm_value()](form_type_password_confirm_value.md) — Determines the value for a password_confirm form element.
- [form_type_select_value()](form_type_select_value.md) — Determines the value for a select form element.
- [form_type_textarea_value()](form_type_textarea_value.md) — Determines the value for a textarea form element.
- [form_type_textfield_value()](form_type_textfield_value.md) — Determines the value for a textfield form element.
- [form_type_token_value()](form_type_token_value.md) — Determines the value for form's token value.
- [form_set_value()](form_set_value.md) — Changes submitted form values during form validation.
- [form_options_flatten()](form_options_flatten.md) — Allows PHP array processing of multiple select options with the same value.
- [_form_options_flatten()](_form_options_flatten.md) — Iterates over an array and returns a flat array with duplicate keys removed.
- [form_process_select()](form_process_select.md) — Processes a select list form element.
- [theme_select()](theme_select.md) — Returns HTML for a select form element.
- [form_select_options()](form_select_options.md) — Converts an array of options into HTML, for use in select list form elements.
- [form_get_options()](form_get_options.md) — Returns the indexes of a select element's options matching a given key.
- [theme_fieldset()](theme_fieldset.md) — Returns HTML for a fieldset form element and its children.
- [theme_radio()](theme_radio.md) — Returns HTML for a radio button form element.
- [theme_radios()](theme_radios.md) — Returns HTML for a set of radio button form elements.
- [form_process_password_confirm()](form_process_password_confirm.md) — Expand a password_confirm field into two text boxes.
- [password_confirm_validate()](password_confirm_validate.md) — Validates a password_confirm element.
- [theme_date()](theme_date.md) — Returns HTML for a date selection form element.
- [form_process_date()](form_process_date.md) — Expands a date element into year, month, and day select elements.
- [date_validate()](date_validate.md) — Validates the date type to prevent invalid dates (e.g., February 30, 2006).
- [map_month()](map_month.md) — Helper function for usage with drupal_map_assoc to display month names.
- [weight_value()](weight_value.md) — Sets the value for a weight element, with zero as a default.
- [form_process_radios()](form_process_radios.md) — Expands a radios element into individual radio elements.
- [theme_checkbox()](theme_checkbox.md) — Returns HTML for a checkbox form element.
- [theme_checkboxes()](theme_checkboxes.md) — Returns HTML for a set of checkbox form elements.
- [form_pre_render_conditional_form_element()](form_pre_render_conditional_form_element.md) — Adds form element theming to an element if its title or description is set.
- [form_process_checkbox()](form_process_checkbox.md) — Sets the #checked property of a checkbox element.
- [form_process_checkboxes()](form_process_checkboxes.md) — Processes a checkboxes form element.
- [form_process_actions()](form_process_actions.md) — Processes a form actions container element.
- [form_process_button()](form_process_button.md) — Processes a form button element.
- [form_process_container()](form_process_container.md) — Processes a container element.
- [theme_container()](theme_container.md) — Returns HTML to wrap child elements in a container.
- [theme_tableselect()](theme_tableselect.md) — Returns HTML for a table with radio buttons or checkboxes.
- [form_process_tableselect()](form_process_tableselect.md) — Creates checkbox or radio elements to populate a tableselect table.
- [form_process_machine_name()](form_process_machine_name.md) — Processes a machine-readable name form element.
- [form_validate_machine_name()](form_validate_machine_name.md) — Form element validation handler for machine_name elements.
- [form_process_fieldset()](form_process_fieldset.md) — Arranges fieldsets into groups.
- [form_pre_render_fieldset()](form_pre_render_fieldset.md) — Adds members of this group as actual elements for rendering.
- [form_process_vertical_tabs()](form_process_vertical_tabs.md) — Creates a group formatted as vertical tabs.
- [theme_vertical_tabs()](theme_vertical_tabs.md) — Returns HTML for an element's children fieldsets as vertical tabs.
- [theme_submit()](theme_submit.md) — Returns HTML for a submit button form element.
- [theme_button()](theme_button.md) — Returns HTML for a button form element.
- [theme_image_button()](theme_image_button.md) — Returns HTML for an image button form element.
- [theme_hidden()](theme_hidden.md) — Returns HTML for a hidden form element.
- [form_process_autocomplete()](form_process_autocomplete.md) — Process function to prepare autocomplete data.
- [theme_textfield()](theme_textfield.md) — Returns HTML for a textfield form element.
- [theme_form()](theme_form.md) — Returns HTML for a form.
- [theme_textarea()](theme_textarea.md) — Returns HTML for a textarea form element.
- [theme_password()](theme_password.md) — Returns HTML for a password form element.
- [form_process_weight()](form_process_weight.md) — Expands a weight element into a select element.
- [theme_file()](theme_file.md) — Returns HTML for a file upload form element.
- [theme_form_element()](theme_form_element.md) — Returns HTML for a form element.
- [theme_form_required_marker()](theme_form_required_marker.md) — Returns HTML for a marker for required form elements.
- [theme_form_element_label()](theme_form_element_label.md) — Returns HTML for a form element label and required marker.
- [_form_set_class()](_form_set_class.md) — Sets a form element's class attribute.
- [element_validate_integer()](element_validate_integer.md) — Form element validation handler for integer elements.
- [element_validate_integer_positive()](element_validate_integer_positive.md) — Form element validation handler for integer elements that must be positive.
- [element_validate_number()](element_validate_number.md) — Form element validation handler for number elements.
- [batch_set()](batch_set.md) — Adds a new batch.
- [batch_process()](batch_process.md) — Processes the batch.
- [batch_get()](batch_get.md) — Retrieves the current batch.
- [_batch_populate_queue()](_batch_populate_queue.md) — Populates a job queue with the operations of a batch set.
- [_batch_queue()](_batch_queue.md) — Returns a queue object for a batch set.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

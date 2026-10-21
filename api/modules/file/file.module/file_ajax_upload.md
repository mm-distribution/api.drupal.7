# file_ajax_upload()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 238–303 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L238-L303)
- **Module/theme:** file

## Signature

```php
function file_ajax_upload()
```

## Documentation

```text
Menu callback; Shared Ajax callback for file uploads and deletions.

This rebuilds the form element for a particular field item. As long as the
form processing is properly encapsulated in the widget element the form
should rebuild correctly using FAPI without the need for additional callbacks
or processing.
```

## Code

```php
function file_ajax_upload() {
  $form_parents = func_get_args();
  $form_build_id = (string) array_pop($form_parents);

  // Sanitize form parents before using them.
  $form_parents = array_filter($form_parents, 'element_child');

  if (empty($_POST['form_build_id']) || $form_build_id != $_POST['form_build_id']) {
    // Invalid request.
    drupal_set_message(t('An unrecoverable error occurred. The uploaded file likely exceeded the maximum file size (@size) that this server supports.', array('@size' => format_size(file_upload_max_size()))), 'error');
    $commands = array();
    $commands[] = ajax_command_prepend(NULL, theme('status_messages'));

    // Unset the problematic file from the input so that user can submit the
    // form without reloading the page.
    // @see https://www.drupal.org/project/drupal/issues/2749245
    $field_name = (string) reset($form_parents);
    $wrapper_id = drupal_html_id('edit-' . $field_name);
    $commands[] = ajax_command_invoke('#' . $wrapper_id . ' .form-type-managed-file input[type="file"]', 'val', array(''));

    return array('#type' => 'ajax', '#commands' => $commands);
  }

  list($form, $form_state, $form_id, $form_build_id, $commands) = ajax_get_form();

  if (!$form) {
    // Invalid form_build_id.
    drupal_set_message(t('An unrecoverable error occurred. Use of this form has expired. Try reloading the page and submitting again.'), 'error');
    $commands = array();
    $commands[] = ajax_command_prepend(NULL, theme('status_messages'));
    return array('#type' => 'ajax', '#commands' => $commands);
  }

  // Get the current element and count the number of files.
  $current_element = $form;
  foreach ($form_parents as $parent) {
    $current_element = $current_element[$parent];
  }
  $current_file_count = isset($current_element['#file_upload_delta']) ? $current_element['#file_upload_delta'] : 0;

  // Process user input. $form and $form_state are modified in the process.
  drupal_process_form($form['#form_id'], $form, $form_state);

  // Retrieve the element to be rendered.
  foreach ($form_parents as $parent) {
    $form = $form[$parent];
  }

  // Add the special Ajax class if a new file was added.
  if (isset($form['#file_upload_delta']) && $current_file_count < $form['#file_upload_delta']) {
    $form[$current_file_count]['#attributes']['class'][] = 'ajax-new-content';
  }
  // Otherwise just add the new content class on a placeholder.
  else {
    $form['#suffix'] = (isset($form['#suffix']) ? $form['#suffix'] : '') . '<span class="ajax-new-content"></span>';
  }

  $form['#prefix'] = (isset($form['#prefix']) ? $form['#prefix'] : '') . theme('status_messages');

  $output = drupal_render($form);
  $js = drupal_add_js();
  $settings = drupal_array_merge_deep_array($js['settings']['data']);

  $commands[] = ajax_command_replace(NULL, $output, $settings);
  return array('#type' => 'ajax', '#commands' => $commands);
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._

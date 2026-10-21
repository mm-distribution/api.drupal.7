# file_field_widget_value()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 596–617 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L596-L617)
- **Module/theme:** file

## Signature

```php
function file_field_widget_value($element, $input = FALSE, $form_state = array())
```

## Documentation

```text
The #value_callback for the file_generic field element.
```

## Code

```php
function file_field_widget_value($element, $input = FALSE, $form_state = array()) {
  if ($input) {
    // Checkboxes lose their value when empty.
    // If the display field is present make sure its unchecked value is saved.
    $field = field_widget_field($element, $form_state);
    if (empty($input['display'])) {
      $input['display'] = !empty($field['settings']['display_field']) ? 0 : 1;
    }
  }

  // We depend on the managed file element to handle uploads.
  $return = file_managed_file_value($element, $input, $form_state);

  // Ensure that all the required properties are returned even if empty.
  $return += array(
    'fid' => 0,
    'display' => 1,
    'description' => '',
  );

  return $return;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

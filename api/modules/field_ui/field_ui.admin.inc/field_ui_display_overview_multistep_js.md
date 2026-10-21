# field_ui_display_overview_multistep_js()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1289–1322 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1289-L1322)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_display_overview_multistep_js($form, &$form_state)
```

## Documentation

```text
Ajax handler for multistep buttons on the 'Manage display' screen.
```

## Code

```php
function field_ui_display_overview_multistep_js($form, &$form_state) {
  $trigger = $form_state['triggering_element'];
  $op = $trigger['#op'];

  // Pick the elements that need to receive the ajax-new-content effect.
  switch ($op) {
    case 'edit':
      $updated_rows = array($trigger['#field_name']);
      $updated_columns = array('format');
      break;

    case 'update':
    case 'cancel':
      $updated_rows = array($trigger['#field_name']);
      $updated_columns = array('format', 'settings_summary', 'settings_edit');
      break;

    case 'refresh_table':
      $updated_rows = array_values(explode(' ', $form_state['values']['refresh_rows']));
      $updated_columns = array('settings_summary', 'settings_edit');
      break;
  }

  foreach ($updated_rows as $name) {
    foreach ($updated_columns as $key) {
      $element = &$form['fields'][$name][$key];
      $element['#prefix'] = '<div class="ajax-new-content">' . (isset($element['#prefix']) ? $element['#prefix'] : '');
      $element['#suffix'] = (isset($element['#suffix']) ? $element['#suffix'] : '') . '</div>';
    }
  }

  // Return the whole table.
  return $form['fields'];
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# taxonomy_field_settings_form()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1804–1832 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1804-L1832)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_settings_form()](../../field_ui/field_ui.api.php/hook_field_settings_form.md)

## Signature

```php
function taxonomy_field_settings_form($field, $instance, $has_data)
```

## Documentation

```text
Implements hook_field_settings_form().
```

## Code

```php
function taxonomy_field_settings_form($field, $instance, $has_data) {
  // Get proper values for 'allowed_values_function', which is a core setting.
  $vocabularies = taxonomy_get_vocabularies();
  $options = array();
  foreach ($vocabularies as $vocabulary) {
    $options[$vocabulary->machine_name] = $vocabulary->name;
  }
  $form['allowed_values'] = array(
    '#tree' => TRUE,
  );

  foreach ($field['settings']['allowed_values'] as $delta => $tree) {
    $form['allowed_values'][$delta]['vocabulary'] = array(
      '#type' => 'select',
      '#title' => t('Vocabulary'),
      '#default_value' => $tree['vocabulary'],
      '#options' => $options,
      '#required' => TRUE,
      '#description' => t('The vocabulary which supplies the options for this field.'),
      '#disabled' => $has_data,
    );
    $form['allowed_values'][$delta]['parent'] = array(
      '#type' => 'value',
      '#value' => $tree['parent'],
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._

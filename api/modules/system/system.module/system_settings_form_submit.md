# system_settings_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2845–2857 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2845-L2857)
- **Module/theme:** system

## Signature

```php
function system_settings_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for system_settings_form().

If you want node type configure style handling of your checkboxes,
add an array_filter value to your form.
```

## Code

```php
function system_settings_form_submit($form, &$form_state) {
  // Exclude unnecessary elements.
  form_state_values_clean($form_state);

  foreach ($form_state['values'] as $key => $value) {
    if (is_array($value) && isset($form_state['values']['array_filter'])) {
      $value = array_keys(array_filter($value));
    }
    variable_set($key, $value);
  }

  drupal_set_message(t('The configuration options have been saved.'));
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._

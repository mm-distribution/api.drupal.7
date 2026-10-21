# path_admin_form_submit()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 225–233 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L225-L233)
- **Module/theme:** path

## Signature

```php
function path_admin_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for path_admin_form().

@see path_admin_form_validate()
@see path_admin_form_delete_submit()
```

## Code

```php
function path_admin_form_submit($form, &$form_state) {
  // Remove unnecessary values.
  form_state_values_clean($form_state);

  path_save($form_state['values']);

  drupal_set_message(t('The alias has been saved.'));
  $form_state['redirect'] = 'admin/config/search/path';
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

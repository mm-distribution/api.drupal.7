# filter_admin_format_form_submit()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 349–376 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L349-L376)
- **Module/theme:** filter

## Signature

```php
function filter_admin_format_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for filter_admin_format_form().

@see filter_admin_format_form_validate()
```

## Code

```php
function filter_admin_format_form_submit($form, &$form_state) {
  // Remove unnecessary values.
  form_state_values_clean($form_state);

  // Add the submitted form values to the text format, and save it.
  $format = $form['#format'];
  foreach ($form_state['values'] as $key => $value) {
    $format->$key = $value;
  }
  $status = filter_format_save($format);

  // Save user permissions.
  if ($permission = filter_permission_name($format)) {
    foreach ($format->roles as $rid => $enabled) {
      user_role_change_permissions($rid, array($permission => $enabled));
    }
  }

  switch ($status) {
    case SAVED_NEW:
      drupal_set_message(t('Added text format %format.', array('%format' => $format->name)));
      break;

    case SAVED_UPDATED:
      drupal_set_message(t('The text format %format has been updated.', array('%format' => $format->name)));
      break;
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

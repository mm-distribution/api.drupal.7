# update_manager_update_form_validate()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 291–301 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L291-L301)
- **Module/theme:** update
- **Topics:** [update_manager_update](../../../topics/update_manager_update.md)

## Signature

```php
function update_manager_update_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for update_manager_update_form().

Ensures that at least one project is selected.

@see update_manager_update_form_submit()
```

## Code

```php
function update_manager_update_form_validate($form, &$form_state) {
  if (!empty($form_state['values']['projects'])) {
    $enabled = array_filter($form_state['values']['projects']);
  }
  if (!empty($form_state['values']['disabled_projects'])) {
    $disabled = array_filter($form_state['values']['disabled_projects']);
  }
  if (empty($enabled) && empty($disabled)) {
    form_set_error('projects', t('You must select at least one project to update.'));
  }
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

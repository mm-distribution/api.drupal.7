# update_manager_install_form_validate()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 613–623 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L613-L623)
- **Module/theme:** update
- **Topics:** [update_manager_install](../../../topics/update_manager_install.md)

## Signature

```php
function update_manager_install_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for update_manager_install_form().

@see update_manager_install_form_submit()
```

## Code

```php
function update_manager_install_form_validate($form, &$form_state) {
  if (!($form_state['values']['project_url'] XOR !empty($_FILES['files']['name']['project_upload']))) {
    form_set_error('project_url', t('You must either provide a URL or upload an archive file to install.'));
  }

  if ($form_state['values']['project_url']) {
    if (!valid_url($form_state['values']['project_url'], TRUE)) {
      form_set_error('project_url', t('The provided URL is invalid.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

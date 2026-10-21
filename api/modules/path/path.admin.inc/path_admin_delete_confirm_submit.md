# path_admin_delete_confirm_submit()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 259–264 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L259-L264)
- **Module/theme:** path

## Signature

```php
function path_admin_delete_confirm_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for path_admin_delete_confirm().
```

## Code

```php
function path_admin_delete_confirm_submit($form, &$form_state) {
  if ($form_state['values']['confirm']) {
    path_delete($form_state['path']['pid']);
    $form_state['redirect'] = 'admin/config/search/path';
  }
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

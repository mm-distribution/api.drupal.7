# user_admin_permissions_submit()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 770–779 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L770-L779)
- **Module/theme:** user

## Signature

```php
function user_admin_permissions_submit($form, &$form_state)
```

## Documentation

```text
Save permissions selected on the administer permissions page.

@see user_admin_permissions()
```

## Code

```php
function user_admin_permissions_submit($form, &$form_state) {
  foreach ($form_state['values']['role_names'] as $rid => $name) {
    user_role_change_permissions($rid, $form_state['values'][$rid]);
  }

  drupal_set_message(t('The changes have been saved.'));

  // Clear the cached pages and blocks.
  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

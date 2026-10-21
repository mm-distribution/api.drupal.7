# user_admin_account_submit()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 250–267 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L250-L267)
- **Module/theme:** user

## Signature

```php
function user_admin_account_submit($form, &$form_state)
```

## Documentation

```text
Submit the user administration update form.
```

## Code

```php
function user_admin_account_submit($form, &$form_state) {
  $operations = module_invoke_all('user_operations', $form, $form_state);
  $operation = $operations[$form_state['values']['operation']];
  // Filter out unchecked accounts.
  $accounts = array_filter($form_state['values']['accounts']);
  if ($function = $operation['callback']) {
    // Add in callback arguments if present.
    if (isset($operation['callback arguments'])) {
      $args = array_merge(array($accounts), $operation['callback arguments']);
    }
    else {
      $args = array($accounts);
    }
    call_user_func_array($function, $args);

    drupal_set_message(t('The update has been performed.'));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

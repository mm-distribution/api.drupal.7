# hook_user_operations()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 168–183 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L168-L183)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_operations()
```

## Documentation

```text
Add mass user operations.

This hook enables modules to inject custom operations into the mass operations
dropdown found at admin/people, by associating a callback function with
the operation, which is called when the form is submitted. The callback function
receives one initial argument, which is an array of the checked users.

@return
  An array of operations. Each operation is an associative array that may
  contain the following key-value pairs:
  - "label": Required. The label for the operation, displayed in the dropdown menu.
  - "callback": Required. The function to call for the operation.
  - "callback arguments": Optional. An array of additional arguments to pass to
    the callback function.
```

## Code

```php
function hook_user_operations() {
  $operations = array(
    'unblock' => array(
      'label' => t('Unblock the selected users'),
      'callback' => 'user_user_operations_unblock',
    ),
    'block' => array(
      'label' => t('Block the selected users'),
      'callback' => 'user_user_operations_block',
    ),
    'cancel' => array(
      'label' => t('Cancel the selected user accounts'),
    ),
  );
  return $operations;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_operations()".

- [user_user_operations()](../user.module/user_user_operations.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

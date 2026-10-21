# user_email_validation_test_valid_email_address_alter()

- **Type:** Function
- **File:** [`modules/user/tests/user_email_validation_test.module`](_file.md), lines 11–17 · [local source](../../../../../source/modules/user/tests/user_email_validation_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_email_validation_test.module#L11-L17)
- **Module/theme:** user_flood_test
- **Implements:** [hook_valid_email_address_alter()](../../../system/system.api.php/hook_valid_email_address_alter.md)

## Signature

```php
function user_email_validation_test_valid_email_address_alter(&$valid, $mail)
```

## Documentation

```text
Implements hook_valid_email_address_alter().
```

## Code

```php
function user_email_validation_test_valid_email_address_alter(&$valid, $mail) {
  $local = '.local';
  // Invalidate all e-mails ending with .local.
  if (substr_compare($mail, $local, -strlen($local)) === 0) {
    $valid = FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/user/tests/user_email_validation_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_email_validation_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

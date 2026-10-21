# hook_valid_email_address_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4836–4845 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4836-L4845)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_valid_email_address_alter(&$valid, $mail)
```

## Documentation

```text
Alter core e-mail validation.

This hook is called immediately after core e-mail validation takes place and
gives other modules a chance to override it. This is useful in cases where
you want to have stricter or looser validation standards than that provided
by Drupal core.

@param $valid
  Boolean value referencing the validation result.

@param $mail
  E-mail address being validated.

@see valid_email_address()
```

## Code

```php
function hook_valid_email_address_alter(&$valid, $mail) {
  if (preg_match("/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/", $mail)) {
    list($username, $domain) = explode('@', $mail);
    // Check DNS records.
    if (checkdnsrr($domain, 'MX')) {
      $valid = TRUE;
    }
  }
  $valid = FALSE;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_valid_email_address_alter()".

- [user_email_validation_test_valid_email_address_alter()](../../user/tests/user_email_validation_test.module/user_email_validation_test_valid_email_address_alter.md) — `modules/user/tests/user_email_validation_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

# valid_email_address()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1292–1296 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1292-L1296)
- **Topics:** [validation](../../topics/validation.md)

## Signature

```php
function valid_email_address($mail)
```

## Documentation

```text
Verifies the syntax of the given e-mail address.

This uses the
@link http://php.net/manual/filter.filters.validate.php PHP e-mail validation filter. @endlink
However, a module may override this by implementing
hook_valid_email_address_alter(&$valid, $mail).

@see hook_valid_email_address_alter()

@param $mail
  A string containing an e-mail address.

@return
  TRUE if the address is in a valid format.
```

## Code

```php
function valid_email_address($mail) {
  $valid = (bool) filter_var($mail, FILTER_VALIDATE_EMAIL);
  drupal_alter('valid_email_address', $valid, $mail);
  return $valid;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

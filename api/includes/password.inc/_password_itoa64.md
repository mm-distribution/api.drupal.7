# _password_itoa64()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 41–43 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L41-L43)

## Signature

```php
function _password_itoa64()
```

## Documentation

```text
Returns a string for mapping an int to the corresponding base 64 character.
```

## Code

```php
function _password_itoa64() {
  return './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

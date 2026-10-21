# _password_get_count_log2()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 194–197 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L194-L197)

## Signature

```php
function _password_get_count_log2($setting)
```

## Documentation

```text
Parse the log2 iteration count from a stored hash or setting string.
```

## Code

```php
function _password_get_count_log2($setting) {
  $itoa64 = _password_itoa64();
  return strpos($itoa64, $setting[3]);
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

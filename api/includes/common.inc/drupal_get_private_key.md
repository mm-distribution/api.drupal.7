# drupal_get_private_key()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5336–5342 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5336-L5342)

## Signature

```php
function drupal_get_private_key()
```

## Documentation

```text
Ensures the private key variable used to generate tokens is set.

@return
  The private key.
```

## Code

```php
function drupal_get_private_key() {
  if (!($key = variable_get('drupal_private_key', 0))) {
    $key = drupal_random_key();
    variable_set('drupal_private_key', $key);
  }
  return $key;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

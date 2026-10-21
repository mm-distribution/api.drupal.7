# drupal_installation_attempted()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3012–3014 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3012-L3014)

## Signature

```php
function drupal_installation_attempted()
```

## Documentation

```text
Returns TRUE if a Drupal installation is currently being attempted.
```

## Code

```php
function drupal_installation_attempted() {
  return defined('MAINTENANCE_MODE') && MAINTENANCE_MODE == 'install';
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

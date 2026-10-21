# DrupalFakeCache::isEmpty()

- **Type:** Method
- **File:** [`includes/cache-install.inc`](../_file.md), lines 71–73 · [local source](../../../../source/includes/cache-install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache-install.inc#L71-L73)
- **Class:** [DrupalFakeCache](../DrupalFakeCache.md)

## Signature

```php
function isEmpty()
```

## Documentation

```text
Overrides DrupalDatabaseCache::isEmpty().
```

## Code

```php
  function isEmpty() {
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/cache-install.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache-install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

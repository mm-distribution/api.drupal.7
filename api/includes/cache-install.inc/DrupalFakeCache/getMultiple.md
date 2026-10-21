# DrupalFakeCache::getMultiple()

- **Type:** Method
- **File:** [`includes/cache-install.inc`](../_file.md), lines 29–31 · [local source](../../../../source/includes/cache-install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache-install.inc#L29-L31)
- **Class:** [DrupalFakeCache](../DrupalFakeCache.md)

## Signature

```php
function getMultiple(&$cids)
```

## Documentation

```text
Overrides DrupalDatabaseCache::getMultiple().
```

## Code

```php
  function getMultiple(&$cids) {
    return array();
  }
```

---
_Drupal 7.103 · [includes/cache-install.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache-install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

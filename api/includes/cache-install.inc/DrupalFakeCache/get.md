# DrupalFakeCache::get()

- **Type:** Method
- **File:** [`includes/cache-install.inc`](../_file.md), lines 22–24 · [local source](../../../../source/includes/cache-install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache-install.inc#L22-L24)
- **Class:** [DrupalFakeCache](../DrupalFakeCache.md)

## Signature

```php
function get($cid)
```

## Documentation

```text
Overrides DrupalDatabaseCache::get().
```

## Code

```php
  function get($cid) {
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/cache-install.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache-install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

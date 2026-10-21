# DrupalDatabaseCache::__construct()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 331–333 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L331-L333)
- **Class:** [DrupalDatabaseCache](../DrupalDatabaseCache.md)

## Signature

```php
function __construct($bin)
```

## Documentation

```text
Constructs a DrupalDatabaseCache object.

@param $bin
  The cache bin for which the object is created.
```

## Code

```php
  function __construct($bin) {
    $this->bin = $bin;
  }
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# ThemeRegistry::__construct()

- **Type:** Method
- **File:** [`includes/theme.inc`](../_file.md), lines 381–401 · [local source](../../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L381-L401)
- **Class:** [ThemeRegistry](../ThemeRegistry.md)

## Signature

```php
function __construct($cid, $bin)
```

## Documentation

_No docblock in source._

## Code

```php
  function __construct($cid, $bin) {
    $this->cid = $cid;
    $this->bin = $bin;
    $this->persistable = module_load_all(NULL) && $_SERVER['REQUEST_METHOD'] == 'GET';

    $data = array();
    if ($this->persistable && $cached = cache_get($this->cid, $this->bin)) {
      $data = $cached->data;
    }
    else {
      // If there is no runtime cache stored, fetch the full theme registry,
      // but then initialize each value to NULL. This allows offsetExists()
      // to function correctly on non-registered theme hooks without triggering
      // a call to resolveCacheMiss().
      $data = $this->initializeRegistry();
      if ($this->persistable) {
        $this->set($data);
      }
    }
    $this->storage = $data;
  }
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

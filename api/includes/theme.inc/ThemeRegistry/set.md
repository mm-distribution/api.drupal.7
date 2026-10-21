# ThemeRegistry::set()

- **Type:** Method
- **File:** [`includes/theme.inc`](../_file.md), lines 447–464 · [local source](../../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L447-L464)
- **Class:** [ThemeRegistry](../ThemeRegistry.md)

## Signature

```php
public function set($data, $lock = TRUE)
```

## Documentation

_No docblock in source._

## Code

```php
  public function set($data, $lock = TRUE) {
    $lock_name = $this->cid . ':' . $this->bin;
    if (!$lock || lock_acquire($lock_name)) {
      if ($cached = cache_get($this->cid, $this->bin)) {
        // Use array merge instead of union so that filled in values in $data
        // overwrite empty values in the current cache.
        $data = array_merge($cached->data, $data);
      }
      else {
        $registry = $this->initializeRegistry();
        $data = array_merge($registry, $data);
      }
      cache_set($this->cid, $data, $this->bin);
      if ($lock) {
        lock_release($lock_name);
      }
    }
  }
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

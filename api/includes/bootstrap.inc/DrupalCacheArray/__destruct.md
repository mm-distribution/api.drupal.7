# DrupalCacheArray::__destruct()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 456–469 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L456-L469)
- **Class:** [DrupalCacheArray](../DrupalCacheArray.md)

## Signature

```php
public function __destruct()
```

## Documentation

```text
Destructs the DrupalCacheArray object.
```

## Code

```php
  public function __destruct() {
    if ($this->bin == 'cache_form' && !variable_get('drupal_cache_array_persist_cache_form', FALSE)) {
      return;
    }
    $data = array();
    foreach ($this->keysToPersist as $offset => $persist) {
      if ($persist) {
        $data[$offset] = $this->storage[$offset];
      }
    }
    if (!empty($data)) {
      $this->set($data);
    }
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

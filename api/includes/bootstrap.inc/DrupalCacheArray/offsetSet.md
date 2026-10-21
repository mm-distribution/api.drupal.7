# DrupalCacheArray::offsetSet()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 384–386 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L384-L386)
- **Class:** [DrupalCacheArray](../DrupalCacheArray.md)

## Signature

```php
public function offsetSet($offset, $value)
```

## Documentation

_No docblock in source._

## Code

```php
  public function offsetSet($offset, $value) {
    $this->storage[$offset] = $value;
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

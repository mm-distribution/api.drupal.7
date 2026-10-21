# DrupalCacheArray::persist()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 411–413 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L411-L413)
- **Class:** [DrupalCacheArray](../DrupalCacheArray.md)

## Signature

```php
protected function persist($offset, $persist = TRUE)
```

## Documentation

```text
Flags an offset value to be written to the persistent cache.

If a value is assigned to a cache object with offsetSet(), by default it
will not be written to the persistent cache unless it is flagged with this
method. This allows items to be cached for the duration of a request,
without necessarily writing back to the persistent cache at the end.

@param $offset
  The array offset that was requested.
@param $persist
  Optional boolean to specify whether the offset should be persisted or
  not, defaults to TRUE. When called with $persist = FALSE the offset will
  be unflagged so that it will not be written at the end of the request.
```

## Code

```php
  protected function persist($offset, $persist = TRUE) {
    $this->keysToPersist[$offset] = $persist;
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

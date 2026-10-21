# DrupalLocalStreamWrapper::stream_stat()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 541–543 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L541-L543)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_stat()
```

## Documentation

```text
Support for fstat().

@return
  An array with file status, or FALSE in case of an error - see fstat()
  for a description of this array.

@see http://php.net/manual/streamwrapper.stream-stat.php
```

## Code

```php
  public function stream_stat() {
    return fstat($this->handle);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

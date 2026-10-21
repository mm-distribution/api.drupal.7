# DrupalLocalStreamWrapper::stream_seek()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 502–506 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L502-L506)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_seek($offset, $whence)
```

## Documentation

```text
Support for fseek().

@param $offset
  The byte offset to got to.
@param $whence
  SEEK_SET, SEEK_CUR, or SEEK_END.

@return
  TRUE on success.

@see http://php.net/manual/streamwrapper.stream-seek.php
```

## Code

```php
  public function stream_seek($offset, $whence) {
    // fseek returns 0 on success and -1 on a failure.
    // stream_seek   1 on success and  0 on a failure.
    return !fseek($this->handle, $offset, $whence);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

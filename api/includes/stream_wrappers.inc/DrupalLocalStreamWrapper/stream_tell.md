# DrupalLocalStreamWrapper::stream_tell()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 528–530 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L528-L530)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_tell()
```

## Documentation

```text
Support for ftell().

@return
  The current offset in bytes from the beginning of file.

@see http://php.net/manual/streamwrapper.stream-tell.php
```

## Code

```php
  public function stream_tell() {
    return ftell($this->handle);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

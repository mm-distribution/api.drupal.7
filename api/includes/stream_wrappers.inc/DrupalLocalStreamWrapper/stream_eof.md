# DrupalLocalStreamWrapper::stream_eof()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 485–487 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L485-L487)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_eof()
```

## Documentation

```text
Support for feof().

@return
  TRUE if end-of-file has been reached.

@see http://php.net/manual/streamwrapper.stream-eof.php
```

## Code

```php
  public function stream_eof() {
    return feof($this->handle);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

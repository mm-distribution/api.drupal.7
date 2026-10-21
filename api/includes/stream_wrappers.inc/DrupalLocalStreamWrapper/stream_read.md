# DrupalLocalStreamWrapper::stream_read()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 458–460 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L458-L460)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_read($count)
```

## Documentation

```text
Support for fread(), file_get_contents() etc.

@param $count
  Maximum number of bytes to be read.

@return
  The string that was read, or FALSE in case of an error.

@see http://php.net/manual/streamwrapper.stream-read.php
```

## Code

```php
  public function stream_read($count) {
    return fread($this->handle, $count);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

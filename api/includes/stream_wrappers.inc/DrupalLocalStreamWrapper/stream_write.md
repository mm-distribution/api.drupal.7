# DrupalLocalStreamWrapper::stream_write()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 473–475 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L473-L475)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_write($data)
```

## Documentation

```text
Support for fwrite(), file_put_contents() etc.

@param $data
  The string to be written.

@return
  The number of bytes written (integer).

@see http://php.net/manual/streamwrapper.stream-write.php
```

## Code

```php
  public function stream_write($data) {
    return fwrite($this->handle, $data);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

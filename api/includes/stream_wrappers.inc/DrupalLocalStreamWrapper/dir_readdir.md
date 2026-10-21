# DrupalLocalStreamWrapper::dir_readdir()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 878–880 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L878-L880)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function dir_readdir()
```

## Documentation

```text
Support for readdir().

@return
  The next filename, or FALSE if there are no more files in the directory.

@see http://php.net/manual/streamwrapper.dir-readdir.php
```

## Code

```php
  public function dir_readdir() {
    return readdir($this->handle);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

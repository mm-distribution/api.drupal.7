# DrupalTemporaryStreamWrapper::getDirectoryPath()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 998–1000 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L998-L1000)
- **Class:** [DrupalTemporaryStreamWrapper](../DrupalTemporaryStreamWrapper.md)

## Signature

```php
public function getDirectoryPath()
```

## Documentation

```text
Implements abstract public function getDirectoryPath()
```

## Code

```php
  public function getDirectoryPath() {
    return variable_get('file_temporary_path', file_directory_temp());
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# DrupalPrivateStreamWrapper::getDirectoryPath()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 971–973 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L971-L973)
- **Class:** [DrupalPrivateStreamWrapper](../DrupalPrivateStreamWrapper.md)

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
    return variable_get('file_private_path', '');
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

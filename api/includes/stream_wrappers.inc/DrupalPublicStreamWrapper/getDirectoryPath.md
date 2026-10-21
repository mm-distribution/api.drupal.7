# DrupalPublicStreamWrapper::getDirectoryPath()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 924–926 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L924-L926)
- **Class:** [DrupalPublicStreamWrapper](../DrupalPublicStreamWrapper.md)

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
    return variable_get('file_public_path', conf_path() . '/files');
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

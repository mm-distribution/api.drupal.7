# Updater::getBackupDir()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 379–381 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L379-L381)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public function getBackupDir()
```

## Documentation

```text
Return the full path to a directory where backups should be written.
```

## Code

```php
  public function getBackupDir() {
    return file_stream_wrapper_get_instance_by_scheme('temporary')->getDirectoryPath();
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

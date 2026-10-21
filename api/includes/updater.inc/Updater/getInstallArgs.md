# Updater::getInstallArgs()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 209–216 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L209-L216)
- **Class:** [Updater](../Updater.md)

## Signature

```php
protected function getInstallArgs($overrides = array())
```

## Documentation

```text
Store the default parameters for the Updater.

@param array $overrides
  An array of overrides for the default parameters.

@return array
  An array of configuration parameters for an update or install operation.
```

## Code

```php
  protected function getInstallArgs($overrides = array()) {
    $args = array(
      'make_backup' => FALSE,
      'install_dir' => $this->getInstallDirectory(),
      'backup_dir'  => $this->getBackupDir(),
    );
    return array_merge($args, $overrides);
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

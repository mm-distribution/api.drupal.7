# Updater::factory()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 104–112 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L104-L112)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public static function factory($source)
```

## Documentation

```text
Return an Updater of the appropriate type depending on the source.

If a directory is provided which contains a module, will return a
ModuleUpdater.

@param string $source
  Directory of a Drupal project.

@return Updater
```

## Code

```php
  public static function factory($source) {
    if (is_dir($source)) {
      $updater = self::getUpdaterFromDirectory($source);
    }
    else {
      throw new UpdaterException(t('Unable to determine the type of the source directory.'));
    }
    return new $updater($source);
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

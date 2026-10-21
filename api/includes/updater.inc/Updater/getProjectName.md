# Updater::getProjectName()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 175–177 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L175-L177)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public static function getProjectName($directory)
```

## Documentation

```text
Get the name of the project directory (basename).

@todo: It would be nice, if projects contained an info file which could
       provide their canonical name.

@param string $directory

@return string
  The name of the project.
```

## Code

```php
  public static function getProjectName($directory) {
    return drupal_basename($directory);
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# DrupalUpdaterInterface::canUpdateDirectory()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 54–54 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L54)
- **Class:** [DrupalUpdaterInterface](../DrupalUpdaterInterface.md)

## Signature

```php
public static function canUpdateDirectory($directory);
```

## Documentation

```text
Determine if the Updater can handle the project provided in $directory.

@todo: Provide something more rational here, like a project spec file.

@param string $directory

@return bool
  TRUE if the project is installed, FALSE if not.
```

## Code

```php
  public static function canUpdateDirectory($directory);
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

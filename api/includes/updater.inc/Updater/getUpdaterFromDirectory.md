# Updater::getUpdaterFromDirectory()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 123–133 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L123-L133)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public static function getUpdaterFromDirectory($directory)
```

## Documentation

```text
Determine which Updater class can operate on the given directory.

@param string $directory
  Extracted Drupal project.

@return string
  The class name which can work with this project type.
```

## Code

```php
  public static function getUpdaterFromDirectory($directory) {
    // Gets a list of possible implementing classes.
    $updaters = drupal_get_updaters();
    foreach ($updaters as $updater) {
      $class = $updater['class'];
      if (call_user_func(array($class, 'canUpdateDirectory'), $directory)) {
        return $class;
      }
    }
    throw new UpdaterException(t('Cannot determine the type of project.'));
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

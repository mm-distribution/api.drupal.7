# Updater::getProjectTitle()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 188–198 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L188-L198)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public static function getProjectTitle($directory)
```

## Documentation

```text
Return the project name from a Drupal info file.

@param string $directory
  Directory to search for the info file.

@return string
  The title of the project.
```

## Code

```php
  public static function getProjectTitle($directory) {
    $info_file = self::findInfoFile($directory);
    $info = drupal_parse_info_file($info_file);
    if (empty($info)) {
      throw new UpdaterException(t('Unable to parse info file: %info_file.', array('%info_file' => $info_file)));
    }
    if (empty($info['name'])) {
      throw new UpdaterException(t("The info file (%info_file) does not define a 'name' attribute.", array('%info_file' => $info_file)));
    }
    return $info['name'];
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

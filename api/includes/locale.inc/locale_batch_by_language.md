# locale_batch_by_language()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2259–2280 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2259-L2280)
- **Topics:** [locale-autoimport](../../topics/locale-autoimport.md)

## Signature

```php
function locale_batch_by_language($langcode, $finished = NULL, $skip = array())
```

## Documentation

```text
Prepare a batch to import translations for all enabled
modules in a given language.

@param $langcode
  Language code to import translations for.
@param $finished
  Optional finished callback for the batch.
@param $skip
  Array of component names to skip. Used in the installer for the
  second pass import, when most components are already imported.

@return
  A batch structure or FALSE if no files found.
```

## Code

```php
function locale_batch_by_language($langcode, $finished = NULL, $skip = array()) {
  // Collect all files to import for all enabled modules and themes.
  $files = array();
  $components = array();
  $query = db_select('system', 's');
  $query->fields('s', array('name', 'filename'));
  $query->condition('s.status', 1);
  if (count($skip)) {
    $query->condition('name', $skip, 'NOT IN');
  }
  $result = $query->execute();
  foreach ($result as $component) {
    // Collect all files for all components, names as $langcode.po or
    // with names ending with $langcode.po. This allows for filenames
    // like node-module.de.po to let translators use small files and
    // be able to import in smaller chunks.
    $files = array_merge($files, file_scan_directory(dirname($component->filename) . '/translations', '/(^|\.)' . $langcode . '\.po$/', array('recurse' => FALSE)));
    $components[] = $component->name;
  }

  return _locale_batch_build($files, $finished, $components);
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

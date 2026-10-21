# locale_batch_by_component()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2294–2314 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2294-L2314)
- **Topics:** [locale-autoimport](../../topics/locale-autoimport.md)

## Signature

```php
function locale_batch_by_component($components, $finished = '_locale_batch_system_finished')
```

## Documentation

```text
Prepare a batch to run when installing modules or enabling themes.

This batch will import translations for the newly added components
in all the languages already set up on the site.

@param $components
  An array of component (theme and/or module) names to import
  translations for.
@param $finished
  Optional finished callback for the batch.
```

## Code

```php
function locale_batch_by_component($components, $finished = '_locale_batch_system_finished') {
  $files = array();
  $languages = language_list('enabled');
  unset($languages[1]['en']);
  if (count($languages[1])) {
    $language_list = join('|', array_keys($languages[1]));
    // Collect all files to import for all $components.
    $result = db_query("SELECT name, filename FROM {system} WHERE status = 1");
    foreach ($result as $component) {
      if (in_array($component->name, $components)) {
        // Collect all files for this component in all enabled languages, named
        // as $langcode.po or with names ending with $langcode.po. This allows
        // for filenames like node-module.de.po to let translators use small
        // files and be able to import in smaller chunks.
        $files = array_merge($files, file_scan_directory(dirname($component->filename) . '/translations', '/(^|\.)(' . $language_list . ')\.po$/', array('recurse' => FALSE)));
      }
    }
    return _locale_batch_build($files, $finished);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

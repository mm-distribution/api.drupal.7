# _locale_batch_build()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2329–2353 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2329-L2353)
- **Topics:** [locale-autoimport](../../topics/locale-autoimport.md)

## Signature

```php
function _locale_batch_build($files, $finished = NULL, $components = array())
```

## Documentation

```text
Build a locale batch from an array of files.

@param $files
  Array of files to import.
@param $finished
  Optional finished callback for the batch.
@param $components
  Optional list of component names the batch covers. Used in the installer.

@return
  A batch structure.
```

## Code

```php
function _locale_batch_build($files, $finished = NULL, $components = array()) {
  $t = get_t();
  if (count($files)) {
    $operations = array();
    foreach ($files as $file) {
      // We call _locale_batch_import for every batch operation.
      $operations[] = array('_locale_batch_import', array($file->uri));
    }
    $batch = array(
      'operations'    => $operations,
      'title'         => $t('Importing interface translations'),
      'init_message'  => $t('Starting import'),
      'error_message' => $t('Error importing interface translations'),
      'file'          => 'includes/locale.inc',
      // This is not a batch API construct, but data passed along to the
      // installer, so we know what did we import already.
      '#components'   => $components,
    );
    if (isset($finished)) {
      $batch['finished'] = $finished;
    }
    return $batch;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

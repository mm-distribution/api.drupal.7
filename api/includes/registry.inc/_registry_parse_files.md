# _registry_parse_files()

- **Type:** Function
- **File:** [`includes/registry.inc`](_file.md), lines 156–177 · [local source](../../../source/includes/registry.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc#L156-L177)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function _registry_parse_files($files)
```

## Documentation

```text
Parse all changed files and save their interface and class listings.

Parse all files that have changed since the registry was last built, and save
their interface and class listings.

@param $files
 The list of files to check and parse.
```

## Code

```php
function _registry_parse_files($files) {
  $parsed_files = array();
  foreach ($files as $filename => $file) {
    if (file_exists($filename)) {
      $hash = hash_file('sha256', $filename);
      if (empty($file['hash']) || $file['hash'] != $hash) {
        $file['hash'] = $hash;
        $parsed_files[$filename] = $file;
      }
    }
  }
  foreach ($parsed_files as $filename => $file) {
    _registry_parse_file($filename, file_get_contents($filename), $file['module'], $file['weight']);
    db_merge('registry_file')
      ->key(array('filename' => $filename))
      ->fields(array(
        'hash' => $file['hash'],
      ))
      ->execute();
  }
  return array_keys($parsed_files);
}
```

---
_Drupal 7.103 · [includes/registry.inc](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

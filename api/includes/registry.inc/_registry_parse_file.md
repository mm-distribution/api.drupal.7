# _registry_parse_file()

- **Type:** Function
- **File:** [`includes/registry.inc`](_file.md), lines 191–213 · [local source](../../../source/includes/registry.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc#L191-L213)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function _registry_parse_file($filename, $contents, $module = '', $weight = 0)
```

## Documentation

```text
Parse a file and save its interface and class listings.

@param $filename
  Name of the file we are going to parse.
@param $contents
  Contents of the file we are going to parse as a string.
@param $module
  (optional) Name of the module this file belongs to.
@param $weight
  (optional) Weight of the module.
```

## Code

```php
function _registry_parse_file($filename, $contents, $module = '', $weight = 0) {
  if (preg_match_all('/^\s*(?:abstract|final)?\s*(class|interface|trait)\s+([a-zA-Z0-9_]+)/m', $contents, $matches)) {
    foreach ($matches[2] as $key => $name) {
      db_merge('registry')
        ->key(array(
          'name' => $name,
          'type' => $matches[1][$key],
        ))
        ->fields(array(
          'filename' => $filename,
          'module' => $module,
          'weight' => $weight,
        ))
        ->execute();
    }
    // Delete any resources for this file where the name is not in the list
    // we just merged in.
    db_delete('registry')
      ->condition('filename', $filename)
      ->condition('name', $matches[2], 'NOT IN')
      ->execute();
  }
}
```

---
_Drupal 7.103 · [includes/registry.inc](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

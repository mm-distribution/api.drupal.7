# registry_get_parsed_files()

- **Type:** Function
- **File:** [`includes/registry.inc`](_file.md), lines 140–145 · [local source](../../../source/includes/registry.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc#L140-L145)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function registry_get_parsed_files()
```

## Documentation

```text
Return the list of files in registry_file
```

## Code

```php
function registry_get_parsed_files() {
  $files = array();
  // We want the result as a keyed array.
  $files = db_query("SELECT * FROM {registry_file}")->fetchAllAssoc('filename', PDO::FETCH_ASSOC);
  return $files;
}
```

---
_Drupal 7.103 · [includes/registry.inc](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

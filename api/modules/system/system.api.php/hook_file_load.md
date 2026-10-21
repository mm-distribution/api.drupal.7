# hook_file_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2838–2846 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2838-L2846)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_load($files)
```

## Documentation

```text
Load additional information into file objects.

file_load_multiple() calls this hook to allow modules to load
additional information into each file.

@param $files
  An array of file objects, indexed by fid.

@see file_load_multiple()
@see file_load()
```

## Code

```php
function hook_file_load($files) {
  // Add the upload specific data into the file object.
  $result = db_query('SELECT * FROM {upload} u WHERE u.fid IN (:fids)', array(':fids' => array_keys($files)))->fetchAll(PDO::FETCH_ASSOC);
  foreach ($result as $record) {
    foreach ($record as $key => $value) {
      $files[$record['fid']]->$key = $value;
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_load()".

- [entity_crud_hook_test_file_load()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_file_load.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [file_test_file_load()](../../simpletest/tests/file_test.module/file_test_file_load.md) — `modules/simpletest/tests/file_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

# file_test_file_mimetype_mapping_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 417–427 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L417-L427)
- **Module/theme:** batch_test
- **Implements:** [hook_file_mimetype_mapping_alter()](../../../system/system.api.php/hook_file_mimetype_mapping_alter.md)

## Signature

```php
function file_test_file_mimetype_mapping_alter(&$mapping)
```

## Documentation

```text
Implements hook_file_mimetype_mapping_alter().
```

## Code

```php
function file_test_file_mimetype_mapping_alter(&$mapping) {
  // Add new mappings.
  $mapping['mimetypes']['file_test_mimetype_1'] = 'madeup/file_test_1';
  $mapping['mimetypes']['file_test_mimetype_2'] = 'madeup/file_test_2';
  $mapping['mimetypes']['file_test_mimetype_3'] = 'madeup/doc';
  $mapping['extensions']['file_test_1'] = 'file_test_mimetype_1';
  $mapping['extensions']['file_test_2'] = 'file_test_mimetype_2';
  $mapping['extensions']['file_test_3'] = 'file_test_mimetype_2';
  // Override existing mapping.
  $mapping['extensions']['doc'] = 'file_test_mimetype_3';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

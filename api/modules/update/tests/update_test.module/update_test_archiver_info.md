# update_test_archiver_info()

- **Type:** Function
- **File:** [`modules/update/tests/update_test.module`](_file.md), lines 127–135 · [local source](../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L127-L135)
- **Module/theme:** aaa_update_test
- **Implements:** [hook_archiver_info()](../../../system/system.api.php/hook_archiver_info.md)

## Signature

```php
function update_test_archiver_info()
```

## Documentation

```text
Implements hook_archiver_info().
```

## Code

```php
function update_test_archiver_info() {
  return array(
    'update_test_archiver' => array(
      // This is bogus, we only care about the extensions for now.
      'class' => 'ArchiverUpdateTest',
      'extensions' => array('update-test-extension'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

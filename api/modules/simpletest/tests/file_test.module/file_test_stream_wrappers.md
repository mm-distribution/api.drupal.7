# file_test_stream_wrappers()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 33–46 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L33-L46)
- **Module/theme:** batch_test
- **Implements:** [hook_stream_wrappers()](../../../system/system.api.php/hook_stream_wrappers.md)

## Signature

```php
function file_test_stream_wrappers()
```

## Documentation

```text
Implements hook_stream_wrappers().
```

## Code

```php
function file_test_stream_wrappers() {
  return array(
    'dummy' => array(
      'name' => t('Dummy files'),
      'class' => 'DrupalDummyStreamWrapper',
      'description' => t('Dummy wrapper for simpletest.'),
    ),
    'dummy-remote' => array(
      'name' => t('Dummy files (remote)'),
      'class' => 'DrupalDummyRemoteStreamWrapper',
      'description' => t('Dummy wrapper for simpletest (remote).'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

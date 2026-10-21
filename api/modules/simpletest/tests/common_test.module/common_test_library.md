# common_test_library()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 257–270 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L257-L270)
- **Module/theme:** batch_test
- **Implements:** [hook_library()](../../../system/system.api.php/hook_library.md)

## Signature

```php
function common_test_library()
```

## Documentation

```text
Implements hook_library().

Adds Farbtastic in a different version.
```

## Code

```php
function common_test_library() {
  $libraries['farbtastic'] = array(
    'title' => 'Custom Farbtastic Library',
    'website' => 'http://code.google.com/p/farbtastic/',
    'version' => '5.3',
    'js' => array(
      'misc/farbtastic/farbtastic.js' => array(),
    ),
    'css' => array(
      'misc/farbtastic/farbtastic.css' => array(),
    ),
  );
  return $libraries;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

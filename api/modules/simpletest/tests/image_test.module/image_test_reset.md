# image_test_reset()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 29–41 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L29-L41)
- **Module/theme:** batch_test

## Signature

```php
function image_test_reset()
```

## Documentation

```text
Reset/initialize the history of calls to the toolkit functions.

@see image_test_get_all_calls()
```

## Code

```php
function image_test_reset() {
  // Keep track of calls to these operations
  $results = array(
    'load' => array(),
    'save' => array(),
    'settings' => array(),
    'resize' => array(),
    'rotate' => array(),
    'crop' => array(),
    'desaturate' => array(),
  );
  variable_set('image_test_results', $results);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# common_test_theme()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 225–231 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L225-L231)
- **Module/theme:** batch_test
- **Implements:** [hook_theme()](../../../system/system.api.php/hook_theme.md)

## Signature

```php
function common_test_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function common_test_theme() {
  return array(
    'common_test_foo' => array(
      'variables' => array('foo' => 'foo', 'bar' => 'bar'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

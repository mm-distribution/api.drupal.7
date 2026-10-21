# menu_test_static_variable()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 528–534 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L528-L534)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_static_variable($value = NULL)
```

## Documentation

```text
Static function for testing hook results.

@param $value
  The value to set or NULL to return the current value.
@return
  A text string for comparison to test assertions.
```

## Code

```php
function menu_test_static_variable($value = NULL) {
  static $variable;
  if (!empty($value)) {
    $variable = $value;
  }
  return $variable;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

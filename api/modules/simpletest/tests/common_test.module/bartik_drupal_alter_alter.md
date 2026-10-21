# bartik_drupal_alter_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 166–192 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L166-L192)
- **Module/theme:** batch_test

## Signature

```php
function bartik_drupal_alter_alter(&$data, &$arg2 = NULL, &$arg3 = NULL)
```

## Documentation

```text
Implements hook_TYPE_alter() on behalf of Bartik theme.

Same as common_test_drupal_alter_alter(), but here, we verify that themes
can also alter and come last.
```

## Code

```php
function bartik_drupal_alter_alter(&$data, &$arg2 = NULL, &$arg3 = NULL) {
  // Alter first argument.
  if (is_array($data)) {
    $data['foo'] .= ' theme';
  }
  elseif (is_object($data)) {
    $data->foo .= ' theme';
  }
  // Alter second argument, if present.
  if (isset($arg2)) {
    if (is_array($arg2)) {
      $arg2['foo'] .= ' theme';
    }
    elseif (is_object($arg2)) {
      $arg2->foo .= ' theme';
    }
  }
  // Try to alter third argument, if present.
  if (isset($arg3)) {
    if (is_array($arg3)) {
      $arg3['foo'] .= ' theme';
    }
    elseif (is_object($arg3)) {
      $arg3->foo .= ' theme';
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

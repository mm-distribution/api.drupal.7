# block_drupal_alter_foo_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 201–203 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L201-L203)
- **Module/theme:** batch_test

## Signature

```php
function block_drupal_alter_foo_alter(&$data, &$arg2 = NULL, &$arg3 = NULL)
```

## Documentation

```text
Implements hook_TYPE_alter() on behalf of block module.

This is for verifying that drupal_alter(array(TYPE1, TYPE2), ...) allows
hook_module_implements_alter() to affect the order in which module
implementations are executed.
```

## Code

```php
function block_drupal_alter_foo_alter(&$data, &$arg2 = NULL, &$arg3 = NULL) {
  $data['foo'] .= ' block';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

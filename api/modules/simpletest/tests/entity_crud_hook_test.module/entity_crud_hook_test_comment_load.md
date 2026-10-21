# entity_crud_hook_test_comment_load()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 116–118 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L116-L118)
- **Module/theme:** batch_test
- **Implements:** [hook_comment_load()](../../../comment/comment.api.php/hook_comment_load.md)

## Signature

```php
function entity_crud_hook_test_comment_load()
```

## Documentation

```text
Implements hook_comment_load().
```

## Code

```php
function entity_crud_hook_test_comment_load() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# entity_crud_hook_test_comment_presave()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 18–20 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L18-L20)
- **Module/theme:** batch_test
- **Implements:** [hook_comment_presave()](../../../comment/comment.api.php/hook_comment_presave.md)

## Signature

```php
function entity_crud_hook_test_comment_presave()
```

## Documentation

```text
Implements hook_comment_presave().
```

## Code

```php
function entity_crud_hook_test_comment_presave() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

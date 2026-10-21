# comment_hook_test_comment_publish()

- **Type:** Function
- **File:** [`modules/comment/tests/comment_hook_test.module`](_file.md), lines 11–13 · [local source](../../../../../source/modules/comment/tests/comment_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/tests/comment_hook_test.module#L11-L13)
- **Module/theme:** comment_hook_test
- **Implements:** [hook_comment_publish()](../../comment.api.php/hook_comment_publish.md)

## Signature

```php
function comment_hook_test_comment_publish($comment)
```

## Documentation

```text
Implements hook_comment_publish().
```

## Code

```php
function comment_hook_test_comment_publish($comment) {
  $_SESSION['comment_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/comment/tests/comment_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/tests/comment_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

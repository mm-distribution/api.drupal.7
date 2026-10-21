# poll_delete()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 615–625 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L615-L625)
- **Module/theme:** poll
- **Implements:** [hook_delete()](../../node/node.api.php/hook_delete.md)

## Signature

```php
function poll_delete($node)
```

## Documentation

```text
Implements hook_delete().
```

## Code

```php
function poll_delete($node) {
  db_delete('poll')
    ->condition('nid', $node->nid)
    ->execute();
  db_delete('poll_choice')
    ->condition('nid', $node->nid)
    ->execute();
  db_delete('poll_vote')
    ->condition('nid', $node->nid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# poll_update()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 570–610 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L570-L610)
- **Module/theme:** poll
- **Implements:** [hook_update()](../../node/node.api.php/hook_update.md)

## Signature

```php
function poll_update($node)
```

## Documentation

```text
Implements hook_update().
```

## Code

```php
function poll_update($node) {
  // Update poll settings.
  db_update('poll')
    ->fields(array(
      'runtime' => $node->runtime,
      'active' => $node->active,
    ))
    ->condition('nid', $node->nid)
    ->execute();

  // Poll choices with empty titles signifies removal. We remove all votes to
  // the removed options, so people who voted on them can vote again.
  foreach ($node->choice as $key => $choice) {
    if (!empty($choice['chtext'])) {
      db_merge('poll_choice')
        ->key(array('chid' => $choice['chid']))
        ->fields(array(
          'chtext' => $choice['chtext'],
          'chvotes' => (int) $choice['chvotes'],
          'weight' => $choice['weight'],
        ))
        ->insertFields(array(
          'nid' => $node->nid,
          'chtext' => $choice['chtext'],
          'chvotes' => (int) $choice['chvotes'],
          'weight' => $choice['weight'],
        ))
        ->execute();
    }
    else {
      db_delete('poll_vote')
        ->condition('nid', $node->nid)
        ->condition('chid', $key)
        ->execute();
      db_delete('poll_choice')
        ->condition('nid', $node->nid)
        ->condition('chid', $choice['chid'])
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._

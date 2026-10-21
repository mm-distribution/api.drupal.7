# poll_insert()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 536–565 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L536-L565)
- **Module/theme:** poll
- **Implements:** [hook_insert()](../../node/node.api.php/hook_insert.md)

## Signature

```php
function poll_insert($node)
```

## Documentation

```text
Implements hook_insert().
```

## Code

```php
function poll_insert($node) {
  if (!user_access('administer nodes')) {
    // Make sure all votes are 0 initially
    foreach ($node->choice as $i => $choice) {
      $node->choice[$i]['chvotes'] = 0;
    }
    $node->active = 1;
  }

  db_insert('poll')
    ->fields(array(
      'nid' => $node->nid,
      'runtime' => $node->runtime,
      'active' => $node->active,
    ))
    ->execute();

  foreach ($node->choice as $choice) {
    if ($choice['chtext'] != '') {
      db_insert('poll_choice')
        ->fields(array(
          'nid' => $node->nid,
          'chtext' => $choice['chtext'],
          'chvotes' => $choice['chvotes'],
          'weight' => $choice['weight'],
        ))
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._

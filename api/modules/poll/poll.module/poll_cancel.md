# poll_cancel()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 955–973 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L955-L973)
- **Module/theme:** poll

## Signature

```php
function poll_cancel($form, &$form_state)
```

## Documentation

```text
Submit callback for poll_cancel_form().
```

## Code

```php
function poll_cancel($form, &$form_state) {
  global $user;
  $node = node_load($form['#nid']);

  db_delete('poll_vote')
    ->condition('nid', $node->nid)
    ->condition($user->uid ? 'uid' : 'hostname', $user->uid ? $user->uid : ip_address())
    ->execute();

  // Subtract from the votes.
  db_update('poll_choice')
    ->expression('chvotes', 'chvotes - 1')
    ->condition('chid', $node->vote)
    ->execute();

  unset($_SESSION['poll_vote'][$node->nid]);

  drupal_set_message(t('Your vote was cancelled.'));
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._

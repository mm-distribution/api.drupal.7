# poll_vote()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 752–787 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L752-L787)
- **Module/theme:** poll

## Signature

```php
function poll_vote($form, &$form_state)
```

## Documentation

```text
Submit handler for processing a vote.
```

## Code

```php
function poll_vote($form, &$form_state) {
  $node = $form['#node'];
  $choice = $form_state['values']['choice'];

  global $user;
  db_insert('poll_vote')
    ->fields(array(
      'nid' => $node->nid,
      'chid' => $choice,
      'uid' => $user->uid,
      'hostname' => ip_address(),
      'timestamp' => REQUEST_TIME,
    ))
    ->execute();

  // Add one to the votes.
  db_update('poll_choice')
    ->expression('chvotes', 'chvotes + 1')
    ->condition('chid', $choice)
    ->execute();

  cache_clear_all();

  if (!$user->uid) {
    // The vote is recorded so the user gets the result view instead of the
    // voting form when viewing the poll. Saving a value in $_SESSION has the
    // convenient side effect of preventing the user from hitting the page
    // cache. When anonymous voting is allowed, the page cache should only
    // contain the voting form, not the results.
    $_SESSION['poll_vote'][$node->nid] = $choice;
  }

  drupal_set_message(t('Your vote was recorded.'));

  // Return the user to whatever page they voted from.
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._

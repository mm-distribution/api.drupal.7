# poll_load()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 488–531 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L488-L531)
- **Module/theme:** poll
- **Implements:** [hook_load()](../../node/node.api.php/hook_load.md)

## Signature

```php
function poll_load($nodes)
```

## Documentation

```text
Implements hook_load().
```

## Code

```php
function poll_load($nodes) {
  global $user;
  foreach ($nodes as $node) {
    $poll = db_query("SELECT runtime, active FROM {poll} WHERE nid = :nid", array(':nid' => $node->nid))->fetchObject();

    if (empty($poll)) {
      $poll = new stdClass();
    }

    // Load the appropriate choices into the $poll object.
    $poll->choice = db_select('poll_choice', 'c')
      ->addTag('translatable')
      ->fields('c', array('chid', 'chtext', 'chvotes', 'weight'))
      ->condition('c.nid', $node->nid)
      ->orderBy('weight')
      ->execute()->fetchAllAssoc('chid', PDO::FETCH_ASSOC);

    // Determine whether or not this user is allowed to vote.
    $poll->allowvotes = FALSE;
    if (user_access('vote on polls') && $poll->active) {
      if ($user->uid) {
        // If authenticated, find existing vote based on uid.
        $poll->vote = db_query('SELECT chid FROM {poll_vote} WHERE nid = :nid AND uid = :uid', array(':nid' => $node->nid, ':uid' => $user->uid))->fetchField();
        if (empty($poll->vote)) {
          $poll->vote = -1;
          $poll->allowvotes = TRUE;
        }
      }
      elseif (!empty($_SESSION['poll_vote'][$node->nid])) {
        // Otherwise the user is anonymous. Look for an existing vote in the
        // user's session.
        $poll->vote = $_SESSION['poll_vote'][$node->nid];
      }
      else {
        // Finally, query the database for an existing vote based on anonymous
        // user's hostname.
        $poll->allowvotes = !db_query("SELECT 1 FROM {poll_vote} WHERE nid = :nid AND hostname = :hostname AND uid = 0", array(':nid' => $node->nid, ':hostname' => ip_address()))->fetchField();
      }
    }
    foreach ($poll as $key => $value) {
      $nodes[$node->nid]->$key = $value;
    }
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._

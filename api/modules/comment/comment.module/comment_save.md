# comment_save()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1465–1613 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1465-L1613)
- **Module/theme:** comment

## Signature

```php
function comment_save($comment)
```

## Documentation

```text
Accepts a submission of new or changed comment content.

@param $comment
  A comment object.
```

## Code

```php
function comment_save($comment) {
  global $user;

  $transaction = db_transaction();
  try {
    $defaults = array(
      'mail' => '',
      'homepage' => '',
      'name' => '',
      'status' => user_access('skip comment approval') ? COMMENT_PUBLISHED : COMMENT_NOT_PUBLISHED,
    );
    foreach ($defaults as $key => $default) {
      if (!isset($comment->$key)) {
        $comment->$key = $default;
      }
    }
    // Make sure we have a bundle name.
    if (!isset($comment->node_type)) {
      $node = node_load($comment->nid);
      $comment->node_type = 'comment_node_' . $node->type;
    }

    // Load the stored entity, if any.
    if (!empty($comment->cid) && !isset($comment->original)) {
      $comment->original = entity_load_unchanged('comment', $comment->cid);
    }

    field_attach_presave('comment', $comment);

    // Allow modules to alter the comment before saving.
    module_invoke_all('comment_presave', $comment);
    module_invoke_all('entity_presave', $comment, 'comment');

    if ($comment->cid) {

      drupal_write_record('comment', $comment, 'cid');

      // Ignore slave server temporarily to give time for the
      // saved comment to be propagated to the slave.
      db_ignore_slave();

      // Update the {node_comment_statistics} table prior to executing hooks.
      _comment_update_node_statistics($comment->nid);

      field_attach_update('comment', $comment);
      // Allow modules to respond to the updating of a comment.
      module_invoke_all('comment_update', $comment);
      module_invoke_all('entity_update', $comment, 'comment');
    }
    else {
      // Add the comment to database. This next section builds the thread field.
      // Also see the documentation for comment_view().
      if (!empty($comment->thread)) {
        // Allow calling code to set thread itself.
        $thread = $comment->thread;
      }
      elseif ($comment->pid == 0) {
        // This is a comment with no parent comment (depth 0): we start
        // by retrieving the maximum thread level.
        $max = db_query('SELECT MAX(thread) FROM {comment} WHERE nid = :nid', array(':nid' => $comment->nid))->fetchField();
        // Strip the "/" from the end of the thread.
        $max = rtrim((string) $max, '/');
        // We need to get the value at the correct depth.
        $parts = explode('.', $max);
        $firstsegment = $parts[0];
        // Finally, build the thread field for this new comment.
        $thread = int2vancode(vancode2int($firstsegment) + 1) . '/';
      }
      else {
        // This is a comment with a parent comment, so increase the part of the
        // thread value at the proper depth.

        // Get the parent comment:
        $parent = comment_load($comment->pid);
        // Strip the "/" from the end of the parent thread.
        $parent->thread = (string) rtrim((string) $parent->thread, '/');
        // Get the max value in *this* thread.
        $max = db_query("SELECT MAX(thread) FROM {comment} WHERE thread LIKE :thread AND nid = :nid", array(
          ':thread' => $parent->thread . '.%',
          ':nid' => $comment->nid,
        ))->fetchField();

        if ($max == '') {
          // First child of this parent.
          $thread = $parent->thread . '.' . int2vancode(0) . '/';
        }
        else {
          // Strip the "/" at the end of the thread.
          $max = rtrim($max, '/');
          // Get the value at the correct depth.
          $parts = explode('.', $max);
          $parent_depth = count(explode('.', $parent->thread));
          $last = $parts[$parent_depth];
          // Finally, build the thread field for this new comment.
          $thread = $parent->thread . '.' . int2vancode(vancode2int($last) + 1) . '/';
        }
      }

      if (empty($comment->created)) {
        $comment->created = REQUEST_TIME;
      }

      if (empty($comment->changed)) {
        $comment->changed = $comment->created;
      }

      if ($comment->uid === $user->uid && isset($user->name)) { // '===' Need to modify anonymous users as well.
        $comment->name = $user->name;
      }

      // Ensure the parent id (pid) has a value set.
      if (empty($comment->pid)) {
        $comment->pid = 0;
      }

      // Add the values which aren't passed into the function.
      $comment->thread = $thread;
      $comment->hostname = ip_address();

      drupal_write_record('comment', $comment);

      // Ignore slave server temporarily to give time for the
      // created comment to be propagated to the slave.
      db_ignore_slave();

      // Update the {node_comment_statistics} table prior to executing hooks.
      _comment_update_node_statistics($comment->nid);

      field_attach_insert('comment', $comment);

      // Tell the other modules a new comment has been submitted.
      module_invoke_all('comment_insert', $comment);
      module_invoke_all('entity_insert', $comment, 'comment');
    }
    if ($comment->status == COMMENT_PUBLISHED) {
      module_invoke_all('comment_publish', $comment);
    }
    elseif ($comment->status == COMMENT_NOT_PUBLISHED) {
      module_invoke_all('comment_unpublish', $comment);
    }
    unset($comment->original);
  }
  catch (Exception $e) {
    $transaction->rollback('comment');
    watchdog_exception('comment', $e);
    throw $e;
  }

}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# forum_get_topics()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 914–1020 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L914-L1020)
- **Module/theme:** forum

## Signature

```php
function forum_get_topics($tid, $sortby, $forum_per_page)
```

## Documentation

```text
Gets all the topics in a forum.

@param $tid
  The term ID of the forum.
@param $sortby
  One of the following integers indicating the sort criteria:
  - 1: Date - newest first.
  - 2: Date - oldest first.
  - 3: Posts with the most comments first.
  - 4: Posts with the least comments first.
@param $forum_per_page
  The maximum number of topics to display per page.

@return
  A list of all the topics in a forum.
```

## Code

```php
function forum_get_topics($tid, $sortby, $forum_per_page) {
  global $user, $forum_topic_list_header;

  $forum_topic_list_header = array(
    NULL,
    array('data' => t('Topic'), 'field' => 'f.title'),
    array('data' => t('Replies'), 'field' => 'f.comment_count'),
    array('data' => t('Last reply'), 'field' => 'f.last_comment_timestamp'),
  );

  $order = _forum_get_topic_order($sortby);
  // Skip element with index 0 which is NULL.
  for ($i = 1; $i < count($forum_topic_list_header); $i++) {
    if ($forum_topic_list_header[$i]['field'] == $order['field']) {
      $forum_topic_list_header[$i]['sort'] = $order['sort'];
    }
  }

  $query = db_select('forum_index', 'f')->extend('PagerDefault')->extend('TableSort');
  $query->fields('f');
  $query
    ->condition('f.tid', $tid)
    ->addTag('node_access')
    ->orderBy('f.sticky', 'DESC')
    ->orderByHeader($forum_topic_list_header)
    ->limit($forum_per_page);

  $count_query = db_select('forum_index', 'f');
  $count_query->condition('f.tid', $tid);
  $count_query->addExpression('COUNT(*)');
  $count_query->addTag('node_access');

  $query->setCountQuery($count_query);
  $result = $query->execute();
  $nids = array();
  foreach ($result as $record) {
    $nids[] = $record->nid;
  }
  if ($nids) {
    $query = db_select('node', 'n')->extend('TableSort');
    $query->fields('n', array('title', 'nid', 'type', 'sticky', 'created', 'uid'));
    $query->addField('n', 'comment', 'comment_mode');

    $query->join('node_comment_statistics', 'ncs', 'n.nid = ncs.nid');
    $query->fields('ncs', array('cid', 'last_comment_uid', 'last_comment_timestamp', 'comment_count'));

    $query->join('forum_index', 'f', 'f.nid = ncs.nid');
    $query->addField('f', 'tid', 'forum_tid');

    $query->join('users', 'u', 'n.uid = u.uid');
    $query->addField('u', 'name');

    $query->join('users', 'u2', 'ncs.last_comment_uid = u2.uid');

    $query->addExpression('CASE ncs.last_comment_uid WHEN 0 THEN ncs.last_comment_name ELSE u2.name END', 'last_comment_name');

    $query
      ->orderBy('f.sticky', 'DESC')
      ->orderByHeader($forum_topic_list_header)
      ->condition('n.nid', $nids);

    $result = $query->execute();
  }
  else {
    $result = array();
  }

  $topics = array();
  $first_new_found = FALSE;
  foreach ($result as $topic) {
    if ($user->uid) {
      // A forum is new if the topic is new, or if there are new comments since
      // the user's last visit.
      if ($topic->forum_tid != $tid) {
        $topic->new = 0;
      }
      else {
        $history = _forum_user_last_visit($topic->nid);
        $topic->new_replies = comment_num_new($topic->nid, $history);
        $topic->new = $topic->new_replies || ($topic->last_comment_timestamp > $history);
      }
    }
    else {
      // Do not track "new replies" status for topics if the user is anonymous.
      $topic->new_replies = 0;
      $topic->new = 0;
    }

    // Make sure only one topic is indicated as the first new topic.
    $topic->first_new = FALSE;
    if ($topic->new != 0 && !$first_new_found) {
      $topic->first_new = TRUE;
      $first_new_found = TRUE;
    }

    if ($topic->comment_count > 0) {
      $last_reply = new stdClass();
      $last_reply->created = $topic->last_comment_timestamp;
      $last_reply->name = $topic->last_comment_name;
      $last_reply->uid = $topic->last_comment_uid;
      $topic->last_reply = $last_reply;
    }
    $topics[] = $topic;
  }

  return $topics;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# forum_forum_load()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 765–868 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L765-L868)
- **Module/theme:** forum

## Signature

```php
function forum_forum_load($tid = NULL)
```

## Documentation

```text
Returns a tree of all forums for a given taxonomy term ID.

@param $tid
  (optional) Taxonomy term ID of the forum. If not given all forums will be
  returned.

@return
  A tree of taxonomy objects, with the following additional properties:
  - num_topics: Number of topics in the forum.
  - num_posts: Total number of posts in all topics.
  - last_post: Most recent post for the forum.
  - forums: An array of child forums.
```

## Code

```php
function forum_forum_load($tid = NULL) {
  $cache = &drupal_static(__FUNCTION__, array());

  // Return a cached forum tree if available.
  if (!isset($tid)) {
    $tid = 0;
  }
  if (isset($cache[$tid])) {
    return $cache[$tid];
  }

  $vid = variable_get('forum_nav_vocabulary', 0);

  // Load and validate the parent term.
  if ($tid) {
    $forum_term = taxonomy_term_load($tid);
    if (!$forum_term || ($forum_term->vid != $vid)) {
      return $cache[$tid] = FALSE;
    }
  }
  // If $tid is 0, create an empty object to hold the child terms.
  elseif ($tid === 0) {
    $forum_term = (object) array(
      'tid' => 0,
    );
  }

  // Determine if the requested term is a container.
  if (!$forum_term->tid || in_array($forum_term->tid, variable_get('forum_containers', array()))) {
    $forum_term->container = 1;
  }

  // Load parent terms.
  $forum_term->parents = taxonomy_get_parents_all($forum_term->tid);

  // Load the tree below.
  $forums = array();
  $_forums = taxonomy_get_tree($vid, $tid);

  if (count($_forums)) {
    $query = db_select('node', 'n');
    $query->join('node_comment_statistics', 'ncs', 'n.nid = ncs.nid');
    $query->join('forum', 'f', 'n.vid = f.vid');
    $query->addExpression('COUNT(n.nid)', 'topic_count');
    $query->addExpression('SUM(ncs.comment_count)', 'comment_count');
    $counts = $query
      ->fields('f', array('tid'))
      ->condition('n.status', 1)
      ->groupBy('tid')
      ->addTag('node_access')
      ->execute()
      ->fetchAllAssoc('tid');
  }

  foreach ($_forums as $forum) {
    // Determine if the child term is a container.
    if (in_array($forum->tid, variable_get('forum_containers', array()))) {
      $forum->container = 1;
    }

    // Merge in the topic and post counters.
    if (!empty($counts[$forum->tid])) {
      $forum->num_topics = $counts[$forum->tid]->topic_count;
      $forum->num_posts = $counts[$forum->tid]->topic_count + $counts[$forum->tid]->comment_count;
    }
    else {
      $forum->num_topics = 0;
      $forum->num_posts = 0;
    }

    // Query "Last Post" information for this forum.
    $query = db_select('node', 'n');
    $query->join('users', 'u1', 'n.uid = u1.uid');
    $query->join('forum', 'f', 'n.vid = f.vid AND f.tid = :tid', array(':tid' => $forum->tid));
    $query->join('node_comment_statistics', 'ncs', 'n.nid = ncs.nid');
    $query->join('users', 'u2', 'ncs.last_comment_uid = u2.uid');
    $query->addExpression('CASE ncs.last_comment_uid WHEN 0 THEN ncs.last_comment_name ELSE u2.name END', 'last_comment_name');

    $topic = $query
      ->fields('ncs', array('last_comment_timestamp', 'last_comment_uid'))
      ->condition('n.status', 1)
      ->orderBy('last_comment_timestamp', 'DESC')
      ->range(0, 1)
      ->addTag('node_access')
      ->execute()
      ->fetchObject();

    // Merge in the "Last Post" information.
    $last_post = new stdClass();
    if (!empty($topic->last_comment_timestamp)) {
      $last_post->created = $topic->last_comment_timestamp;
      $last_post->name = $topic->last_comment_name;
      $last_post->uid = $topic->last_comment_uid;
    }
    $forum->last_post = $last_post;

    $forums[$forum->tid] = $forum;
  }

  // Cache the result, and return the tree.
  $forum_term->forums = $forums;
  $cache[$tid] = $forum_term;
  return $forum_term;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._

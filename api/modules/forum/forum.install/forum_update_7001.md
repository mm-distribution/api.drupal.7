# forum_update_7001()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 269–352 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L269-L352)
- **Module/theme:** forum

## Signature

```php
function forum_update_7001()
```

## Documentation

```text
Create new {forum_index} table.
```

## Code

```php
function forum_update_7001() {
  $forum_index = array(
    'description' => 'Maintains denormalized information about node/term relationships.',
    'fields' => array(
      'nid' => array(
        'description' => 'The {node}.nid this record tracks.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'title' => array(
        'description' => 'The title of this node, always treated as non-markup plain text.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
      'tid' => array(
         'description' => 'The term ID.',
         'type' => 'int',
         'unsigned' => TRUE,
         'not null' => TRUE,
         'default' => 0,
      ),
      'sticky' => array(
        'description' => 'Boolean indicating whether the node is sticky.',
        'type' => 'int',
        'not null' => FALSE,
        'default' => 0,
        'size' => 'tiny',
      ),
      'created' => array(
        'description' => 'The Unix timestamp when the node was created.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default'=> 0,
      ),
      'last_comment_timestamp' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The Unix timestamp of the last comment that was posted within this node, from {comment}.timestamp.',
      ),
      'comment_count' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The total number of comments on this node.',
      ),
    ),
    'indexes' => array(
      'forum_topics' => array('tid', 'sticky', 'last_comment_timestamp'),
    ),
    'foreign keys' => array(
      'tracked_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
      'term' => array(
        'table' => 'taxonomy_term_data',
        'columns' => array(
          'tid' => 'tid',
        ),
      ),
    ),
  );
  db_create_table('forum_index', $forum_index);

  $select = db_select('node', 'n');
  $forum_alias = $select->join('forum', 'f', 'n.vid = f.vid');
  $ncs_alias = $select->join('node_comment_statistics', 'ncs', 'n.nid = ncs.nid');
  $select
    ->fields('n', array('nid', 'title', 'sticky', 'created'))
    ->fields($forum_alias, array('tid'))
    ->fields($ncs_alias, array('last_comment_timestamp', 'comment_count'));

  db_insert('forum_index')
    ->fields(array('nid', 'title', 'sticky', 'created', 'tid', 'last_comment_timestamp', 'comment_count'))
    ->from($select)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._

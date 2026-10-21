# comment_schema()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 399–575 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L399-L575)
- **Module/theme:** comment
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function comment_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function comment_schema() {
  $schema['comment'] = array(
    'description' => 'Stores comments and associated data.',
    'fields' => array(
      'cid' => array(
        'type' => 'serial',
        'not null' => TRUE,
        'description' => 'Primary Key: Unique comment ID.',
      ),
      'pid' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {comment}.cid to which this comment is a reply. If set to 0, this comment is not a reply to an existing comment.',
      ),
      'nid' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {node}.nid to which this comment is a reply.',
      ),
      'uid' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {users}.uid who authored the comment. If set to 0, this comment was created by an anonymous user.',
      ),
      'subject' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The comment title.',
      ),
      'hostname' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => "The author's host name.",
      ),
      'created' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The time that the comment was created, as a Unix timestamp.',
      ),
      'changed' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The time that the comment was last edited, as a Unix timestamp.',
      ),
      'status' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 1,
        'size' => 'tiny',
        'description' => 'The published status of a comment. (0 = Not Published, 1 = Published)',
      ),
      'thread' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'description' => "The vancode representation of the comment's place in a thread.",
      ),
      'name' => array(
        'type' => 'varchar',
        'length' => 60,
        'not null' => FALSE,
        'description' => "The comment author's name. Uses {users}.name if the user is logged in, otherwise uses the value typed into the comment form.",
      ),
      'mail' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => FALSE,
        'description' => "The comment author's e-mail address from the comment form, if user is anonymous, and the 'Anonymous users may/must leave their contact information' setting is turned on.",
      ),
      'homepage' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => FALSE,
        'description' => "The comment author's home page address from the comment form, if user is anonymous, and the 'Anonymous users may/must leave their contact information' setting is turned on.",
      ),
      'language' => array(
        'description' => 'The {languages}.language of this comment.',
        'type' => 'varchar',
        'length' => 12,
        'not null' => TRUE,
        'default' => '',
      ),
    ),
    'indexes' => array(
      'comment_status_pid' => array('pid', 'status'),
      'comment_num_new' => array('nid', 'status', 'created', 'cid', 'thread'),
      'comment_uid' => array('uid'),
      'comment_nid_language' => array('nid', 'language'),
      'comment_created' => array('created'),
    ),
    'primary key' => array('cid'),
    'foreign keys' => array(
      'comment_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
      'comment_author' => array(
        'table' => 'users',
        'columns' => array('uid' => 'uid'),
      ),
    ),
  );

  $schema['node_comment_statistics'] = array(
    'description' => 'Maintains statistics of node and comments posts to show "new" and "updated" flags.',
    'fields' => array(
      'nid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {node}.nid for which the statistics are compiled.',
      ),
      'cid' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {comment}.cid of the last comment.',
      ),
      'last_comment_timestamp' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The Unix timestamp of the last comment that was posted within this node, from {comment}.changed.',
      ),
      'last_comment_name' => array(
        'type' => 'varchar',
        'length' => 60,
        'not null' => FALSE,
        'description' => 'The name of the latest author to post a comment on this node, from {comment}.name.',
      ),
      'last_comment_uid' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The user ID of the latest author to post a comment on this node, from {comment}.uid.',
      ),
      'comment_count' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The total number of comments on this node.',
      ),
    ),
    'primary key' => array('nid'),
    'indexes' => array(
      'node_comment_timestamp' => array('last_comment_timestamp'),
      'comment_count' => array('comment_count'),
      'last_comment_uid' => array('last_comment_uid'),
    ),
    'foreign keys' => array(
      'statistics_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
      'last_comment_author' => array(
        'table' => 'users',
        'columns' => array(
          'last_comment_uid' => 'uid',
        ),
      ),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._

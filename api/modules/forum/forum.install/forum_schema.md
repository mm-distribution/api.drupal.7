# forum_schema()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 126–241 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L126-L241)
- **Module/theme:** forum
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function forum_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function forum_schema() {
  $schema['forum'] = array(
    'description' => 'Stores the relationship of nodes to forum terms.',
    'fields' => array(
      'nid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {node}.nid of the node.',
      ),
      'vid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Primary Key: The {node}.vid of the node.',
      ),
      'tid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {taxonomy_term_data}.tid of the forum term assigned to the node.',
      ),
    ),
    'indexes' => array(
      'forum_topic' => array('nid', 'tid'),
      'tid' => array('tid'),
    ),
    'primary key' => array('vid'),
    'foreign keys' => array(
      'forum_node' => array(
        'table' => 'node',
        'columns' => array(
          'nid' => 'nid',
          'vid' => 'vid',
        ),
      ),
    ),
  );

  $schema['forum_index'] = array(
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
      'forum_topics' => array('nid', 'tid', 'sticky', 'last_comment_timestamp'),
      'created' => array('created'),
      'last_comment_timestamp' => array('last_comment_timestamp'),
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


  return $schema;
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._

# poll_schema()

- **Type:** Function
- **File:** [`modules/poll/poll.install`](_file.md), lines 11–149 · [local source](../../../../source/modules/poll/poll.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install#L11-L149)
- **Module/theme:** poll
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function poll_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function poll_schema() {
  $schema['poll'] = array(
    'description' => 'Stores poll-specific information for poll nodes.',
    'fields' => array(
      'nid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => "The poll's {node}.nid.",
      ),
      'runtime' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The number of seconds past {node}.created during which the poll is open.',
      ),
      'active' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Boolean indicating whether or not the poll is open.',
      ),
    ),
    'primary key' => array('nid'),
    'foreign keys' => array(
      'poll_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
    ),
  );

  $schema['poll_choice'] = array(
    'description' => 'Stores information about all choices for all {poll}s.',
    'fields' => array(
      'chid' => array(
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => 'Unique identifier for a poll choice.',
      ),
      'nid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {node}.nid this choice belongs to.',
      ),
      'chtext' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The text for this choice.',
        'translatable' => TRUE,
      ),
      'chvotes' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The total number of votes this choice has received by all users.',
      ),
      'weight' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The sort order of this choice among all choices for the same node.',
      ),
    ),
    'indexes' => array(
      'nid' => array('nid'),
    ),
    'primary key' => array('chid'),
    'foreign keys' => array(
      'choice_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
    ),
  );

  $schema['poll_vote'] = array(
    'description' => 'Stores per-{users} votes for each {poll}.',
    'fields' => array(
      'chid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => "The {users}'s vote for this poll.",
      ),
      'nid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => 'The {poll} node this vote is for.',
      ),
      'uid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {users}.uid this vote is from unless the voter was anonymous.',
      ),
      'hostname' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The IP address this vote is from unless the voter was logged in.',
      ),
      'timestamp' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The timestamp of the vote creation.',
      ),
    ),
    'primary key' => array('nid', 'uid', 'hostname'),
    'foreign keys' => array(
      'poll_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
      'voter' => array(
        'table' => 'users',
        'columns' => array('uid' => 'uid'),
      ),
    ),
    'indexes' => array(
      'chid'     => array('chid'),
      'hostname' => array('hostname'),
      'uid' => array('uid'),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/poll/poll.install](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install) · Licensed GPL-2.0-or-later (see LICENSE)._

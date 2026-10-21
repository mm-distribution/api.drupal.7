# shortcut_schema()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.install`](_file.md), lines 52–115 · [local source](../../../../source/modules/shortcut/shortcut.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.install#L52-L115)
- **Module/theme:** shortcut
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function shortcut_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function shortcut_schema() {
  $schema['shortcut_set'] = array(
    'description' => 'Stores information about sets of shortcuts links.',
    'fields' => array(
      'set_name' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
        'description' => "Primary Key: The {menu_links}.menu_name under which the set's links are stored.",
      ),
      'title' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The title of the set.',
      ),
    ),
    'primary key' => array('set_name'),
    'foreign keys' => array(
      'menu_name' => array(
        'table' => 'menu_links',
        'columns' => array('set_name' => 'menu_name'),
      ),
    ),
  );

  $schema['shortcut_set_users'] = array(
    'description' => 'Maps users to shortcut sets.',
    'fields' => array(
      'uid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {users}.uid for this set.',
      ),
      'set_name' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
        'description' => "The {shortcut_set}.set_name that will be displayed for this user.",
      ),
    ),
    'primary key' => array('uid'),
    'indexes' => array(
      'set_name' => array('set_name'),
    ),
    'foreign keys' => array(
      'set_user' => array(
        'table' => 'users',
        'columns' => array('uid' => 'uid'),
      ),
      'set_name' => array(
        'table' => 'shortcut_set',
        'columns' => array('set_name' => 'set_name'),
      ),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.install](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.install) · Licensed GPL-2.0-or-later (see LICENSE)._

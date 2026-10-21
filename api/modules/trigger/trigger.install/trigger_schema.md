# trigger_schema()

- **Type:** Function
- **File:** [`modules/trigger/trigger.install`](_file.md), lines 11–47 · [local source](../../../../source/modules/trigger/trigger.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install#L11-L47)
- **Module/theme:** trigger
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function trigger_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function trigger_schema() {
  // The total index length (hook and aid) must be less than 333. Since the aid
  // field is 255 characters, the hook field can have a maximum length of 78.
  $schema['trigger_assignments'] = array(
    'description' => 'Maps trigger to hook and operation assignments from trigger.module.',
    'fields' => array(
      'hook' => array(
        'type' => 'varchar',
        'length' => 78,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Primary Key: The name of the internal Drupal hook; for example, node_insert.',
      ),
      'aid' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => "Primary Key: Action's {actions}.aid.",
      ),
      'weight' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The weight of the trigger assignment in relation to other triggers.',
      ),
    ),
    'primary key' => array('hook', 'aid'),
    'foreign keys' => array(
      'action' => array(
        'table' => 'actions',
        'columns' => array('aid' => 'aid'),
      ),
    ),
  );
  return $schema;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.install](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install) · Licensed GPL-2.0-or-later (see LICENSE)._

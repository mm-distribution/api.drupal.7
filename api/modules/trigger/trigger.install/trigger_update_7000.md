# trigger_update_7000()

- **Type:** Function
- **File:** [`modules/trigger/trigger.install`](_file.md), lines 63–80 · [local source](../../../../source/modules/trigger/trigger.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install#L63-L80)
- **Module/theme:** trigger

## Signature

```php
function trigger_update_7000()
```

## Documentation

```text
Alter the "hook" field and drop the "op field" of {trigger_assignments}.

Increase the length of the "hook" field to 78 characters and adds operation
names to the hook names, and drops the "op" field.
```

## Code

```php
function trigger_update_7000() {
  db_drop_primary_key('trigger_assignments');
  db_change_field('trigger_assignments', 'hook', 'hook', array('type' => 'varchar', 'length' => 78, 'not null' => TRUE, 'default' => '', 'description' => 'Primary Key: The name of the internal Drupal hook; for example, node_insert.'));

  $result = db_query("SELECT hook, op, aid FROM {trigger_assignments} WHERE op <> ''");

  foreach ($result as $record) {
    db_update('trigger_assignments')
      ->fields(array('hook' => $record->hook . '_' . $record->op))
      ->condition('hook', $record->hook)
      ->condition('op', $record->op)
      ->condition('aid', $record->aid)
      ->execute();
  }
  db_drop_field('trigger_assignments', 'op');

  db_add_primary_key('trigger_assignments', array('hook', 'aid'));
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.install](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install) · Licensed GPL-2.0-or-later (see LICENSE)._

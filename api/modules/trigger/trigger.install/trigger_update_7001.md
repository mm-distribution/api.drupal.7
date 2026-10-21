# trigger_update_7001()

- **Type:** Function
- **File:** [`modules/trigger/trigger.install`](_file.md), lines 93–96 · [local source](../../../../source/modules/trigger/trigger.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install#L93-L96)
- **Module/theme:** trigger
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function trigger_update_7001()
```

## Documentation

```text
Increase the length of the "hook" field to 78 characters.

This is a separate function for those who ran an older version of
trigger_update_7000() that did not do this.
```

## Code

```php
function trigger_update_7001() {
  db_drop_primary_key('trigger_assignments');
  db_change_field('trigger_assignments', 'hook', 'hook', array('type' => 'varchar', 'length' => 78, 'not null' => TRUE, 'default' => '', 'description' => 'Primary Key: The name of the internal Drupal hook; for example, node_insert.', ), array('primary key' => array('hook', 'aid')));
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.install](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install) · Licensed GPL-2.0-or-later (see LICENSE)._

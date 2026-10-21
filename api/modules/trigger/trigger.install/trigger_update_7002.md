# trigger_update_7002()

- **Type:** Function
- **File:** [`modules/trigger/trigger.install`](_file.md), lines 101–112 · [local source](../../../../source/modules/trigger/trigger.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install#L101-L112)
- **Module/theme:** trigger
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function trigger_update_7002()
```

## Documentation

```text
Renames nodeapi to node.
```

## Code

```php
function trigger_update_7002() {
  $result = db_query("SELECT hook, aid FROM {trigger_assignments}");

  foreach($result as $record) {
    $new_hook = str_replace('nodeapi', 'node', $record->hook);
    db_update('trigger_assignments')
      ->fields(array('hook' => $new_hook))
      ->condition('hook', $record->hook)
      ->condition('aid', $record->aid)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.install](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install) · Licensed GPL-2.0-or-later (see LICENSE)._

# system_update_7063()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3101–3109 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3101-L3109)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7063()
```

## Documentation

```text
Delete {menu_links} records for 'type' => MENU_CALLBACK which would not appear in a fresh install.
```

## Code

```php
function system_update_7063() {
  // For router items where 'type' => MENU_CALLBACK, {menu_router}.type is
  // stored as 4 in Drupal 6, and 0 in Drupal 7. Fortunately Drupal 7 doesn't
  // store any types as 4, so delete both.
  $result = db_query('SELECT ml.mlid FROM {menu_links} ml INNER JOIN {menu_router} mr ON ml.router_path = mr.path WHERE ml.module = :system AND ml.customized = 0 AND mr.type IN(:callbacks)', array(':callbacks' => array(0, 4), ':system' => 'system'));
  foreach ($result as $record) {
    db_delete('menu_links')->condition('mlid', $record->mlid)->execute();
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._

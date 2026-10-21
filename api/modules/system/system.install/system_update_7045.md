# system_update_7045()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2474–2477 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2474-L2477)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7045()
```

## Documentation

```text
Add expiration field to the {flood} table.
```

## Code

```php
function system_update_7045() {
  db_add_field('flood', 'expiration', array('description' => 'Expiration timestamp. Expired events are purged on cron run.', 'type' => 'int', 'not null' => TRUE, 'default' => 0));
  db_add_index('flood', 'purge', array('expiration'));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._

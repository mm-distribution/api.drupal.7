# system_update_7051()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2555–2557 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2555-L2557)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7051()
```

## Documentation

```text
make the IP field IPv6 compatible
```

## Code

```php
function system_update_7051() {
  db_change_field('blocked_ips', 'ip', 'ip', array('description' => 'IP address', 'type' => 'varchar', 'length' => 40, 'not null' => TRUE, 'default' => ''));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._

# system_update_7002()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 1931–1956 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L1931-L1956)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7002()
```

## Documentation

```text
Add a table to store blocked IP addresses.
```

## Code

```php
function system_update_7002() {
  $schema['blocked_ips'] = array(
    'description' => 'Stores blocked IP addresses.',
    'fields' => array(
      'iid' => array(
        'description' => 'Primary Key: unique ID for IP addresses.',
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'ip' => array(
        'description' => 'IP address',
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
      ),
    ),
    'indexes' => array(
      'blocked_ip' => array('ip'),
    ),
    'primary key' => array('iid'),
  );

  db_create_table('blocked_ips', $schema['blocked_ips']);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._

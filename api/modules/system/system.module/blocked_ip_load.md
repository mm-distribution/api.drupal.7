# blocked_ip_load()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1720–1722 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1720-L1722)
- **Module/theme:** system

## Signature

```php
function blocked_ip_load($iid)
```

## Documentation

```text
Retrieve a blocked IP address from the database.

@param $iid integer
  The ID of the blocked IP address to retrieve.

@return
  The blocked IP address from the database as an array.
```

## Code

```php
function blocked_ip_load($iid) {
  return db_query("SELECT * FROM {blocked_ips} WHERE iid = :iid", array(':iid' => $iid))->fetchAssoc();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._

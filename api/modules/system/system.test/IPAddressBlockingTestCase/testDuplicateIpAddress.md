# IPAddressBlockingTestCase::testDuplicateIpAddress()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 777–791 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L777-L791)
- **Class:** [IPAddressBlockingTestCase](../IPAddressBlockingTestCase.md)
- **Module/theme:** system

## Signature

```php
function testDuplicateIpAddress()
```

## Documentation

```text
Test duplicate IP addresses are not present in the 'blocked_ips' table.
```

## Code

```php
  function testDuplicateIpAddress() {
    drupal_static_reset('ip_address');
    $submit_ip = $_SERVER['REMOTE_ADDR'] = '192.168.1.1';
    system_block_ip_action();
    system_block_ip_action();
    $ip_count = db_query("SELECT COUNT(*) from {blocked_ips} WHERE ip = :ip", array(':ip' => $submit_ip))->fetchColumn();
    $this->assertEqual('1', $ip_count);
    drupal_static_reset('ip_address');
    $submit_ip = $_SERVER['REMOTE_ADDR'] = ' ';
    system_block_ip_action();
    system_block_ip_action();
    system_block_ip_action();
    $ip_count = db_query("SELECT COUNT(*) from {blocked_ips} WHERE ip = :ip", array(':ip' => $submit_ip))->fetchColumn();
    $this->assertEqual('1', $ip_count);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

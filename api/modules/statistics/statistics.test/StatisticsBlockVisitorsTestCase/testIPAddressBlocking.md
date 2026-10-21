# StatisticsBlockVisitorsTestCase::testIPAddressBlocking()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 273–305 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L273-L305)
- **Class:** [StatisticsBlockVisitorsTestCase](../StatisticsBlockVisitorsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testIPAddressBlocking()
```

## Documentation

```text
Blocks an IP address via the top visitors report and then unblocks it.
```

## Code

```php
  function testIPAddressBlocking() {
    // IP address for testing.
    $test_ip_address = '1.2.3.3';

    // Verify the IP address from accesslog appears on the top visitors page
    // and that a 'block IP address' link is displayed.
    $this->drupalLogin($this->blocking_user);
    $this->drupalGet('admin/reports/visitors');
    $this->assertText($test_ip_address, 'IP address found.');
    $this->assertText(t('block IP address'), 'Block IP link displayed');

    // Block the IP address.
    $this->clickLink('block IP address');
    $this->assertText(t('IP address blocking'), 'IP blocking page displayed.');
    $edit = array();
    $edit['ip'] = $test_ip_address;
    $this->drupalPost('admin/config/people/ip-blocking', $edit, t('Add'));
    $ip = db_query("SELECT iid from {blocked_ips} WHERE ip = :ip", array(':ip' => $edit['ip']))->fetchField();
    $this->assertNotEqual($ip, FALSE, 'IP address found in database');
    $this->assertRaw(t('The IP address %ip has been blocked.', array('%ip' => $edit['ip'])), 'IP address was blocked.');

    // Verify that the block/unblock link on the top visitors page has been
    // altered.
    $this->drupalGet('admin/reports/visitors');
    $this->assertText(t('unblock IP address'), 'Unblock IP address link displayed');

    // Unblock the IP address.
    $this->clickLink('unblock IP address');
    $this->assertRaw(t('Are you sure you want to delete %ip?', array('%ip' => $test_ip_address)), 'IP address deletion confirmation found.');
    $edit = array();
    $this->drupalPost('admin/config/people/ip-blocking/delete/1', NULL, t('Delete'));
    $this->assertRaw(t('The IP address %ip was deleted.', array('%ip' => $test_ip_address)), 'IP address deleted.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._

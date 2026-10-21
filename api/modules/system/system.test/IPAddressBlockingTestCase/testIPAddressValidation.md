# IPAddressBlockingTestCase::testIPAddressValidation()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 724–772 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L724-L772)
- **Class:** [IPAddressBlockingTestCase](../IPAddressBlockingTestCase.md)
- **Module/theme:** system

## Signature

```php
function testIPAddressValidation()
```

## Documentation

```text
Test a variety of user input to confirm correct validation and saving of data.
```

## Code

```php
  function testIPAddressValidation() {
    $this->drupalGet('admin/config/people/ip-blocking');

    // Block a valid IP address.
    $edit = array();
    $edit['ip'] = '1.2.3.3';
    $this->drupalPost('admin/config/people/ip-blocking', $edit, t('Add'));
    $ip = db_query("SELECT iid from {blocked_ips} WHERE ip = :ip", array(':ip' => $edit['ip']))->fetchField();
    $this->assertTrue($ip, t('IP address found in database.'));
    $this->assertRaw(t('The IP address %ip has been blocked.', array('%ip' => $edit['ip'])), t('IP address was blocked.'));

    // Try to block an IP address that's already blocked.
    $edit = array();
    $edit['ip'] = '1.2.3.3';
    $this->drupalPost('admin/config/people/ip-blocking', $edit, t('Add'));
    $this->assertText(t('This IP address is already blocked.'));

    // Try to block a reserved IP address.
    $edit = array();
    $edit['ip'] = '255.255.255.255';
    $this->drupalPost('admin/config/people/ip-blocking', $edit, t('Add'));
    $this->assertText(t('Enter a valid IP address.'));

    // Try to block a reserved IP address.
    $edit = array();
    $edit['ip'] = 'test.example.com';
    $this->drupalPost('admin/config/people/ip-blocking', $edit, t('Add'));
    $this->assertText(t('Enter a valid IP address.'));

    // Submit an empty form.
    $edit = array();
    $edit['ip'] = '';
    $this->drupalPost('admin/config/people/ip-blocking', $edit, t('Add'));
    $this->assertText(t('Enter a valid IP address.'));

    // Pass an IP address as a URL parameter and submit it.
    $submit_ip = '1.2.3.4';
    $this->drupalPost('admin/config/people/ip-blocking/' . $submit_ip, NULL, t('Add'));
    $ip = db_query("SELECT iid from {blocked_ips} WHERE ip = :ip", array(':ip' => $submit_ip))->fetchField();
    $this->assertTrue($ip, t('IP address found in database'));
    $this->assertRaw(t('The IP address %ip has been blocked.', array('%ip' => $submit_ip)), t('IP address was blocked.'));

    // Submit your own IP address. This fails, although it works when testing manually.
     // TODO: on some systems this test fails due to a bug or inconsistency in cURL.
     // $edit = array();
     // $edit['ip'] = ip_address();
     // $this->drupalPost('admin/config/people/ip-blocking', $edit, t('Save'));
     // $this->assertText(t('You may not block your own IP address.'));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

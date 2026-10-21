# BootstrapIPAddressTestCase::testIPAddressHost()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 48–119 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L48-L119)
- **Class:** [BootstrapIPAddressTestCase](../BootstrapIPAddressTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testIPAddressHost()
```

## Documentation

```text
test IP Address and hostname
```

## Code

```php
  function testIPAddressHost() {
    // Test the normal IP address.
    $this->assertTrue(
      ip_address() == $this->remote_ip,
      'Got remote IP address.'
    );

    // Proxy forwarding on but no proxy addresses defined.
    variable_set('reverse_proxy', 1);
    $this->assertTrue(
      ip_address() == $this->remote_ip,
      'Proxy forwarding without trusted proxies got remote IP address.'
    );

    // Proxy forwarding on and proxy address not trusted.
    variable_set('reverse_proxy_addresses', array($this->proxy_ip, $this->proxy2_ip));
    drupal_static_reset('ip_address');
    $_SERVER['REMOTE_ADDR'] = $this->untrusted_ip;
    $this->assertTrue(
      ip_address() == $this->untrusted_ip,
      'Proxy forwarding with untrusted proxy got remote IP address.'
    );

    // Proxy forwarding on and proxy address trusted.
    $_SERVER['REMOTE_ADDR'] = $this->proxy_ip;
    $_SERVER['HTTP_X_FORWARDED_FOR'] = $this->forwarded_ip;
    drupal_static_reset('ip_address');
    $this->assertTrue(
      ip_address() == $this->forwarded_ip,
      'Proxy forwarding with trusted proxy got forwarded IP address.'
    );

    // Proxy forwarding on and proxy address trusted and visiting from proxy.
    $_SERVER['REMOTE_ADDR'] = $this->proxy_ip;
    $_SERVER['HTTP_X_FORWARDED_FOR'] = $this->proxy_ip;
    drupal_static_reset('ip_address');
    $this->assertTrue(
      ip_address() == $this->proxy_ip,
      'Visiting from trusted proxy got proxy IP address.'
    );

    // Multi-tier architecture with comma separated values in header.
    $_SERVER['REMOTE_ADDR'] = $this->proxy_ip;
    $_SERVER['HTTP_X_FORWARDED_FOR'] = implode(', ', array($this->untrusted_ip, $this->forwarded_ip, $this->proxy2_ip));
    drupal_static_reset('ip_address');
    $this->assertTrue(
      ip_address() == $this->forwarded_ip,
      'Proxy forwarding with trusted 2-tier proxy got forwarded IP address.'
    );

    // Custom client-IP header.
    variable_set('reverse_proxy_header', 'HTTP_X_CLUSTER_CLIENT_IP');
    $_SERVER['HTTP_X_CLUSTER_CLIENT_IP'] = $this->cluster_ip;
    drupal_static_reset('ip_address');
    $this->assertTrue(
      ip_address() == $this->cluster_ip,
      'Cluster environment got cluster client IP.'
    );

    // Verifies that drupal_valid_http_host() prevents invalid characters.
    $this->assertFalse(drupal_valid_http_host('security/.drupal.org:80'), 'HTTP_HOST with / is invalid');
    $this->assertFalse(drupal_valid_http_host('security\\.drupal.org:80'), 'HTTP_HOST with \\ is invalid');
    $this->assertFalse(drupal_valid_http_host('security<.drupal.org:80'), 'HTTP_HOST with &lt; is invalid');
    $this->assertFalse(drupal_valid_http_host('security..drupal.org:80'), 'HTTP_HOST with .. is invalid');
    // Verifies that host names are shorter than 1000 characters.
    $this->assertFalse(drupal_valid_http_host(str_repeat('x', 1001)), 'HTTP_HOST with more than 1000 characters is invalid.');
    $this->assertFalse(drupal_valid_http_host(str_repeat('.', 101)), 'HTTP_HOST with more than 100 subdomains is invalid.');
    $this->assertFalse(drupal_valid_http_host(str_repeat(':', 101)), 'HTTP_HOST with more than 100 portseparators is invalid.');

    // IPv6 loopback address
    $this->assertTrue(drupal_valid_http_host('[::1]:80'), 'HTTP_HOST containing IPv6 loopback is valid');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._

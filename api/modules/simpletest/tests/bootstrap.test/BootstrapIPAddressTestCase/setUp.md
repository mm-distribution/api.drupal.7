# BootstrapIPAddressTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 20–37 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L20-L37)
- **Class:** [BootstrapIPAddressTestCase](../BootstrapIPAddressTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    $this->oldserver = $_SERVER;

    $this->remote_ip = '127.0.0.1';
    $this->proxy_ip = '127.0.0.2';
    $this->proxy2_ip = '127.0.0.3';
    $this->forwarded_ip = '127.0.0.4';
    $this->cluster_ip = '127.0.0.5';
    $this->untrusted_ip = '0.0.0.0';

    drupal_static_reset('ip_address');

    $_SERVER['REMOTE_ADDR'] = $this->remote_ip;
    unset($_SERVER['HTTP_X_FORWARDED_FOR']);
    unset($_SERVER['HTTP_X_CLUSTER_CLIENT_IP']);

    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._

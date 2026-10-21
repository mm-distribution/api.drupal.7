# BootstrapTrustedHostsTestCase::testTrustedHosts()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 985–998 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L985-L998)
- **Class:** [BootstrapTrustedHostsTestCase](../BootstrapTrustedHostsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTrustedHosts()
```

## Documentation

```text
Tests hostname validation.

@see drupal_check_trusted_hosts()
```

## Code

```php
  function testTrustedHosts() {
    $trusted_host_patterns = array(
      '^example\.com$',
      '^.+\.example\.com$',
      '^example\.org',
      '^.+\.example\.org',
    );

    foreach ($this->providerTestTrustedHosts() as $data) {
      $test = array_combine(array('host', 'message', 'expected'), $data);
      $valid_host = drupal_check_trusted_hosts($test['host'], $trusted_host_patterns);
      $this->assertEqual($test['expected'], $valid_host, $test['message']);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._

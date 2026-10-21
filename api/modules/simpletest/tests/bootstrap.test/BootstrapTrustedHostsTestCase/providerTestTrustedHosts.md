# BootstrapTrustedHostsTestCase::providerTestTrustedHosts()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 1003–1023 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L1003-L1023)
- **Class:** [BootstrapTrustedHostsTestCase](../BootstrapTrustedHostsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function providerTestTrustedHosts()
```

## Documentation

```text
Provides test data for testTrustedHosts().
```

## Code

```php
  public function providerTestTrustedHosts() {
    $data = array();

    // Tests canonical URL.
    $data[] = array('www.example.com', 'canonical URL is trusted', TRUE);

    // Tests missing hostname for HTTP/1.0 compatability where the Host
    // header is optional.
    $data[] = array(NULL, 'empty Host is valid', TRUE);

    // Tests the additional patterns from the settings.
    $data[] = array('example.com', 'host from settings is trusted', TRUE);
    $data[] = array('subdomain.example.com', 'host from settings is trusted', TRUE);
    $data[] = array('www.example.org', 'host from settings is trusted', TRUE);
    $data[] = array('example.org', 'host from settings is trusted', TRUE);

    // Tests mismatch.
    $data[] = array('www.blackhat.com', 'unspecified host is untrusted', FALSE);

    return $data;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# DrupalHTTPRequestTestCase::testDrupalHTTPRequestBasicAuth()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1215–1226 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1215-L1226)
- **Class:** [DrupalHTTPRequestTestCase](../DrupalHTTPRequestTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHTTPRequestBasicAuth()
```

## Documentation

_No docblock in source._

## Code

```php
  function testDrupalHTTPRequestBasicAuth() {
    $username = $this->randomName();
    $password = $this->randomName();
    $url = url('system-test/auth', array('absolute' => TRUE));

    $auth = str_replace('://', '://' . $username . ':' . $password . '@', $url);
    $result = drupal_http_request($auth);

    $this->drupalSetContent($result->data);
    $this->assertRaw($username, 'Username is passed correctly.');
    $this->assertRaw($password, 'Password is passed correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

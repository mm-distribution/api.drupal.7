# DrupalHTTPRequestTestCase::testDrupalHTTPRequestRedirect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1228–1269 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1228-L1269)
- **Class:** [DrupalHTTPRequestTestCase](../DrupalHTTPRequestTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHTTPRequestRedirect()
```

## Documentation

_No docblock in source._

## Code

```php
  function testDrupalHTTPRequestRedirect() {
    $redirect_301 = drupal_http_request(url('system-test/redirect/301', array('absolute' => TRUE)), array('max_redirects' => 1));
    $this->assertEqual($redirect_301->redirect_code, 301, 'drupal_http_request follows the 301 redirect.');

    $redirect_301 = drupal_http_request(url('system-test/redirect/301', array('absolute' => TRUE)), array('max_redirects' => 0));
    $this->assertFalse(isset($redirect_301->redirect_code), 'drupal_http_request does not follow 301 redirect if max_redirects = 0.');

    $redirect_invalid = drupal_http_request(url('system-test/redirect-protocol-relative', array('absolute' => TRUE)), array('max_redirects' => 1));
    $this->assertEqual($redirect_invalid->code, -1002, format_string('301 redirect to protocol-relative URL returned with error code !error.', array('!error' => $redirect_invalid->error)));
    $this->assertEqual($redirect_invalid->error, 'missing schema', format_string('301 redirect to protocol-relative URL returned with error message "!error".', array('!error' => $redirect_invalid->error)));

    $redirect_invalid = drupal_http_request(url('system-test/redirect-noscheme', array('absolute' => TRUE)), array('max_redirects' => 1));
    $this->assertEqual($redirect_invalid->code, -1002, format_string('301 redirect to invalid URL returned with error code !error.', array('!error' => $redirect_invalid->error)));
    $this->assertEqual($redirect_invalid->error, 'missing schema', format_string('301 redirect to invalid URL returned with error message "!error".', array('!error' => $redirect_invalid->error)));

    $redirect_invalid = drupal_http_request(url('system-test/redirect-noparse', array('absolute' => TRUE)), array('max_redirects' => 1));
    $this->assertEqual($redirect_invalid->code, -1001, format_string('301 redirect to invalid URL returned with error message code "!error".', array('!error' => $redirect_invalid->error)));
    $this->assertEqual($redirect_invalid->error, 'unable to parse URL', format_string('301 redirect to invalid URL returned with error message "!error".', array('!error' => $redirect_invalid->error)));

    $redirect_invalid = drupal_http_request(url('system-test/redirect-invalid-scheme', array('absolute' => TRUE)), array('max_redirects' => 1));
    $this->assertEqual($redirect_invalid->code, -1003, format_string('301 redirect to invalid URL returned with error code !error.', array('!error' => $redirect_invalid->error)));
    $this->assertEqual($redirect_invalid->error, 'invalid schema ftp', format_string('301 redirect to invalid URL returned with error message "!error".', array('!error' => $redirect_invalid->error)));

    $redirect_302 = drupal_http_request(url('system-test/redirect/302', array('absolute' => TRUE)), array('max_redirects' => 1));
    $this->assertEqual($redirect_302->redirect_code, 302, 'drupal_http_request follows the 302 redirect.');

    $redirect_302 = drupal_http_request(url('system-test/redirect/302', array('absolute' => TRUE)), array('max_redirects' => 0));
    $this->assertFalse(isset($redirect_302->redirect_code), 'drupal_http_request does not follow 302 redirect if $retry = 0.');

    $redirect_307 = drupal_http_request(url('system-test/redirect/307', array('absolute' => TRUE)), array('max_redirects' => 1));
    $this->assertEqual($redirect_307->redirect_code, 307, 'drupal_http_request follows the 307 redirect.');

    $redirect_307 = drupal_http_request(url('system-test/redirect/307', array('absolute' => TRUE)), array('max_redirects' => 0));
    $this->assertFalse(isset($redirect_307->redirect_code), 'drupal_http_request does not follow 307 redirect if max_redirects = 0.');

    $multiple_redirect_final_url = url('system-test/multiple-redirects/0', array('absolute' => TRUE));
    $multiple_redirect_1 = drupal_http_request(url('system-test/multiple-redirects/1', array('absolute' => TRUE)), array('max_redirects' => 1));
    $this->assertEqual($multiple_redirect_1->redirect_url, $multiple_redirect_final_url, 'redirect_url contains the final redirection location after 1 redirect.');

    $multiple_redirect_3 = drupal_http_request(url('system-test/multiple-redirects/3', array('absolute' => TRUE)), array('max_redirects' => 3));
    $this->assertEqual($multiple_redirect_3->redirect_url, $multiple_redirect_final_url, 'redirect_url contains the final redirection location after 3 redirects.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

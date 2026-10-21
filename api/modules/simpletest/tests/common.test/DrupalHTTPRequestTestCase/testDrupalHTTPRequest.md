# DrupalHTTPRequestTestCase::testDrupalHTTPRequest()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1166–1213 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1166-L1213)
- **Class:** [DrupalHTTPRequestTestCase](../DrupalHTTPRequestTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHTTPRequest()
```

## Documentation

_No docblock in source._

## Code

```php
  function testDrupalHTTPRequest() {
    global $is_https;

    // Parse URL schema.
    $missing_scheme = drupal_http_request('example.com/path');
    $this->assertEqual($missing_scheme->code, -1002, 'Returned with "-1002" error code.');
    $this->assertEqual($missing_scheme->error, 'missing schema', 'Returned with "missing schema" error message.');

    $unable_to_parse = drupal_http_request('http:///path');
    $this->assertEqual($unable_to_parse->code, -1001, 'Returned with "-1001" error code.');
    $this->assertEqual($unable_to_parse->error, 'unable to parse URL', 'Returned with "unable to parse URL" error message.');

    // Fetch page and check that the data parameter works with both array and string.
    $data_array = array($this->randomName() => $this->randomString() . ' "\'');
    $data_string = drupal_http_build_query($data_array);
    $result = drupal_http_request(url('node', array('absolute' => TRUE)), array('data' => $data_array));
    $this->assertEqual($result->code, 200, 'Fetched page successfully.');
    $this->assertTrue(substr($result->request, -strlen($data_string)) === $data_string, 'Request ends with URL-encoded data when drupal_http_request() called using array.');
    $result = drupal_http_request(url('node', array('absolute' => TRUE)), array('data' => $data_string));
    $this->assertTrue(substr($result->request, -strlen($data_string)) === $data_string, 'Request ends with URL-encoded data when drupal_http_request() called using string.');

    $this->drupalSetContent($result->data);
    $this->assertTitle(t('Welcome to @site-name | @site-name', array('@site-name' => variable_get('site_name', 'Drupal'))), 'Site title matches.');

    // Test that code and status message is returned.
    $result = drupal_http_request(url('pagedoesnotexist', array('absolute' => TRUE)));
    $this->assertTrue(!empty($result->protocol),  'Result protocol is returned.');
    $this->assertEqual($result->code, '404', 'Result code is 404');
    $this->assertEqual($result->status_message, 'Not Found', 'Result status message is "Not Found"');

    // Skip the timeout tests when the testing environment is HTTPS because
    // stream_set_timeout() does not work for SSL connections.
    // @link http://bugs.php.net/bug.php?id=47929
    if (!$is_https) {
      // Test that timeout is respected. The test machine is expected to be able
      // to make the connection (i.e. complete the fsockopen()) in 2 seconds and
      // return within a total of 5 seconds. If the test machine is extremely
      // slow, the test will fail. fsockopen() has been seen to time out in
      // slightly less than the specified timeout, so allow a little slack on
      // the minimum expected time (i.e. 1.8 instead of 2).
      timer_start(__METHOD__);
      $result = drupal_http_request(url('system-test/sleep/10', array('absolute' => TRUE)), array('timeout' => 2));
      $time = timer_read(__METHOD__) / 1000;
      $this->assertTrue(1.8 < $time && $time < 5, format_string('Request timed out (%time seconds).', array('%time' => $time)));
      $this->assertTrue($result->error, 'An error message was returned.');
      $this->assertEqual($result->code, HTTP_REQUEST_TIMEOUT, 'Proper error code was returned.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

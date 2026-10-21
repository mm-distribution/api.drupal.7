# SimpleTestFunctionalTest::testUserAgentValidation()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 104–136 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L104-L136)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function testUserAgentValidation()
```

## Documentation

```text
Test validation of the User-Agent header we use to perform test requests.
```

## Code

```php
  function testUserAgentValidation() {
    if (!$this->inCURL()) {
      global $base_url;
      $simpletest_path = $base_url . '/' . drupal_get_path('module', 'simpletest');
      $HTTP_path = $simpletest_path .'/tests/http.php?q=node';
      $https_path = $simpletest_path .'/tests/https.php?q=node';
      // Generate a valid simpletest User-Agent to pass validation.
      $this->assertTrue(preg_match('/simpletest\d+/', $this->databasePrefix, $matches), 'Database prefix contains simpletest prefix.');
      $test_ua = drupal_generate_test_ua($matches[0]);
      $this->additionalCurlOptions = array(CURLOPT_USERAGENT => $test_ua);

      // Test pages only available for testing.
      $this->drupalGet($HTTP_path);
      $this->assertResponse(200, 'Requesting http.php with a legitimate simpletest User-Agent returns OK.');
      $this->drupalGet($https_path);
      $this->assertResponse(200, 'Requesting https.php with a legitimate simpletest User-Agent returns OK.');

      // Now slightly modify the HMAC on the header, which should not validate.
      $this->additionalCurlOptions = array(CURLOPT_USERAGENT => $test_ua . 'X');
      $this->drupalGet($HTTP_path);
      $this->assertResponse(403, 'Requesting http.php with a bad simpletest User-Agent fails.');
      $this->drupalGet($https_path);
      $this->assertResponse(403, 'Requesting https.php with a bad simpletest User-Agent fails.');

      // Use a real User-Agent and verify that the special files http.php and
      // https.php can't be accessed.
      $this->additionalCurlOptions = array(CURLOPT_USERAGENT => 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12');
      $this->drupalGet($HTTP_path);
      $this->assertResponse(403, 'Requesting http.php with a normal User-Agent fails.');
      $this->drupalGet($https_path);
      $this->assertResponse(403, 'Requesting https.php with a normal User-Agent fails.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._

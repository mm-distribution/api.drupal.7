# RequestSanitizerTest::requestSanitizationTest()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 74–116 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L74-L116)
- **Class:** [RequestSanitizerTest](../RequestSanitizerTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function requestSanitizationTest(SanitizerTestRequest $request, array $expected = array(), array $expected_errors = NULL, array $whitelist = array(), $label = NULL)
```

## Documentation

```text
Tests RequestSanitizer class.

@param \SanitizerTestRequest $request
  The request to sanitize.
@param array $expected
  An array of expected request parameters after sanitization.
@param array|null $expected_errors
  An array of expected errors. If set to NULL then error logging is
  disabled.
@param array $whitelist
  An array of keys to whitelist and not sanitize.
@param string $label
  A descriptive name for each test / group of assertions.

@throws \ReflectionException
```

## Code

```php
  public function requestSanitizationTest(SanitizerTestRequest $request, array $expected = array(), array $expected_errors = NULL, array $whitelist = array(), $label = NULL) {
    // Set up globals.
    $_GET = $request->getQuery();
    $_POST = $request->getRequest();
    $_COOKIE = $request->getCookies();
    $_REQUEST = array_merge($request->getQuery(), $request->getRequest());

    $GLOBALS['conf']['sanitize_input_whitelist'] = $whitelist;
    $GLOBALS['conf']['sanitize_input_logging'] = is_null($expected_errors) ? FALSE : TRUE;
    if ($label !== 'already sanitized request') {
      $reflection = new \ReflectionProperty('DrupalRequestSanitizer', 'sanitized');
      $reflection->setAccessible(TRUE);
      $reflection->setValue(NULL, FALSE);
    }
    DrupalRequestSanitizer::sanitize();
    if (isset($_GET['destination'])) {
      DrupalRequestSanitizer::cleanDestination();
    }

    // Normalise the expected data.
    $expected += array(
      'cookies' => array(),
      'query' => array(),
      'request' => array(),
    );

    // Test PHP globals.
    $this->assertEqualLabelled($expected['cookies'], $_COOKIE, NULL, 'Other', $label . ' (COOKIE)');
    $this->assertEqualLabelled($expected['query'], $_GET, NULL, 'Other', $label . ' (GET)');
    $this->assertEqualLabelled($expected['request'], $_POST, NULL, 'Other', $label . ' (POST)');
    $expected_request = array_merge($expected['query'], $expected['request']);
    $this->assertEqualLabelled($expected_request, $_REQUEST, NULL, 'Other', $label . ' (REQUEST)');

    // Ensure any expected errors have been triggered.
    if (!empty($expected_errors)) {
      foreach ($expected_errors as $expected_error) {
        $this->assertError($expected_error, E_USER_NOTICE, $label . ' (errors)');
      }
    }
    else {
      $this->assertEqualLabelled(array(), $this->errors, NULL, 'Other', $label . ' (errors)');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# RequestSanitizerTest::requestSanitizerTests()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 124–209 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L124-L209)
- **Class:** [RequestSanitizerTest](../RequestSanitizerTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function requestSanitizerTests()
```

## Documentation

```text
Data provider for testRequestSanitization.

@return array
  A list of tests to carry out.
```

## Code

```php
  public function requestSanitizerTests() {
    $tests = array();

    $request = new SanitizerTestRequest(array('q' => 'index.php'));
    $tests['no sanitization GET'] = array($request, array('query' => array('q' => 'index.php')));

    $request = new SanitizerTestRequest(array(), array('field' => 'value'));
    $tests['no sanitization POST'] = array($request, array('request' => array('field' => 'value')));

    $request = new SanitizerTestRequest(array(), array(), array(), array('key' => 'value'));
    $tests['no sanitization COOKIE'] = array($request, array('cookies' => array('key' => 'value')));

    $request = new SanitizerTestRequest(array('q' => 'index.php'), array('field' => 'value'), array(), array('key' => 'value'));
    $tests['no sanitization GET, POST, COOKIE'] = array($request, array('query' => array('q' => 'index.php'), 'request' => array('field' => 'value'), 'cookies' => array('key' => 'value')));

    $request = new SanitizerTestRequest(array('q' => 'index.php'));
    $tests['no sanitization GET log'] = array($request, array('query' => array('q' => 'index.php')), array());

    $request = new SanitizerTestRequest(array(), array('field' => 'value'));
    $tests['no sanitization POST log'] = array($request, array('request' => array('field' => 'value')), array());

    $request = new SanitizerTestRequest(array(), array(), array(), array('key' => 'value'));
    $tests['no sanitization COOKIE log'] = array($request, array('cookies' => array('key' => 'value')), array());

    $request = new SanitizerTestRequest(array('#q' => 'index.php'));
    $tests['sanitization GET'] = array($request);

    $request = new SanitizerTestRequest(array(), array('#field' => 'value'));
    $tests['sanitization POST'] = array($request);

    $request = new SanitizerTestRequest(array(), array(), array(), array('#key' => 'value'));
    $tests['sanitization COOKIE'] = array($request);

    $request = new SanitizerTestRequest(array('#q' => 'index.php'), array('#field' => 'value'), array(), array('#key' => 'value'));
    $tests['sanitization GET, POST, COOKIE'] = array($request);

    $request = new SanitizerTestRequest(array('#q' => 'index.php'));
    $tests['sanitization GET log'] = array($request, array(), array('Potentially unsafe keys removed from query string parameters (GET): #q'));

    $request = new SanitizerTestRequest(array(), array('#field' => 'value'));
    $tests['sanitization POST log'] = array($request, array(), array('Potentially unsafe keys removed from request body parameters (POST): #field'));

    $request = new SanitizerTestRequest(array(), array(), array(), array('#key' => 'value'));
    $tests['sanitization COOKIE log'] = array($request, array(), array('Potentially unsafe keys removed from cookie parameters (COOKIE): #key'));

    $request = new SanitizerTestRequest(array('#q' => 'index.php'), array('#field' => 'value'), array(), array('#key' => 'value'));
    $tests['sanitization GET, POST, COOKIE log'] = array($request, array(), array('Potentially unsafe keys removed from query string parameters (GET): #q', 'Potentially unsafe keys removed from request body parameters (POST): #field', 'Potentially unsafe keys removed from cookie parameters (COOKIE): #key'));

    $request = new SanitizerTestRequest(array('q' => 'index.php', 'foo' => array('#bar' => 'foo')));
    $tests['recursive sanitization log'] = array($request, array('query' => array('q' => 'index.php', 'foo' => array())), array('Potentially unsafe keys removed from query string parameters (GET): #bar'));

    $request = new SanitizerTestRequest(array('q' => 'index.php', 'foo' => array('#bar' => 'foo')));
    $tests['recursive no sanitization whitelist'] = array($request, array('query' => array('q' => 'index.php', 'foo' => array('#bar' => 'foo'))), array(), array('#bar'));

    $request = new SanitizerTestRequest(array(), array('#field' => 'value'));
    $tests['no sanitization POST whitelist'] = array($request, array('request' => array('#field' => 'value')), array(), array('#field'));

    $request = new SanitizerTestRequest(array('q' => 'index.php', 'foo' => array('#bar' => 'foo', '#foo' => 'bar')));
    $tests['recursive multiple sanitization log'] = array($request, array('query' => array('q' => 'index.php', 'foo' => array())), array('Potentially unsafe keys removed from query string parameters (GET): #bar, #foo'));

    $request = new SanitizerTestRequest(array('#q' => 'index.php'));
    $tests['already sanitized request'] = array($request, array('query' => array('#q' => 'index.php')));

    $request = new SanitizerTestRequest(array('destination' => 'whatever?%23test=value'));
    $tests['destination removal GET'] = array($request);

    $request = new SanitizerTestRequest(array('destination' => 'whatever?%23test=value'));
    $tests['destination removal GET log'] = array($request, array(), array('Potentially unsafe destination removed from query string parameters (GET) because it contained the following keys: #test'));

    $request = new SanitizerTestRequest(array('destination' => 'whatever?q[%23test]=value'));
    $tests['destination removal subkey'] = array($request);

    $request = new SanitizerTestRequest(array('destination' => 'whatever?q[%23test]=value'));
    $tests['destination whitelist'] = array($request, array('query' => array('destination' => 'whatever?q[%23test]=value')), array(), array('#test'));

    $request = new SanitizerTestRequest(array('destination' => "whatever?\x00bar=base&%23test=value"));
    $tests['destination removal zero byte'] = array($request);

    $request = new SanitizerTestRequest(array('destination' => 'whatever?q=value'));
    $tests['destination kept'] = array($request, array('query' => array('destination' => 'whatever?q=value')));

    $request = new SanitizerTestRequest(array('destination' => 'whatever'));
    $tests['destination no query'] = array($request, array('query' => array('destination' => 'whatever')));

    return $tests;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._

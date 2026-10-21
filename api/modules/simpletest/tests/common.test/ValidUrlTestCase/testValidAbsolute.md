# ValidUrlTestCase::testValidAbsolute()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2509–2539 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2509-L2539)
- **Class:** [ValidUrlTestCase](../ValidUrlTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testValidAbsolute()
```

## Documentation

```text
Test valid absolute URLs.
```

## Code

```php
  function testValidAbsolute() {
    $url_schemes = array('http', 'https', 'ftp');
    $valid_absolute_urls = array(
      'example.com',
      'www.example.com',
      'ex-ample.com',
      '3xampl3.com',
      'example.com/paren(the)sis',
      'example.com/index.html#pagetop',
      'example.com:8080',
      'subdomain.example.com',
      'example.com/index.php?q=node',
      'example.com/index.php?q=node&param=false',
      'user@www.example.com',
      'user:pass@www.example.com:8080/login.php?do=login&style=%23#pagetop',
      '127.0.0.1',
      'example.org?',
      'john%20doe:secret:foo@example.org/',
      'example.org/~,$\'*;',
      'caf%C3%A9.example.org',
      '[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html',
    );

    foreach ($url_schemes as $scheme) {
      foreach ($valid_absolute_urls as $url) {
        $test_url = $scheme . '://' . $url;
        $valid_url = valid_url($test_url, TRUE);
        $this->assertTrue($valid_url, format_string('@url is a valid url.', array('@url' => $test_url)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

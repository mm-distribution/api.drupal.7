# ValidUrlTestCase::testValidRelative()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2564–2580 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2564-L2580)
- **Class:** [ValidUrlTestCase](../ValidUrlTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testValidRelative()
```

## Documentation

```text
Test valid relative URLs.
```

## Code

```php
  function testValidRelative() {
    $valid_relative_urls = array(
      'paren(the)sis',
      'index.html#pagetop',
      'index.php?q=node',
      'index.php?q=node&param=false',
      'login.php?do=login&style=%23#pagetop',
    );

    foreach (array('', '/') as $front) {
      foreach ($valid_relative_urls as $url) {
        $test_url = $front . $url;
        $valid_url = valid_url($test_url);
        $this->assertTrue($valid_url, format_string('@url is a valid url.', array('@url' => $test_url)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

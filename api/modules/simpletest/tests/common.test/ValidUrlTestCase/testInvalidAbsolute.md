# ValidUrlTestCase::testInvalidAbsolute()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2544–2559 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2544-L2559)
- **Class:** [ValidUrlTestCase](../ValidUrlTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInvalidAbsolute()
```

## Documentation

```text
Test invalid absolute URLs.
```

## Code

```php
  function testInvalidAbsolute() {
    $url_schemes = array('http', 'https', 'ftp');
    $invalid_ablosule_urls = array(
      '',
      'ex!ample.com',
      'ex%ample.com',
    );

    foreach ($url_schemes as $scheme) {
      foreach ($invalid_ablosule_urls as $url) {
        $test_url = $scheme . '://' . $url;
        $valid_url = valid_url($test_url, TRUE);
        $this->assertFalse($valid_url, format_string('@url is NOT a valid url.', array('@url' => $test_url)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

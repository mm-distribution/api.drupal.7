# ValidUrlTestCase::testInvalidRelative()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2585–2599 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2585-L2599)
- **Class:** [ValidUrlTestCase](../ValidUrlTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInvalidRelative()
```

## Documentation

```text
Test invalid relative URLs.
```

## Code

```php
  function testInvalidRelative() {
    $invalid_relative_urls = array(
      'ex^mple',
      'example<>',
      'ex%ample',
    );

    foreach (array('', '/') as $front) {
      foreach ($invalid_relative_urls as $url) {
        $test_url = $front . $url;
        $valid_url = valid_url($test_url);
        $this->assertFALSE($valid_url, format_string('@url is NOT a valid url.', array('@url' => $test_url)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

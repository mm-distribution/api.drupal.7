# DrupalGetQueryArrayTestCase::testDrupalGetQueryArray()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3379–3384 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3379-L3384)
- **Class:** [DrupalGetQueryArrayTestCase](../DrupalGetQueryArrayTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testDrupalGetQueryArray()
```

## Documentation

```text
Tests that drupal_get_query_array() correctly explodes query parameters.
```

## Code

```php
  public function testDrupalGetQueryArray() {
    $url = "http://my.site.com/somepath?foo=/content/folder[@name='foo']/folder[@name='bar']";
    $parsed = parse_url($url);
    $result = drupal_get_query_array($parsed['query']);
    $this->assertEqual($result['foo'], "/content/folder[@name='foo']/folder[@name='bar']", 'drupal_get_query_array() should only explode parameters on the first equals sign.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

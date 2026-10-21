# CommonURLUnitTest::testDrupalHttpBuildQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 188–193 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L188-L193)
- **Class:** [CommonURLUnitTest](../CommonURLUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHttpBuildQuery()
```

## Documentation

```text
Test drupal_http_build_query().
```

## Code

```php
  function testDrupalHttpBuildQuery() {
    $this->assertEqual(drupal_http_build_query(array('a' => ' &#//+%20@۞')), 'a=%20%26%23//%2B%2520%40%DB%9E', 'Value was properly encoded.');
    $this->assertEqual(drupal_http_build_query(array(' &#//+%20@۞' => 'a')), '%20%26%23%2F%2F%2B%2520%40%DB%9E=a', 'Key was properly encoded.');
    $this->assertEqual(drupal_http_build_query(array('a' => '1', 'b' => '2', 'c' => '3')), 'a=1&b=2&c=3', 'Multiple values were properly concatenated.');
    $this->assertEqual(drupal_http_build_query(array('a' => array('b' => '2', 'c' => '3'), 'd' => 'foo')), 'a%5Bb%5D=2&a%5Bc%5D=3&d=foo', 'Nested array was properly encoded.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

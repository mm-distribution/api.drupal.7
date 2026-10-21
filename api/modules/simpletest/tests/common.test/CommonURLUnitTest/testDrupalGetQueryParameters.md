# CommonURLUnitTest::testDrupalGetQueryParameters()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 141–183 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L141-L183)
- **Class:** [CommonURLUnitTest](../CommonURLUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalGetQueryParameters()
```

## Documentation

```text
Test drupal_get_query_parameters().
```

## Code

```php
  function testDrupalGetQueryParameters() {
    $original = array(
      'a' => 1,
      'b' => array(
        'd' => 4,
        'e' => array(
          'f' => 5,
        ),
      ),
      'c' => 3,
      'q' => 'foo/bar',
    );

    // Default arguments.
    $result = $_GET;
    unset($result['q']);
    $this->assertEqual(drupal_get_query_parameters(), $result, "\$_GET['q'] was removed.");

    // Default exclusion.
    $result = $original;
    unset($result['q']);
    $this->assertEqual(drupal_get_query_parameters($original), $result, "'q' was removed.");

    // First-level exclusion.
    $result = $original;
    unset($result['b']);
    $this->assertEqual(drupal_get_query_parameters($original, array('b')), $result, "'b' was removed.");

    // Second-level exclusion.
    $result = $original;
    unset($result['b']['d']);
    $this->assertEqual(drupal_get_query_parameters($original, array('b[d]')), $result, "'b[d]' was removed.");

    // Third-level exclusion.
    $result = $original;
    unset($result['b']['e']['f']);
    $this->assertEqual(drupal_get_query_parameters($original, array('b[e][f]')), $result, "'b[e][f]' was removed.");

    // Multiple exclusions.
    $result = $original;
    unset($result['a'], $result['b']['e'], $result['c']);
    $this->assertEqual(drupal_get_query_parameters($original, array('a', 'b[e]', 'c')), $result, "'a', 'b[e]', 'c' were removed.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

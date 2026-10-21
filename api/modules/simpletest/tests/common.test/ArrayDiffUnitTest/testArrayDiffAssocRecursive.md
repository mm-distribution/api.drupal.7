# ArrayDiffUnitTest::testArrayDiffAssocRecursive()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3348–3360 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3348-L3360)
- **Class:** [ArrayDiffUnitTest](../ArrayDiffUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testArrayDiffAssocRecursive()
```

## Documentation

```text
Tests drupal_array_diff_assoc_recursive().
```

## Code

```php
  public function testArrayDiffAssocRecursive() {
    $expected = array(
      'different' => 'no',
      'int_diff' => 1,
      // The 'array' key should not be returned, as it's the same.
      'array_diff' => array('same' => 'same'),
      'array_compared_to_string' => array('value'),
      'string_compared_to_array' => 'value',
      'new' => 'new',
    );

    $this->assertIdentical(drupal_array_diff_assoc_recursive($this->array1, $this->array2), $expected);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

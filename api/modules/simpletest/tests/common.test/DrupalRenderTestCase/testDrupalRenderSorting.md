# DrupalRenderTestCase::testDrupalRenderSorting()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2141–2213 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2141-L2213)
- **Class:** [DrupalRenderTestCase](../DrupalRenderTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalRenderSorting()
```

## Documentation

```text
Test sorting by weight.
```

## Code

```php
  function testDrupalRenderSorting() {
    $first = $this->randomName();
    $second = $this->randomName();
    // Build an array with '#weight' set for each element.
    $elements = array(
      'second' => array(
        '#weight' => 10,
        '#markup' => $second,
      ),
      'first' => array(
        '#weight' => 0,
        '#markup' => $first,
      ),
    );
    $output = drupal_render($elements);

    // The lowest weight element should appear last in $output.
    $this->assertTrue(strpos($output, $second) > strpos($output, $first), 'Elements were sorted correctly by weight.');

    // Confirm that the $elements array has '#sorted' set to TRUE.
    $this->assertTrue($elements['#sorted'], "'#sorted' => TRUE was added to the array");

    // Pass $elements through element_children() and ensure it remains
    // sorted in the correct order. drupal_render() will return an empty string
    // if used on the same array in the same request.
    $children = element_children($elements);
    $this->assertTrue(array_shift($children) == 'first', 'Child found in the correct order.');
    $this->assertTrue(array_shift($children) == 'second', 'Child found in the correct order.');


    // The same array structure again, but with #sorted set to TRUE.
    $elements = array(
      'second' => array(
        '#weight' => 10,
        '#markup' => $second,
      ),
      'first' => array(
        '#weight' => 0,
        '#markup' => $first,
      ),
      '#sorted' => TRUE,
    );
    $output = drupal_render($elements);

    // The elements should appear in output in the same order as the array.
    $this->assertTrue(strpos($output, $second) < strpos($output, $first), 'Elements were not sorted.');

    // The order of children with same weight should be preserved.
    $element_mixed_weight = array(
      'child5' => array('#weight' => 10),
      'child3' => array('#weight' => -10),
      'child1' => array(),
      'child4' => array('#weight' => 10),
      'child2' => array(),
      'child6' => array('#weight' => 10),
      'child9' => array(),
      'child8' => array('#weight' => 10),
      'child7' => array(),
    );

    $expected = array(
      'child3',
      'child1',
      'child2',
      'child9',
      'child7',
      'child5',
      'child4',
      'child6',
      'child8',
      );
    $this->assertEqual($expected, element_children($element_mixed_weight, TRUE), 'Order of elements with the same weight is preserved.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# RenderElementTypesTestCase::assertElements()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 482–486 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L482-L486)
- **Class:** [RenderElementTypesTestCase](../RenderElementTypesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertElements($elements)
```

## Documentation

```text
Asserts that an array of elements is rendered properly.

@param array $elements
  An array of associative arrays describing render elements and their
  expected markup. Each item in $elements must contain the following:
  - 'name': This human readable description will be displayed on the test
    results page.
  - 'value': This is the render element to test.
  - 'expected': This is the expected markup for the element in 'value'.
```

## Code

```php
  function assertElements($elements) {
    foreach($elements as $element) {
      $this->assertIdentical(drupal_render($element['value']), $element['expected'], '"' . $element['name'] . '" input rendered correctly by drupal_render().');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._

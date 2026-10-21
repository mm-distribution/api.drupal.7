# RenderElementTypesTestCase::testContainer()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 491–521 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L491-L521)
- **Class:** [RenderElementTypesTestCase](../RenderElementTypesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testContainer()
```

## Documentation

```text
Tests system #type 'container'.
```

## Code

```php
  function testContainer() {
    $elements = array(
      // Basic container with no attributes.
      array(
        'name' => "#type 'container' with no HTML attributes",
        'value' => array(
          '#type' => 'container',
          'child' => array(
            '#markup' => 'foo',
          ),
        ),
        'expected' => '<div>foo</div>',
      ),
      // Container with a class.
      array(
        'name' => "#type 'container' with a class HTML attribute",
        'value' => array(
          '#type' => 'container',
          'child' => array(
            '#markup' => 'foo',
          ),
          '#attributes' => array(
            'class' => 'bar',
          ),
        ),
        'expected' => '<div class="bar">foo</div>',
      ),
    );

    $this->assertElements($elements);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._

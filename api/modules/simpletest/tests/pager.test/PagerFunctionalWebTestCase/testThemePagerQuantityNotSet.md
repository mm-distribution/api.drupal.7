# PagerFunctionalWebTestCase::testThemePagerQuantityNotSet()

- **Type:** Method
- **File:** [`modules/simpletest/tests/pager.test`](../_file.md), lines 62–73 · [local source](../../../../../../source/modules/simpletest/tests/pager.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test#L62-L73)
- **Class:** [PagerFunctionalWebTestCase](../PagerFunctionalWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testThemePagerQuantityNotSet()
```

## Documentation

```text
Tests theme_pager() when an empty quantity is passed.
```

## Code

```php
  public function testThemePagerQuantityNotSet() {
    $variables = array(
      'element' => 0,
      'parameters' => array(),
      'quantity' => '',
      'tags' => '',
    );
    pager_default_initialize(100, 10);
    $rendered_output = theme_pager($variables);
    $this->assertNotIdentical(stripos($rendered_output, 'next'), FALSE);
    $this->assertNotIdentical(stripos($rendered_output, 'last'), FALSE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/pager.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# DrupalRenderTestCase::testDrupalRenderThemeArguments()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2268–2281 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2268-L2281)
- **Class:** [DrupalRenderTestCase](../DrupalRenderTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalRenderThemeArguments()
```

## Documentation

```text
Test passing arguments to the theme function.
```

## Code

```php
  function testDrupalRenderThemeArguments() {
    $element = array(
      '#theme' => 'common_test_foo',
    );
    // Test that defaults work.
    $this->assertEqual(drupal_render($element), 'foobar', 'Defaults work');
    $element = array(
      '#theme' => 'common_test_foo',
      '#foo' => $this->randomName(),
      '#bar' => $this->randomName(),
    );
    // Test that passing arguments to the theme function works.
    $this->assertEqual(drupal_render($element), $element['#foo'] . $element['#bar'], 'Passing arguments to theme functions works');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

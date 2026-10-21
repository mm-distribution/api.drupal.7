# ThemeTestCase::testDrupalAddRegionContent()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 162–166 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L162-L166)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalAddRegionContent()
```

## Documentation

```text
Test the drupal_add_region_content() function.
```

## Code

```php
  function testDrupalAddRegionContent() {
    $this->drupalGet('theme-test/drupal-add-region-content');
    $this->assertText('Hello');
    $this->assertText('World');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._

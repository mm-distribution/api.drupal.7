# ColorTestCase::testColor()

- **Type:** Method
- **File:** [`modules/color/color.test`](../_file.md), lines 62–66 · [local source](../../../../../source/modules/color/color.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test#L62-L66)
- **Class:** [ColorTestCase](../ColorTestCase.md)
- **Module/theme:** color

## Signature

```php
function testColor()
```

## Documentation

```text
Tests the Color module functionality.
```

## Code

```php
  function testColor() {
    foreach ($this->themes as $theme => $test_values) {
      $this->_testColor($theme, $test_values);
    }
  }
```

---
_Drupal 7.103 · [modules/color/color.test](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test) · Licensed GPL-2.0-or-later (see LICENSE)._

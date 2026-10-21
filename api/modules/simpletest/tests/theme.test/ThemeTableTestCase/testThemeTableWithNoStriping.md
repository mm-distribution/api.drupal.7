# ThemeTableTestCase::testThemeTableWithNoStriping()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 230–240 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L230-L240)
- **Class:** [ThemeTableTestCase](../ThemeTableTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeTableWithNoStriping()
```

## Documentation

```text
Tests that the 'no_striping' option works correctly.
```

## Code

```php
  function testThemeTableWithNoStriping() {
    $rows = array(
      array(
        'data' => array(1),
        'no_striping' => TRUE,
      ),
    );
    $this->content = theme('table', array('rows' => $rows));
    $this->assertNoRaw('class="odd"', 'Odd/even classes were not added because $no_striping = TRUE.');
    $this->assertNoRaw('no_striping', 'No invalid no_striping HTML attribute was printed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._

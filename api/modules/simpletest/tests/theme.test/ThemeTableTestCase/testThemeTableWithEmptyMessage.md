# ThemeTableTestCase::testThemeTableWithEmptyMessage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 214–225 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L214-L225)
- **Class:** [ThemeTableTestCase](../ThemeTableTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeTableWithEmptyMessage()
```

## Documentation

```text
Tests that the table header is printed correctly even if there are no rows,
and that the empty text is displayed correctly.
```

## Code

```php
  function testThemeTableWithEmptyMessage() {
    $header = array(
      t('Header 1'),
      array(
        'data' => t('Header 2'),
        'colspan' => 2,
      ),
    );
    $this->content = theme('table', array('header' => $header, 'rows' => array(), 'empty' => t('No strings available.')));
    $this->assertRaw('<tr class="odd"><td colspan="3" class="empty message">No strings available.</td>', 'Correct colspan was set on empty message.');
    $this->assertRaw('<thead><tr><th>Header 1</th>', 'Table header was printed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# ThemeTableTestCase::testThemeTableFooter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 245–261 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L245-L261)
- **Class:** [ThemeTableTestCase](../ThemeTableTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeTableFooter()
```

## Documentation

```text
Test that the 'footer' option works correctly.
```

## Code

```php
  function testThemeTableFooter() {
    $footer = array(
      array(
        'data' => array(1),
      ),
      array('Foo'),
    );

    $table = array(
      'rows' => array(),
      'footer' => $footer,
    );

    $this->content = theme('table', $table);
    $this->content = preg_replace('@>\s+<@', '><', $this->content);
    $this->assertRaw('<tfoot><tr><td>1</td></tr><tr><td>Foo</td></tr></tfoot>', 'Table footer found.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._

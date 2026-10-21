# TextFieldTestCase::testTextfieldWidgetsFormatted()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 138–141 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L138-L141)
- **Class:** [TextFieldTestCase](../TextFieldTestCase.md)
- **Module/theme:** text

## Signature

```php
function testTextfieldWidgetsFormatted()
```

## Documentation

```text
Test widgets + 'formatted_text' setting.
```

## Code

```php
  function testTextfieldWidgetsFormatted() {
    $this->_testTextfieldWidgetsFormatted('text', 'text_textfield');
    $this->_testTextfieldWidgetsFormatted('text_long', 'text_textarea');
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._

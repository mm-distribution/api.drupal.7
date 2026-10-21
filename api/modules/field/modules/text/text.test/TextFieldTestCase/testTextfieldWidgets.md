# TextFieldTestCase::testTextfieldWidgets()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 79–82 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L79-L82)
- **Class:** [TextFieldTestCase](../TextFieldTestCase.md)
- **Module/theme:** text

## Signature

```php
function testTextfieldWidgets()
```

## Documentation

```text
Test widgets.
```

## Code

```php
  function testTextfieldWidgets() {
    $this->_testTextfieldWidgets('text', 'text_textfield');
    $this->_testTextfieldWidgets('text_long', 'text_textarea');
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._

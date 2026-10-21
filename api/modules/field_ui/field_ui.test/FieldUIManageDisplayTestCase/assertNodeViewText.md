# FieldUIManageDisplayTestCase::assertNodeViewText()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 620–622 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L620-L622)
- **Class:** [FieldUIManageDisplayTestCase](../FieldUIManageDisplayTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function assertNodeViewText($node, $view_mode, $text, $message)
```

## Documentation

```text
Asserts that a string is found in the rendered node in a view mode.

@param $node
  The node.
@param $view_mode
  The view mode in which the node should be displayed.
@param $text
  Plain text to look for.
@param $message
  Message to display.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  function assertNodeViewText($node, $view_mode, $text, $message) {
    return $this->assertNodeViewTextHelper($node, $view_mode, $text, $message, FALSE);
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._

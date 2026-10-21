# FieldUIManageDisplayTestCase::assertNodeViewTextHelper()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 662–685 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L662-L685)
- **Class:** [FieldUIManageDisplayTestCase](../FieldUIManageDisplayTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function assertNodeViewTextHelper($node, $view_mode, $text, $message, $not_exists)
```

## Documentation

```text
Asserts that a string is (not) found in the rendered nodein a view mode.

This helper function is used by assertNodeViewText() and
assertNodeViewNoText().

@param $node
  The node.
@param $view_mode
  The view mode in which the node should be displayed.
@param $text
  Plain text to look for.
@param $message
  Message to display.
@param $not_exists
  TRUE if this text should not exist, FALSE if it should.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  function assertNodeViewTextHelper($node, $view_mode, $text, $message, $not_exists) {
    // Make sure caches on the tester side are refreshed after changes
    // submitted on the tested side.
    field_info_cache_clear();

    // Save current content so that we can restore it when we're done.
    $old_content = $this->drupalGetContent();

    // Render a cloned node, so that we do not alter the original.
    $clone = clone $node;
    $element = node_view($clone, $view_mode);
    $output = drupal_render($element);
    $this->verbose(t('Rendered node - view mode: @view_mode', array('@view_mode' => $view_mode)) . '<hr />'. $output);

    // Assign content so that DrupalWebTestCase functions can be used.
    $this->drupalSetContent($output);
    $method = ($not_exists ? 'assertNoText' : 'assertText');
    $return = $this->{$method}((string) $text, $message);

    // Restore previous content.
    $this->drupalSetContent($old_content);

    return $return;
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._

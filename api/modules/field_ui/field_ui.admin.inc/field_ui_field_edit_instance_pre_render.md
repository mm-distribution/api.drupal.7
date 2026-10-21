# field_ui_field_edit_instance_pre_render()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1972–1990 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1972-L1990)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_edit_instance_pre_render($element)
```

## Documentation

```text
Pre-render function for field instance settings.

Combines the instance, widget, and other settings into a single fieldset so
that elements within each group can be shown at different weights as if they
all had the same parent.
```

## Code

```php
function field_ui_field_edit_instance_pre_render($element) {
  // Merge the widget settings into the main form.
  if (isset($element['widget']['settings'])) {
    foreach (element_children($element['widget']['settings']) as $key) {
      $element['widget_' . $key] = $element['widget']['settings'][$key];
    }
    unset($element['widget']['settings']);
  }

  // Merge the instance settings into the main form.
  if (isset($element['settings'])) {
    foreach (element_children($element['settings']) as $key) {
      $element['instance_' . $key] = $element['settings'][$key];
    }
    unset($element['settings']);
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

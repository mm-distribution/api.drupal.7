# hook_element_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 684–689 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L684-L689)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_element_info()
```

## Documentation

```text
Allows modules to declare their own Form API element types and specify their
default values.

This hook allows modules to declare their own form element types and to
specify their default values. The values returned by this hook will be
merged with the elements returned by hook_form() implementations and so
can return defaults for any Form APIs keys in addition to those explicitly
mentioned below.

Each of the form element types defined by this hook is assumed to have
a matching theme function, e.g. theme_elementtype(), which should be
registered with hook_theme() as normal.

For more information about custom element types see the explanation at
http://drupal.org/node/169815.

@return
 An associative array describing the element types being defined. The array
 contains a sub-array for each element type, with the machine-readable type
 name as the key. Each sub-array has a number of possible attributes:
 - "#input": boolean indicating whether or not this element carries a value
   (even if it's hidden).
 - "#process": array of callback functions taking $element, $form_state,
   and $complete_form.
 - "#after_build": array of callback functions taking $element and $form_state.
 - "#validate": array of callback functions taking $form and $form_state.
 - "#element_validate": array of callback functions taking $element and
   $form_state.
 - "#pre_render": array of callback functions taking $element and $form_state.
 - "#post_render": array of callback functions taking $element and $form_state.
 - "#submit": array of callback functions taking $form and $form_state.
 - "#title_display": optional string indicating if and how #title should be
   displayed, see theme_form_element() and theme_form_element_label().

@see hook_element_info_alter()
@see system_element_info()
```

## Code

```php
function hook_element_info() {
  $types['filter_format'] = array(
    '#input' => TRUE,
  );
  return $types;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_element_info()".

- [contextual_element_info()](../../contextual/contextual.module/contextual_element_info.md) — `modules/contextual/contextual.module`
- [field_ui_element_info()](../../field_ui/field_ui.module/field_ui_element_info.md) — `modules/field_ui/field_ui.module`
- [file_element_info()](../../file/file.module/file_element_info.md) — `modules/file/file.module`
- [filter_element_info()](../../filter/filter.module/filter_element_info.md) — `modules/filter/filter.module`
- [system_element_info()](../system.module/system_element_info.md) — `modules/system/system.module`
- [user_element_info()](../../user/user.module/user_element_info.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

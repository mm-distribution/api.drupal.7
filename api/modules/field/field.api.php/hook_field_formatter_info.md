# hook_field_formatter_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1091–1121 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1091-L1121)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_formatter](../../../topics/field_formatter.md)

## Signature

```php
function hook_field_formatter_info()
```

## Documentation

```text
Expose Field API formatter types.

Formatters handle the display of field values. Formatter hooks are typically
called by the Field Attach API field_attach_prepare_view() and
field_attach_view() functions.

@return
  An array describing the formatter types implemented by the module.
  The keys are formatter type names. To avoid name clashes, formatter type
  names should be prefixed with the name of the module that exposes them.
  The values are arrays describing the formatter type, with the following
  key/value pairs:
  - label: The human-readable name of the formatter type.
  - description: A short description for the formatter type.
  - field types: An array of field types the formatter supports.
  - settings: An array whose keys are the names of the settings available
    for the formatter type, and whose values are the default values for
    those settings.

@see hook_field_formatter_info_alter()
@see hook_field_formatter_view()
@see hook_field_formatter_prepare_view()
```

## Code

```php
function hook_field_formatter_info() {
  return array(
    'text_default' => array(
      'label' => t('Default'),
      'field types' => array('text', 'text_long', 'text_with_summary'),
    ),
    'text_plain' => array(
      'label' => t('Plain text'),
      'field types' => array('text', 'text_long', 'text_with_summary'),
    ),

    // The text_trimmed formatter displays the trimmed version of the
    // full element of the field. It is intended to be used with text
    // and text_long fields. It also works with text_with_summary
    // fields though the text_summary_or_trimmed formatter makes more
    // sense for that field type.
    'text_trimmed' => array(
      'label' => t('Trimmed'),
      'field types' => array('text', 'text_long', 'text_with_summary'),
    ),

    // The 'summary or trimmed' field formatter for text_with_summary
    // fields displays returns the summary element of the field or, if
    // the summary is empty, the trimmed version of the full element
    // of the field.
    'text_summary_or_trimmed' => array(
      'label' => t('Summary or trimmed'),
      'field types' => array('text_with_summary'),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_formatter_info()".

- [field_test_field_formatter_info()](../tests/field_test.field.inc/field_test_field_formatter_info.md) — `modules/field/tests/field_test.field.inc`
- [file_field_formatter_info()](../../file/file.field.inc/file_field_formatter_info.md) — `modules/file/file.field.inc`
- [image_field_formatter_info()](../../image/image.field.inc/image_field_formatter_info.md) — `modules/image/image.field.inc`
- [list_field_formatter_info()](../modules/list/list.module/list_field_formatter_info.md) — `modules/field/modules/list/list.module`
- [number_field_formatter_info()](../modules/number/number.module/number_field_formatter_info.md) — `modules/field/modules/number/number.module`
- [taxonomy_field_formatter_info()](../../taxonomy/taxonomy.module/taxonomy_field_formatter_info.md) — `modules/taxonomy/taxonomy.module`
- [text_field_formatter_info()](../modules/text/text.module/text_field_formatter_info.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

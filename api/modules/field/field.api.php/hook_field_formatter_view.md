# hook_field_formatter_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1240–1282 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1240-L1282)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_formatter](../../../topics/field_formatter.md)

## Signature

```php
function hook_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display)
```

## Documentation

```text
Build a renderable array for a field value.

@param $entity_type
  The type of $entity.
@param $entity
  The entity being displayed.
@param $field
  The field structure.
@param $instance
  The field instance.
@param $langcode
  The language associated with $items.
@param $items
  Array of values for this field.
@param $display
  The display settings to use, as found in the 'display' entry of instance
  definitions. The array notably contains the following keys and values;
  - type: The name of the formatter to use.
  - settings: The array of formatter settings.

@return
  A renderable array for the $items, as an array of child elements keyed
  by numeric indexes starting from 0.
```

## Code

```php
function hook_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  $element = array();
  $settings = $display['settings'];

  switch ($display['type']) {
    case 'sample_field_formatter_simple':
      // Common case: each value is displayed individually in a sub-element
      // keyed by delta. The field.tpl.php template specifies the markup
      // wrapping each value.
      foreach ($items as $delta => $item) {
        $element[$delta] = array('#markup' => $settings['some_setting'] . $item['value']);
      }
      break;

    case 'sample_field_formatter_themeable':
      // More elaborate formatters can defer to a theme function for easier
      // customization.
      foreach ($items as $delta => $item) {
        $element[$delta] = array(
          '#theme' => 'mymodule_theme_sample_field_formatter_themeable',
          '#data' => $item['value'],
          '#some_setting' => $settings['some_setting'],
        );
      }
      break;

    case 'sample_field_formatter_combined':
      // Some formatters might need to display all values within a single piece
      // of markup.
      $rows = array();
      foreach ($items as $delta => $item) {
        $rows[] = array($delta, $item['value']);
      }
      $element[0] = array(
        '#theme' => 'table',
        '#header' => array(t('Delta'), t('Value')),
        '#rows' => $rows,
      );
      break;
  }

  return $element;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_formatter_view()".

- [field_test_field_formatter_view()](../tests/field_test.field.inc/field_test_field_formatter_view.md) — `modules/field/tests/field_test.field.inc`
- [file_field_formatter_view()](../../file/file.field.inc/file_field_formatter_view.md) — `modules/file/file.field.inc`
- [image_field_formatter_view()](../../image/image.field.inc/image_field_formatter_view.md) — `modules/image/image.field.inc`
- [list_field_formatter_view()](../modules/list/list.module/list_field_formatter_view.md) — `modules/field/modules/list/list.module`
- [number_field_formatter_view()](../modules/number/number.module/number_field_formatter_view.md) — `modules/field/modules/number/number.module`
- [taxonomy_field_formatter_view()](../../taxonomy/taxonomy.module/taxonomy_field_formatter_view.md) — `modules/taxonomy/taxonomy.module`
- [text_field_formatter_view()](../modules/text/text.module/text_field_formatter_view.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

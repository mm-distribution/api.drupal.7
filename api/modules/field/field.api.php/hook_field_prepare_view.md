# hook_field_prepare_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 388–402 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L388-L402)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items)
```

## Documentation

```text
Prepare field values prior to display.

This hook is invoked before the field values are handed to formatters
for display, and runs before the formatters' own
hook_field_formatter_prepare_view().

Unlike most other field hooks, this hook operates on multiple entities. The
$entities, $instances and $items parameters are arrays keyed by entity ID.
For performance reasons, information for all available entities should be
loaded in a single query where possible.

Make changes or additions to field values by altering the $items parameter by
reference. There is no return value.

@param $entity_type
  The type of $entity.
@param $entities
  Array of entities being displayed, keyed by entity ID.
@param $field
  The field structure for the operation.
@param $instances
  Array of instance structures for $field for each entity, keyed by entity
  ID.
@param $langcode
  The language associated to $items.
@param $items
  $entity->{$field['field_name']}, or an empty array if unset.
```

## Code

```php
function hook_field_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items) {
  // Sample code from image.module: if there are no images specified at all,
  // use the default image.
  foreach ($entities as $id => $entity) {
    if (empty($items[$id]) && $field['settings']['default_image']) {
      if ($file = file_load($field['settings']['default_image'])) {
        $items[$id][0] = (array) $file + array(
          'is_default' => TRUE,
          'alt' => '',
          'title' => '',
        );
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_prepare_view()".

- [file_field_prepare_view()](../../file/file.field.inc/file_field_prepare_view.md) — `modules/file/file.field.inc`
- [image_field_prepare_view()](../../image/image.field.inc/image_field_prepare_view.md) — `modules/image/image.field.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

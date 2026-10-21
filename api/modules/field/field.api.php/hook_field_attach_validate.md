# hook_field_attach_validate()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1364–1378 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1364-L1378)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_validate($entity_type, $entity, &$errors)
```

## Documentation

```text
Act on field_attach_validate().

This hook is invoked after the field module has performed the operation.

See field_attach_validate() for details and arguments.

@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $entity
  The entity with fields to validate.
@param array $errors
  The array of errors (keyed by field name, language code, and delta) that
  have already been reported for the entity. The function should add its
  errors to this array. Each error is an associative array with the following
  keys and values:
  - error: An error code (should be a string prefixed with the module name).
  - message: The human readable message to be displayed.
```

## Code

```php
function hook_field_attach_validate($entity_type, $entity, &$errors) {
  // Make sure any images in article nodes have an alt text.
  if ($entity_type == 'node' && $entity->type == 'article' && !empty($entity->field_image)) {
    foreach ($entity->field_image as $langcode => $items) {
      foreach ($items as $delta => $item) {
        if (!empty($item['fid']) && empty($item['alt'])) {
          $errors['field_image'][$langcode][$delta][] = array(
            'error' => 'field_example_invalid',
            'message' => t('All images in articles need to have an alternative text set.'),
          );
        }
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_validate()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

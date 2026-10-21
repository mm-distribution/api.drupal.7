# field_info_extra_fields()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 688–693 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L688-L693)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_extra_fields($entity_type, $bundle, $context)
```

## Documentation

```text
Returns a list and settings of pseudo-field elements in a given bundle.

If $context is 'form', an array with the following structure:
@code
  array(
    'name_of_pseudo_field_component' => array(
      'label' => The human readable name of the component,
      'description' => A short description of the component content,
      'weight' => The weight of the component in edit forms,
    ),
    'name_of_other_pseudo_field_component' => array(
      // ...
    ),
  );
@endcode

If $context is 'display', an array with the following structure:
@code
  array(
    'name_of_pseudo_field_component' => array(
      'label' => The human readable name of the component,
      'description' => A short description of the component content,
      // One entry per view mode, including the 'default' mode:
      'display' => array(
        'default' => array(
          'weight' => The weight of the component in displayed entities in
            this view mode,
          'visible' => TRUE if the component is visible, FALSE if hidden, in
            displayed entities in this view mode,
        ),
        'teaser' => array(
          // ...
        ),
      ),
    ),
    'name_of_other_pseudo_field_component' => array(
      // ...
    ),
  );
@endcode

@param $entity_type
  The type of entity; e.g. 'node' or 'user'.
@param $bundle
  The bundle name.
@param $context
  The context for which the list of pseudo-fields is requested. Either
  'form' or 'display'.

@return
  The array of pseudo-field elements in the bundle.
```

## Code

```php
function field_info_extra_fields($entity_type, $bundle, $context) {
  $cache = _field_info_field_cache();
  $info = $cache->getBundleExtraFields($entity_type, $bundle);

  return isset($info[$context]) ? $info[$context] : array();
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

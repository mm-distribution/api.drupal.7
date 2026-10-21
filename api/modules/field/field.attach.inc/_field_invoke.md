# _field_invoke()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 181–231 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L181-L231)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function _field_invoke($op, $entity_type, $entity, &$a = NULL, &$b = NULL, $options = array())
```

## Documentation

```text
Invoke a field hook.

@param $op
  Possible operations include:
  - form
  - validate
  - presave
  - insert
  - update
  - delete
  - delete revision
  - view
  - prepare translation
@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The fully formed $entity_type entity.
@param $a
  - The $form in the 'form' operation.
  - The value of $view_mode in the 'view' operation.
  - Otherwise NULL.
@param $b
  - The $form_state in the 'submit' operation.
  - Otherwise NULL.
@param $options
  An associative array of additional options, with the following keys:
 - 'field_name': The name of the field whose operation should be
   invoked. By default, the operation is invoked on all the fields
   in the entity's bundle. NOTE: This option is not compatible with
   the 'deleted' option; the 'field_id' option should be used
   instead.
 - 'field_id': The id of the field whose operation should be
   invoked. By default, the operation is invoked on all the fields
   in the entity's' bundles.
 - 'default': A boolean value, specifying which implementation of
   the operation should be invoked.
   - if FALSE (default), the field types implementation of the operation
     will be invoked (hook_field_[op])
   - If TRUE, the default field implementation of the field operation
     will be invoked (field_default_[op])
   Internal use only. Do not explicitely set to TRUE, but use
   _field_invoke_default() instead.
 - 'deleted': If TRUE, the function will operate on deleted fields
   as well as non-deleted fields. If unset or FALSE, only
   non-deleted fields are operated on.
 - 'language': A language code or an array of language codes keyed by field
   name. It will be used to narrow down to a single value the available
   languages to act on.
```

## Code

```php
function _field_invoke($op, $entity_type, $entity, &$a = NULL, &$b = NULL, $options = array()) {
  // Merge default options.
  $default_options = array(
    'default' => FALSE,
    'deleted' => FALSE,
    'language' => NULL,
  );
  $options += $default_options;

  // Determine the list of instances to iterate on.
  list(, , $bundle) = entity_extract_ids($entity_type, $entity);
  $instances = _field_invoke_get_instances($entity_type, $bundle, $options);

  // Iterate through the instances and collect results.
  $return = array();
  foreach ($instances as $instance) {
    // field_info_field() is not available for deleted fields, so use
    // field_info_field_by_id().
    $field = field_info_field_by_id($instance['field_id']);
    $field_name = $field['field_name'];
    $function = $options['default'] ? 'field_default_' . $op : $field['module'] . '_field_' . $op;
    if (function_exists($function)) {
      // Determine the list of languages to iterate on.
      $available_languages = field_available_languages($entity_type, $field);
      $languages = _field_language_suggestion($available_languages, $options['language'], $field_name);

      foreach ($languages as $langcode) {
        $items = isset($entity->{$field_name}[$langcode]) ? $entity->{$field_name}[$langcode] : array();
        $result = $function($entity_type, $entity, $field, $instance, $langcode, $items, $a, $b);
        if (isset($result)) {
          // For hooks with array results, we merge results together.
          // For hooks with scalar results, we collect results in an array.
          if (is_array($result)) {
            $return = array_merge($return, $result);
          }
          else {
            $return[] = $result;
          }
        }

        // Populate $items back in the field values, but avoid replacing missing
        // fields with an empty array (those are not equivalent on update).
        if ($items !== array() || isset($entity->{$field_name}[$langcode])) {
          $entity->{$field_name}[$langcode] = $items;
        }
      }
    }
  }

  return $return;
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

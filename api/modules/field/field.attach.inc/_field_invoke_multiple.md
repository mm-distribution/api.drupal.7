# _field_invoke_multiple()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 278–372 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L278-L372)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function _field_invoke_multiple($op, $entity_type, $entities, &$a = NULL, &$b = NULL, $options = array())
```

## Documentation

```text
Invoke a field hook across fields on multiple entities.

@param $op
  Possible operations include:
  - load
  - prepare_view
  For all other operations, use _field_invoke() / field_invoke_default()
  instead.
@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entities
  An array of entities, keyed by entity id.
@param $a
  - The $age parameter in the 'load' operation.
  - Otherwise NULL.
@param $b
  Currently always NULL.
@param $options
  An associative array of additional options, with the following keys:
 - 'field_name': The name of the field whose operation should be
   invoked. By default, the operation is invoked on all the fields
   in the entity's bundle. NOTE: This option is not compatible with
   the 'deleted' option; the 'field_id' option should be used instead.
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
   _field_invoke_multiple_default() instead.
 - 'deleted': If TRUE, the function will operate on deleted fields
   as well as non-deleted fields. If unset or FALSE, only
   non-deleted fields are operated on.
 - 'language': A language code or an array of arrays of language codes keyed
   by entity id and field name. It will be used to narrow down to a single
   value the available languages to act on.

@return
  An array of returned values keyed by entity id.
```

## Code

```php
function _field_invoke_multiple($op, $entity_type, $entities, &$a = NULL, &$b = NULL, $options = array()) {
  // Merge default options.
  $default_options = array(
    'default' => FALSE,
    'deleted' => FALSE,
    'language' => NULL,
  );
  $options += $default_options;

  $fields = array();
  $grouped_instances = array();
  $grouped_entities = array();
  $grouped_items = array();
  $return = array();

  // Go through the entities and collect the fields on which the hook should be
  // invoked.
  //
  // We group fields by id, not by name, because this function can operate on
  // deleted fields which may have non-unique names. However, entities can only
  // contain data for a single field for each name, even if that field
  // is deleted, so we reference field data via the
  // $entity->$field_name property.
  foreach ($entities as $entity) {
    // Determine the list of instances to iterate on.
    list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
    $instances = _field_invoke_get_instances($entity_type, $bundle, $options);

    foreach ($instances as $instance) {
      $field_id = $instance['field_id'];
      $field_name = $instance['field_name'];
      $field = field_info_field_by_id($field_id);
      $function = $options['default'] ? 'field_default_' . $op : $field['module'] . '_field_' . $op;
      if (function_exists($function)) {
        // Add the field to the list of fields to invoke the hook on.
        if (!isset($fields[$field_id])) {
          $fields[$field_id] = $field;
        }
        // Extract the field values into a separate variable, easily accessed
        // by hook implementations.
        // Unless a language suggestion is provided we iterate on all the
        // available languages.
        $available_languages = field_available_languages($entity_type, $field);
        $language = is_array($options['language']) && !empty($options['language'][$id]) ? $options['language'][$id] : $options['language'];
        $languages = _field_language_suggestion($available_languages, $language, $field_name);
        foreach ($languages as $langcode) {
          $grouped_items[$field_id][$langcode][$id] = isset($entity->{$field_name}[$langcode]) ? $entity->{$field_name}[$langcode] : array();
          // Group the instances and entities corresponding to the current
          // field.
          $grouped_instances[$field_id][$langcode][$id] = $instance;
          $grouped_entities[$field_id][$langcode][$id] = $entities[$id];
        }
      }
    }
    // Initialize the return value for each entity.
    $return[$id] = array();
  }

  // For each field, invoke the field hook and collect results.
  foreach ($fields as $field_id => $field) {
    $field_name = $field['field_name'];
    $function = $options['default'] ? 'field_default_' . $op : $field['module'] . '_field_' . $op;
    // Iterate over all the field translations.
    foreach ($grouped_items[$field_id] as $langcode => &$items) {
      $entities = $grouped_entities[$field_id][$langcode];
      $instances = $grouped_instances[$field_id][$langcode];
      $results = $function($entity_type, $entities, $field, $instances, $langcode, $items, $a, $b);
      if (isset($results)) {
        // Collect results by entity.
        // For hooks with array results, we merge results together.
        // For hooks with scalar results, we collect results in an array.
        foreach ($results as $id => $result) {
          if (is_array($result)) {
            $return[$id] = array_merge($return[$id], $result);
          }
          else {
            $return[$id][] = $result;
          }
        }
      }
    }

    // Populate field values back in the entities, but avoid replacing missing
    // fields with an empty array (those are not equivalent on update).
    foreach ($grouped_entities[$field_id] as $langcode => $entities) {
      foreach ($entities as $id => $entity) {
        if ($grouped_items[$field_id][$langcode][$id] !== array() || isset($entity->{$field_name}[$langcode])) {
          $entity->{$field_name}[$langcode] = $grouped_items[$field_id][$langcode][$id];
        }
      }
    }
  }

  return $return;
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

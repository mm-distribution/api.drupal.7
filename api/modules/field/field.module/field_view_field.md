# field_view_field()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 874–922 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L874-L922)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_view_field($entity_type, $entity, $field_name, $display = array(), $langcode = NULL)
```

## Documentation

```text
Returns a renderable array for the value of a single field in an entity.

The resulting output is a fully themed field with label and multiple values.

This function can be used by third-party modules that need to output an
isolated field.
- Do not use inside node (or any other entity) templates; use
  render($content[FIELD_NAME]) instead.
- Do not use to display all fields in an entity; use
  field_attach_prepare_view() and field_attach_view() instead.
- The field_view_value() function can be used to output a single formatted
  field value, without label or wrapping field markup.

The function takes care of invoking the prepare_view steps. It also respects
field access permissions.

@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $entity
  The entity containing the field to display. Must at least contain the id
  key and the field data to display.
@param $field_name
  The name of the field to display.
@param $display
  Can be either:
  - The name of a view mode. The field will be displayed according to the
    display settings specified for this view mode in the $instance
    definition for the field in the entity's bundle.
    If no display settings are found for the view mode, the settings for
    the 'default' view mode will be used.
  - An array of display settings, as found in the 'display' entry of
    $instance definitions. The following key/value pairs are allowed:
    - label: (string) Position of the label. The default 'field' theme
      implementation supports the values 'inline', 'above' and 'hidden'.
      Defaults to 'above'.
    - type: (string) The formatter to use. Defaults to the
      'default_formatter' for the field type, specified in
      hook_field_info(). The default formatter will also be used if the
      requested formatter is not available.
    - settings: (array) Settings specific to the formatter. Defaults to the
      formatter's default settings, specified in
      hook_field_formatter_info().
    - weight: (float) The weight to assign to the renderable element.
      Defaults to 0.
@param $langcode
  (Optional) The language the field values are to be shown in. The site's
  current language fallback logic will be applied no values are available
  for the language. If no language is provided the current language will be
  used.
@return
  A renderable array for the field value.

@see field_view_value()
```

## Code

```php
function field_view_field($entity_type, $entity, $field_name, $display = array(), $langcode = NULL) {
  $output = array();

  if ($field = field_info_field($field_name)) {
    if (is_array($display)) {
      // When using custom display settings, fill in default values.
      $cache = _field_info_field_cache();
      $display = $cache->prepareInstanceDisplay($display, $field["type"]);
    }

    // Hook invocations are done through the _field_invoke() functions in
    // 'single field' mode, to reuse the language fallback logic.
    // Determine the actual language to display for the field, given the
    // languages available in the field data.
    $display_language = field_language($entity_type, $entity, $field_name, $langcode);
    $options = array('field_name' => $field_name, 'language' => $display_language);
    $null = NULL;

    // Invoke prepare_view steps if needed.
    if (empty($entity->_field_view_prepared)) {
      list($id) = entity_extract_ids($entity_type, $entity);

      // First let the field types do their preparation.
      _field_invoke_multiple('prepare_view', $entity_type, array($id => $entity), $display, $null, $options);
      // Then let the formatters do their own specific massaging.
      _field_invoke_multiple_default('prepare_view', $entity_type, array($id => $entity), $display, $null, $options);
    }

    // Build the renderable array.
    $result = _field_invoke_default('view', $entity_type, $entity, $display, $null, $options);

    // Invoke hook_field_attach_view_alter() to let other modules alter the
    // renderable array, as in a full field_attach_view() execution.
    $context = array(
      'entity_type' => $entity_type,
      'entity' => $entity,
      'view_mode' => '_custom',
      'display' => $display,
      'language' => $langcode,
    );
    drupal_alter('field_attach_view', $result, $context);

    if (isset($result[$field_name])) {
      $output = $result[$field_name];
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
